class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        count_dict = defaultdict(list)
        for num, count in counter.items():
            count_dict[count].append(num)

        count_bucket = [0] * max(count_dict.keys())
        for count, ls in count_dict.items():
            count_bucket[count-1] = 1
        
        result = []
        k2 = k
        for i in range(len(count_bucket) - 1, - 1, - 1):
            if k2 > 0 and count_bucket[i] > 0:
                result.extend(count_dict[i+1])
                k2 -= len(count_dict[i+1])
        
        return result
