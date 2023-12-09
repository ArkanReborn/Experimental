import random


def game(cards, hand, card_type=0, card_num=0):
    card_face = ""

    for card in cards:
        hand = hand.replace(card, cards[card])

    if card_type == 0 or card_type > 4:
        raise ValueError(f"Error Invalid Card Type!")
    elif card_type == 1:
        card_face = "Hearts"
    elif card_type == 2:
        card_face = "Spades"
    elif card_type == 3:
        card_face = "Diamonds"
    elif card_type == 4:
        card_face = "Clubs"

    print(f"Dealer Card: {hand} of {card_face}")
    return


cards = {
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "10",
    "11": "King",
    "12": "Queen",
    "13": "Jack",
    "14": "Ace",
}

card_type1 = random.randint(1, 4)
start_cards1 = random.randint(2, 14)
hand1 = str(start_cards1)

card_type2 = random.randint(1, 4)
start_cards2 = random.randint(2, 14)
hand2 = str(start_cards2)

game1 = game(cards, hand1, card_type1, 1)
game2 = game(cards, hand2, card_type2, 2)
