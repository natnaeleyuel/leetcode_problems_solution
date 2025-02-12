class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) % 2 == 0:
            skill.sort()
            half = len(skill) // 2
            div = sum(skill) // half
            result = 0
            left = 0
            right = len(skill) - 1
            while left <= right:
                if skill[left] + skill[right] == div:
                    result += skill[left] * skill[right]
                else:
                    return -1
                
                left += 1
                right -= 1
            return result

