class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        edges = sorted(edges, key= lambda item: min(item[0], item[1]))
        countdict = defaultdict(int)
        countdict2 = defaultdict(set)
        set_nums = set()
        for l, r in edges:
            min_num = min(l, r)
            max_num = max(l, r)
            k = 0
            k2 = 0
            exist = False
            while k <= min_num and not exist:
                if k in countdict2 and min_num in countdict2[k]:
                    exist = True
                    countdict2[k].add(max_num)
                elif k in countdict2 and max_num in countdict2[k]:
                    exist = True
                    countdict2[k].add(min_num)
                k += 1

            if not exist:
                countdict2[min_num].add(min_num)
                countdict2[min_num].add(max_num)
            
            if min_num not in set_nums:
                set_nums.add(min_num)
            if max_num not in set_nums:
                set_nums.add(max_num)
            countdict[min_num] += 1
            countdict[max_num] += 1
        
        set_nums2 = set(range(n))
        result = len(set_nums2.difference(set_nums))
        occur = set()
        for nums, numset in countdict2.items():
            cond = True
            numlist = list(numset)
            for i in range(len(numlist)):
                curr = numlist[i]
                if countdict[curr] != len(numlist) - 1 or nums not in numset or curr in occur:
                    cond = False
                occur.add(curr)
            if cond:
                result += 1
        return result

            
