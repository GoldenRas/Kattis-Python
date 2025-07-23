a = input()
suits = {'P': 13, 'K': 13, 'H': 13, 'T': 13}
seen_cards = set()

for i in range(0, len(a), 3):
    card = a[i:i+3]
    if card in seen_cards:
        print("GRESKA")
        break
    seen_cards.add(card)
    suits[card[0]] -= 1
else:
    print(suits['P'], suits['K'], suits['H'], suits['T'])
