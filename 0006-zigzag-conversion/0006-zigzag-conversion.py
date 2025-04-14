class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        ind = 0
        opr_dict = defaultdict(list)
        while ind < n:
            for i in range(1, numRows + 1):
                if ind < n:
                    opr_dict[i].append(s[ind])
                    ind += 1
                else:
                    break

            if ind < n:
                for j in range(numRows-1, 1, -1):
                    if ind < n:
                        opr_dict[j].append(s[ind])
                        ind += 1
                    else:
                        break
            
        result = [''.join(opr_dict[row]) for row in range(1, numRows + 1)]
        return ''.join(result)
