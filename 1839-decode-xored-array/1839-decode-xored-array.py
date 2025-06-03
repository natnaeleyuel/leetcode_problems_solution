class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        temp = first
        for i in range(len(encoded)):
            result.append(encoded[i] ^ temp)
            temp = encoded[i] ^ temp
        
        return result

