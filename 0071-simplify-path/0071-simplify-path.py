class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        result = []
        for i in range(len(arr)):
            curr = arr[i]
            if curr != '' and curr != '..' and curr != '.':
                result.append(curr)
            elif result and curr == '..':
                result.pop()
            
        return '/' + '/'.join(result)
             