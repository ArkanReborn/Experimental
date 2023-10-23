import math
import random


cards = {
    "1": "ace",
    "2": "2",
    "3": "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9",
    "10" : "10",
    "11" : "King",
    "12" : "Queen",
    "13" : "Jack",
}

hand_start = 2
curr_cards = 1


for card in cards:
    while card in hand:
        
        card_type = random.randint(1, 4)
        start_cards = random.randint(1, 13)

        hand = str(start_cards)

        if curr_cards <= hand_start:

            hand = hand.replace(card, cards[card])

            print(f'Your card is a {hand} of hearts')

    #        if card_type == "1":
    #            print(f'Your card is a {hand} of hearts')        
    #        elif card_type == "2":
    #            print(f'Your card is a {hand} of spades')
    #        elif card_type == "3":
    #            print(f'Your card is a {hand} of diamonds')
    #        elif card_type == "4":
    #            print(f'Your card is a {hand} of clubs')

            curr_cards += 1