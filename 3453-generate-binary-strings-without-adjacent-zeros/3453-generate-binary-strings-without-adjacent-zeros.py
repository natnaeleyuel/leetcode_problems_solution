class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = ["0","1"]
        for i in range(n-1):
            curr = []
            for bin_str in result:
                if bin_str[-1] == '0':
                    curr.append(bin_str + '1')
                else:
                    curr.append(bin_str + '0')
                    curr.append(bin_str + '1')
            result = curr

        return result