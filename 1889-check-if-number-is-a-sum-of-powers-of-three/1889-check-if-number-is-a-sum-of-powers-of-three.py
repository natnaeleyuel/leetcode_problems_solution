from math import pow
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def powerThree(n, base):
            result = 3 ** base
            if result < n:
                base += 1
                return powerThree(n, base)
            elif result == n:
                return base
            else:
                return base - 1

        def makePowerOfThree(n):
            arr = []
            k = powerThree(n, 0)
            for i in range(k+1 - 1, - 1, - 1):    
                arr.append(3**i)
            return arr
    
        arr = makePowerOfThree(n)

        result = 0
        newArr = []
        for i in range(len(arr)):
            result += arr[i]
            if result <= n:
                newArr.append(arr[i])
            else:
                result -= arr[i]
        
        return sum(newArr) == n

