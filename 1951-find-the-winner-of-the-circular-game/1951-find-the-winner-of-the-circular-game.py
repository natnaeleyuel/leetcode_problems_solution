class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n+1)]
        curr = 0
        while len(players) > 1:
            next = (curr + k - 1) % len(players)
            players.pop(next)
            curr = next
        return players[0]