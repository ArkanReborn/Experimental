import random

def player_game(cards, hand, card_type=0, card_num=0):
    card_face = ""
    for card in cards:
        hand = hand.replace(card, cards[card])

    if card_type == 0 or card_type > 4:
        raise ValueError(f'Error Invalid Card Type!')
    elif card_type == 1:
        card_face = "Hearts"
    elif card_type == 2:
        card_face = "Spades"
    elif card_type == 3:
        card_face = "Diamonds"
    elif card_type == 4:
        card_face = "Clubs"

    print(f'Player Card {card_num}: {hand} of {card_face}')
    return 

def dealer_game(cards, hand, card_type=0, card_num=0):
    card_face = ""
    for card in cards:
        hand = hand.replace(card, cards[card])

    if card_type == 0 or card_type > 4:
        raise ValueError(f'Error Invalid Card Type!')
    elif card_type == 1:
        card_face = "Hearts"
    elif card_type == 2:
        card_face = "Spades"
    elif card_type == 3:
        card_face = "Diamonds"
    elif card_type == 4:
        card_face = "Clubs"

    print(f'Dealer Card {card_num}: {hand} of {card_face}')
    return 

cards = {
    "2" : "2",
    "3" : "3",
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
    "14" : "Ace",
}

# Player Cards
player_card_type1 = random.randint(1, 4)
player_start_cards1 = random.randint(2, 14)
player_hand1 = str(player_start_cards1)

player_card_type2 = random.randint(1, 4)
player_start_cards2 = random.randint(2, 14)
player_hand2 = str(player_start_cards2)

# Player Cards 1 and 2
player_game1 = player_game(cards, player_hand1, player_card_type1, 1)
player_game2 = player_game(cards, player_hand2, player_card_type2, 2)

# Dealer Cards
dealer_card_type1 = random.randint(1, 4)
dealer_start_cards1 = random.randint(2, 14)
dealer_hand1 = str(dealer_start_cards1)

dealer_card_type2 = random.randint(1, 4)
dealer_start_cards2 = random.randint(2, 14)
dealer_hand2 = str(dealer_start_cards2)

# Dealer Cards 1 and 2
dealer_game1 = dealer_game(cards, dealer_hand1, dealer_card_type1, 1)
dealer_game2 = dealer_game(cards, dealer_hand2, dealer_card_type2, 2)


# Compare Player and Dealer Cards
value = 0

# Resolving Player Ace Value(s)
if (player_start_cards1 or player_start_cards2) == 14:
    ace_val = input("Would you like your player ace to be worth 1 or 11 points?  Please enter 1 or 11 ONLY")
    if ace_val == 1:
        value = 1
    elif ace_val == 11:
        value = 11
if player_start_cards1 and player_start_cards2 == 14:
    ace_value = input("Would you like your second player ace to be worth 1 or 11 points? Please enter 1 or 11 ONLY")
    if ace_value == 1:
        value += 1
    elif ace_value == 11:
        value += 11

# Resolving Dealer Ace Value(s)
if (dealer_start_cards1 or dealer_start_cards2) == 14:
    ace_val = input("Would you like your dealer ace to be worth 1 or 11 points?  Please enter 1 or 11 ONLY")
    if ace_val == 1:
        value = 1
    elif ace_val == 11:
        value = 11
if dealer_start_cards1 and dealer_start_cards2 == 14:
    ace_value = input("Would you like your second dealer ace to be worth 1 or 11 points? Please enter 1 or 11 ONLY")
    if ace_value == 1:
        value += 1
    elif ace_value == 11:
        value += 11

