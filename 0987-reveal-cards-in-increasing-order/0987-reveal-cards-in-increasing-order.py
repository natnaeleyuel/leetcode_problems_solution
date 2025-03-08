class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result = []
        deck.sort()
        deck.reverse()
        for i in range(len(deck)):
            curr = deck[i]
            result = [curr] + result[-1:] + result[:-1]
        return result
        