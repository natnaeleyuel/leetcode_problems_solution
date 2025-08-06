class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = []
        smallest_leng = len(min(strs, key=len))
        for i in range(smallest_leng):
            curr_chr = strs[0][i]
            cond = True
            for j in range(len(strs)):
                if strs[j][i] != curr_chr:
                    cond = False
            if cond:
                common_prefix.append(curr_chr)
            else:
                break
        return "".join(common_prefix)