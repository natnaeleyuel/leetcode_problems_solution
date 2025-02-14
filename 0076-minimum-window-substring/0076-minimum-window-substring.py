class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        required = len(dict_t)

        window_dict = defaultdict(int)
        aquired = 0

        left = 0
        n = len(s)
        solution = (n+1, None, None)
        for right in range(n):
            cur_char = s[right]
            window_dict[cur_char] += 1
            if cur_char in dict_t:
                if dict_t[cur_char] == window_dict[cur_char]:
                    aquired += 1

            while aquired == required:
                left_char = s[left]
                if solution[0] > right - left + 1:
                    solution = (right - left + 1, left, right)
                
                window_dict[left_char] -= 1

                if left_char in dict_t:
                    if window_dict[left_char] < dict_t[left_char]:
                        aquired -= 1
                
                left += 1

        if solution[0] == n + 1:
            return ""
        else: 
            return s[solution[1]: solution[2]+1]
