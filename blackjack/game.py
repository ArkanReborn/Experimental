import player_cards as player
import dealer_cards as dealer

cards = player.cards
hand1 = player.hand1
hand2 = player.hand2
card_face1 = player.card_type1
card_face2 = player.card_type2

print(player)
print(dealer)

if cards in hand1:
    card = cards
    print(card, card[card_face1])
if cards in hand2:
    card = cards
    print(card, card[card_face2])