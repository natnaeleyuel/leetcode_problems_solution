class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0      
        mod_index_map = {0: -1} 

        for index, value in enumerate(nums):
            prefix_sum += value         
            modulus = prefix_sum % k
            if modulus in mod_index_map and index - mod_index_map[modulus] >= 2:
                return True
          
            if modulus not in mod_index_map:
                mod_index_map[modulus] = index
      
        return False
