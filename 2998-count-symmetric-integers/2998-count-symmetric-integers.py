class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def compute():
            first_half = sum(arr[:len(arr) // 2])
            second_half = sum(arr[len(arr) // 2:])
            return first_half, second_half   

        result = 0
        for i in range(low, high + 1):
            k = len(str(i)) 
            if k % 2 != 0:
                continue
            else:
                arr = list(map(int, str(i)))  
                fh, sh = compute()
                if fh == sh:
                    result += 1
        
        return result
