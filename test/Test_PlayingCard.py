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

    def test_suffledDeck(self):
        deck = playingCard.generateDeck()
        firstCards = deck[0:5]
        deck = playingCard.shuffleCards(deck)
        self.assertTrue(self.notListEqual(firstCards,deck[0:5]))

    def test_dealLastCard(self):
        card = playingCard.dealACard(["SA","S7",'CK'])
        self.assertEqual(card,"CK")

    def test_dealCardsThreePlayer(self):
        deck = playingCard.generateDeck()
        hands = playingCard.dealCards(deck,2,3)
        self.assertEqual(len(hands),3)

    def test_dealCardsFirstTwoCards(self):
        deck = playingCard.generateDeck()
        hands = playingCard.dealCards(deck,2,3)
        self.assertEqual(len(hands[0]),2)

    def test_dealCardsLastTwoCards(self):
        deck = playingCard.generateDeck()
        hands = playingCard.dealCards(deck,2,3)
        self.assertEqual(len(hands[-1]), 2)

    def test_dealCardsAllFourPlayersAllDealt(self):
        deck = playingCard.generateDeck()
        hands = playingCard.dealCards(deck,0,4)
        self.assertEqual(numberOfCards,self.countHands(hands))

    def test_dealCardsAllFivePlayersAllDealt(self):
        deck = playingCard.generateDeck()
        hands = playingCard.dealCards(deck,0,5)
        self.assertEqual(numberOfCards,self.countHands(hands))

    def test_dealCardsAllFivePlayersFirstHand(self):
        deck = playingCard.generateDeck()
        hands = playingCard.dealCards(deck,0,5)
        self.assertEqual(11,len(hands[0]))

    def test_dealCardsAllFivePlayersLastHand(self):
        deck = playingCard.generateDeck()
        hands = playingCard.dealCards(deck,0,5)
        self.assertEqual(10,len(hands[-1]))

    def test_dealCardsAllTwelvePlayersAllDealt(self):
        deck = playingCard.generateDeck()
        hands = playingCard.dealCards(deck,0,12)
        self.assertEqual(numberOfCards,self.countHands(hands))

    def test_SortHand(self):
        randomHand = ["C8", "HA", "C2"]
        playingCard.sortHand(randomHand)
        self.assertEqual(["C2", "C8", "HA"],randomHand)

    def countHands(self,hands):
        total = 0
        for hand in hands:
            total += len(hand)
        return total

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

if __name__ == "__main__":
    unittest.main()
