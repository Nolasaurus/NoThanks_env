## Game Setup

## for 3-5 players, give 11 counters; for 6 players, give
## 9 counters; and for 7 players, give 7 counters

def gameSetup(numPlayers):
    import random
    tokenDict = {'3':11, '4':11, '5':11,'6':9,'7':7}
    
    cards_in_play = random.sample(range(3,36), 24) ## from cards numbered 3-35 remove 9 cards at random 

    ## Player Class
    
    class Player:
        def __init__(self, playerID, cards_in_hand, counters, score):
            self.playerID = playerID
            self.cards_in_hand = cards_in_hand
            self.counters = counters
            self.score = score

        def play(self, cardUp, counters_on_card):
            if playerList[0].counters+playerList[1].counters+playerList[2].counters+counters_on_card != (tokenDict[str(numPlayers)]*numPlayers):
                raise ValueError('COUNTER MISMATCH - NUMBER OF COUNTERS NOT CONSERVED', 
                playerList[0].counters, playerList[1].counters, playerList[2].counters+counters_on_card)
                
            if self.counters == 0:
                self.cards_in_hand.append(cardUp)
                self.counters += counters_on_card
                return 1 # take card and tell gameLoop that you did
            else: 
                #threshhold = 1-1/(self.counters) # 10 ctrs = 0.9, 1 ctrs = 0
                if cardUp-counters_on_card > 1: 
                    self.counters = self.counters-1
                    return 0 #No Thanks! <roll credits>
                    
                else: 
                    self.cards_in_hand.append(cardUp)
                    self.counters += counters_on_card
                    return 1 #take card

    # Create players and assign tokens, IDs
    playerList = []
    for x in range(numPlayers):
        playerList.append(Player('player'+str(x), [], tokenDict[str(numPlayers)],0))
    
    return playerList, cards_in_play