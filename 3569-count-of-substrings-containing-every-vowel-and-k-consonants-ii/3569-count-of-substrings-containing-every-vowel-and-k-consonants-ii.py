class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def f(k: int) -> int:
            counter = Counter()
            ans = l = x = 0
            for c in word:
                if c in "aeiou":
                    counter[c] += 1
                else:
                    x += 1
                while x >= k and len(counter) == 5:
                    d = word[l]
                    if d in "aeiou":
                        counter[d] -= 1
                        if counter[d] == 0:
                            counter.pop(d)
                    else:
                        x -= 1
                    l += 1
                ans += l
            return ans

        return f(k) - f(k + 1)
