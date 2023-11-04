import random

def player_game(cards, hand, card_type=0, card_num=0):
    card_face = ""
    player_list = []

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
    player_list.append(hand)
    return player_list

def dealer_game(cards, hand, card_type=0, card_num=0):
    card_face = ""
    dealer_list = []
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
    dealer_list.append(hand)
    return dealer_list

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

# Resolving Player Ace Value(s)

player_value = 0
player_counter = 0

player_list = player_game()

def player_ace_values(player_start_cards1, player_start_cards2, player_value=0, player_counter=0):
    if (player_start_cards1 or player_start_cards2) == 14:
        ace_val = input("Would you like your player ace to be worth 1 or 11 points?  Please enter 1 or 11 ONLY")
        if ace_val == 1:
            player_value = 1
            player_counter += 1
            if player_start_cards1 == 14:
                player_list.pop(0)
        elif ace_val == 11:
            player_value = 11
            player_counter += 1
    if player_start_cards1 and player_start_cards2 == 14:
        ace_value = input("Would you like your second player ace to be worth 1 or 11 points? Please enter 1 or 11 ONLY")
        if ace_value == 1:
            player_value += 1
            player_counter += 1
        elif ace_value == 11:
            player_value += 11
            player_counter += 1
        return player_value, player_counter

# Resolving Dealer Ace Value(s)
dealer_value = 0
dealer_counter = 0

def dealer_ace_values(dealer_start_cards1, dealer_start_cards2, dealer_value=0, dealer_counter=0):
    if (dealer_start_cards1 or dealer_start_cards2) == 14:
        ace_val = input("Would you like your dealer ace to be worth 1 or 11 points?  Please enter 1 or 11 ONLY")
        if ace_val == 1:
            dealer_value = 1
            dealer_counter += 1
        elif ace_val == 11:
            dealer_value = 11
            dealer_counter += 1
    if dealer_start_cards1 and dealer_start_cards2 == 14:
        ace_value = input("Would you like your second dealer ace to be worth 1 or 11 points? Please enter 1 or 11 ONLY")
        if ace_value == 1:
            dealer_value += 1
            dealer_counter += 1
        elif ace_value == 11:
            dealer_value += 11
            dealer_counter += 1
    return dealer_value, dealer_counter

player_total = 0
dealer_total = 0

def cal_diff(player_value, player_counter, dealer_value, dealer_counter, player_start_cards1, player_start_cards2, dealer_start_cards1, dealer_start_cards2):

    if player_counter == 0:
        player_total = player_start_cards1 + player_start_cards2
    elif player_counter == 1:
        player_total = player_value + 


    dealer_total = dealer_start_cards1 + dealer_start_cards2
    player_diff = 21 - player_total
    dealer_diff = 21 - dealer_total

    return player_diff, dealer_diff

print()