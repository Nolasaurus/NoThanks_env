##Game Core for 'No Thanks'

## get players 
from gameSetup import gameSetup

playerList, cards_in_deck = gameSetup(3)
## run game to completion
def gameLoop():
    global cards_in_deck
    for cardUp in cards_in_deck:
        counters_on_card = 0
        taken = False
        while taken == False:

            for player in playerList:

                if player.play(cardUp, counters_on_card):
                    cards_in_deck = cards_in_deck[1:]
                    taken = True
                    break
                
                counters_on_card+=1

gameLoop()

#Calculate scores
def calc_score(player):
    score = 0
    player.cards_in_hand.sort()

    for card in player.cards_in_hand:
        if (card-1) in player.cards_in_hand:
            pass
        else:
            score+=card
            
    player.score = score

    return player.score, player.counters, player.score-player.counters


## score hand
hand_score = []
counter_score = []
net_score = []
for player in playerList:
    hs, cs, ns = calc_score(player)

    hand_score.append(hs)
    counter_score.append(cs)
    net_score.append(ns)

print('Winner: Player', net_score.index(min(net_score)), 'with a score of', min(net_score))

print(playerList[0].score, playerList[0].counters, playerList[0].score-playerList[0].counters)
print(playerList[1].score, playerList[1].counters, playerList[1].score-playerList[1].counters)
print(playerList[2].score, playerList[2].counters, playerList[2].score-playerList[2].counters)