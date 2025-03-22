class Solution:
    def validStrings(self, n: int) -> List[str]:
        output = ["0","1"]
        for i in range(n-1):
            tmp = []
            for bin_str in output:
                if bin_str[-1] == '0':
                    tmp.append(bin_str+'1')
                else:
                    tmp.append(bin_str+'0')
                    tmp.append(bin_str+'1')
            output = tmp

        return output