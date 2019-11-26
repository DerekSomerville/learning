import playingCard, unittest

numberOfCards = 52

class playingCardTests(unittest.TestCase):

    def test_numberOfCardsInDeck(self):
        deck = playingCard.generateDeck()
        self.assertEqual(len(deck),numberOfCards)

    def test_numberOfCardsInShuffledDeck(self):
        deck = playingCard.generateDeck()
        deck = playingCard.shuffleCards(deck)
        self.assertEqual(len(deck), numberOfCards)

    def notListEqual(self, firstList, secondList):
        equalCount = 0
        counter = 0
        result = False
        for counter in range(len(firstList)):
            if firstList[counter] == secondList[counter]:
                equalCount += 1
            counter += 1
        if equalCount < len(firstList):
            result = True
        return result

    def test_suffledDeck(self):
        deck = playingCard.generateDeck()
        firstCards = deck[0:5]
        deck = playingCard.shuffleCards(deck)
        self.assertTrue(self.notListEqual(firstCards,deck[0:5]))

    def test_dealLastCard(self):
        card = playingCard.dealACard(["SA","S7",'CK'])
        self.assertEqual(card,"CK")

    def test_dealCards(self):
        deck = playingCard.generateDeck()
        hands = playingCard.dealCards(deck,2,3)
        self.assertEqual(len(hands),3)
        self.assertEqual(len(hands[0]),2)
        self.assertEqual(len(hands[-1]), 2)

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()