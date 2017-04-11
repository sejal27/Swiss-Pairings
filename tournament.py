#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name = "tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    # return psycopg2.connect("dbname=tournament")
    params = (database_name,)
    try:
        db = psycopg2.connect("dbname=%s", params)
        cursor = db.cursor()
        return db, cursor   
    except:
        print("Error connecting to the database %s", params)


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    cursor.execute("truncate table matches")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    # Also deletes the matches related to the player being deleted.
    cursor.execute("truncate table players cascade")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    cursor.execute("select count(id) as pcount from players")
    player_count = cursor.fetchone()  # Returns a tuple
    db.close()
    if player_count:
        # Returns the first value in the tuple if not null
        return player_count[0]
    else:
        return 0


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    params = (name,)
    # Inserts the player into the database
    cursor.execute("insert into players (name) values (%s)", params)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute("select * from v_standings")
    playerStandings = cursor.fetchall()
    db.close()
    return playerStandings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cursor = db.cursor()
    params = (winner, loser)
    cursor.execute(
        "insert into matches (winner, loser) values (%s, %s)", params)
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairs = []
    standings = playerStandings()
    for s in range(1, len(standings), 2):
        # Since the list is sorted by wins, the two consecutive players are
        # paired.
        pairs.append((standings[s - 1][0], standings[s - 1]
                      [1], standings[s][0], standings[s][1]))
    return pairs
