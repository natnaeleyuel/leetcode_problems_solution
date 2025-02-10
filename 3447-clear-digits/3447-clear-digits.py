class Solution:
    def clearDigits(self, s: str) -> str:
        listStr = list(s)
        i = 0
        while i < len(listStr): 

            if listStr[i].isnumeric():
                if i > 0 and listStr[i-1].isalpha():
                    del listStr[i]
                    del listStr[i-1]
                    i -= 1
                else:
                    del listStr[i]

                continue
            i += 1

        return ''.join(listStr)
