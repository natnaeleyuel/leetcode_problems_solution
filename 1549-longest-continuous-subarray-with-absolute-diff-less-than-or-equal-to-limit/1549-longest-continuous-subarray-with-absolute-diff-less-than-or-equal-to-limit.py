class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        deque1 = deque()
        deque2 = deque()
        left = 0
        maxlength = 0
        for right in range(n):
            while deque1 and nums[deque1[-1]] >= nums[right]:
                deque1.pop()
            while deque2 and nums[deque2[-1]] <= nums[right]:
                deque2.pop()
            
            deque1.append(right)
            deque2.append(right)

            while nums[deque2[0]] - nums[deque1[0]] > limit:
                left += 1
                if deque1[0] < left:
                    deque1.popleft()
                if deque2[0] < left:
                    deque2.popleft()
            maxlength = max(maxlength, right - left + 1)
        return maxlength
