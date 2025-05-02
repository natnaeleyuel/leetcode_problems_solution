class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        force = [0] * n

        forc = 0
        for i in range(n):
            if dominoes[i] == 'R': 
                forc = n
            elif dominoes[i] == 'L': 
                forc = 0
            else: 
                forc = max(forc - 1, 0)
            force[i] += forc

        forc = 0
        for i in range(n - 1, - 1, - 1):
            if dominoes[i] == 'L': 
                forc = n
            elif dominoes[i] == 'R': 
                forc = 0
            else: 
                forc = max(forc - 1, 0)
            force[i] -= forc

        return "".join('.' if forc == 0 else 'R' if forc > 0 else 'L' for forc in force)