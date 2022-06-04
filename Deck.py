
import random

SUIT = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
DECK = 8 * SUIT
assert len(DECK) == 104

SEED = 'This is my random seed for testing.'

pic = {10: 'T', 11: 'J', 12: 'Q', 13: 'K', 1: 'A'}


class Deck:
    def __init__(self, repeatable=False) -> None:
        self.deck = DECK
        self.deck_size = len(self.deck)
        self.next = 0
        if repeatable:
            random.seed(SEED)

    def shuffle(self) -> None:
        "Shuffle the deck."
        random.shuffle(self.deck)
        self.next = 0
        # print("shuffle...")

    def deal(self, count) -> list[int]:
        "Return the next card from the shoe."
        assert self.next + count <= self.deck_size
        cards = self.deck[self.next: self.next + count]
        self.next += count
        return cards

    def remaining(self) -> int:
        "Return the number of cards still in the shoe."
        return self.deck_size - self.next


def display(c: int) -> str:
    if c > 1 and c < 10:
        return str(c)
    else:
        return pic[c]


if __name__ == '__main__':
    deck = Deck(repeatable=True)
    deck.shuffle()
    for i in range(10):
        show = [display(c) for c in deck.deal(10)]
        print(show)
    print('remaining:', deck.remaining())

    print(deck.deal(4))
    print('remaining:', deck.remaining())

    try:
        deck.deal(1)
    except AssertionError:
        print('deck is empty')
