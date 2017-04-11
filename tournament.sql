-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

drop database tournament; -- Drop any previous db that existed
create database tournament; -- Dreate a new tournament database
-- Connect to the database
\c tournament; 
create table players (id serial primary key, name text); -- Create players table with primary key as player id, of type serial
create table matches (id serial primary key, -- create matches table containing player ids as foriegn keys for winner and loser
    winner integer references players (id), 
    loser integer references players (id));

/* Database Views */

-- View v_matches : list of players and the total number of matches played by them
create view v_matches as 
    select players.id as id, cast(count(matches.id) as integer) as matches 
        from players
        left join matches 
        on (players.id = matches.winner or players.id = matches.loser) 
        group by players.id 
        order by matches desc;

-- View v_wins: list of players sorted by total number of wins
create view v_wins as
    select players.id as id, cast(count(players.name) as integer) as wins from players, matches
        where players.id = matches.winner
        group by players.id
        order by wins desc;

-- View v_standings: list of player standings sorted by number of wins. Created by using joins on players table, views v_matches and v_wins
create view v_standings as
    select players.id, 
           players.name,
           case when v_wins.wins is null then 0 else v_wins.wins end,
           case when v_matches.matches is null then 0 else v_matches.matches end
        from players
        left join v_matches on players.id = v_matches.id
        left join v_wins on players.id = v_wins.id
        order by 
            case when v_wins.wins is null then 0 else v_wins.wins end 
            desc;
\q