class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        for right in range(n):
            curr = s[right]
            if curr != ']':
                stack.append(curr)
            else:
                temp = ''
                while stack and stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(temp * int(num))
        return ''.join(stack)