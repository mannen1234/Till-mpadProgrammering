class Card: 
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        if self.suit in ["♥️", "♦️"]:
            return f"\033[91m{self.value} {self.suit}\033[0m"
        else:
            return f"{self.value} {self.suit}"

class Deck:
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.cards = cards

    def draw_card(self):
        return self.cards["Ess", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    @staticmethod
    def create_deck():
        suits = ["♠️", "♥️", "♣️", "♦️"]
        values = ["Ess", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        cards = []

        for suit in suits:
            for value in values:
                cards.append(Card(suit, value))

        return cards

deck = Deck(Deck.create_deck())
for card in deck.cards:
    print(card)
