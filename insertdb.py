from tournament import registerPlayer, reportMatch, connect
import random

for i in range(0,15):
    registerPlayer("player%s" % i)

def createRandomMatches(num_matches):
    db = connect()
    cursor = db.cursor()
    cursor.execute("select * from players")
    player_list = cursor.fetchall()
    db.close()
    num_players = len(player_list)
    for i in xrange(num_matches):
        print 'match %s' % (i+1)
        player1_index = random.randint(0, num_players - 1)
        player2_index = random.randint(0, num_players - 1)
        if player2_index == player1_index:
            player2_index = (player1_index + 1) % num_players
        winner_id = player_list[player1_index][0]
        winner_name = player_list[player1_index][1]
        loser_id = player_list[player2_index][0]
        loser_name = player_list[player2_index][0]
        reportMatch(winner_id, loser_id)
        print "%s (id = %s) beat %s (id = %s)" % (
            winner_name,
            winner_id,
            loser_name,
            loser_id)

createRandomMatches(10)