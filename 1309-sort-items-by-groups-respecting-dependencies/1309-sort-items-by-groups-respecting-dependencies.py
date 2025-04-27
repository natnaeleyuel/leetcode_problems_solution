class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def tpSort(nodes, pred, succ):
            order = []
            queue = deque(node for node in nodes if not pred[node])
            while queue:
                node = queue.popleft()
                order.append(node)
                for sc in succ[node]:
                    pred[sc].discard(node)
                    if not pred[sc]:
                        queue.append(sc)
            return order if len(order) == len(nodes) else []
        
        new_group = m
        group_item = defaultdict(set)
        for item in range(n):
            if group[item] == -1:
                group[item] = new_group
                new_group += 1
            group_item[group[item]].add(item)
        
        intra_pred = defaultdict(set)
        intra_succ = defaultdict(set)
        inter_pred = defaultdict(set)
        inter_succ = defaultdict(set)

        for item in range(n):
            for before in beforeItems[item]:
                if group[item] == group[before]:
                    intra_pred[item].add(before)
                    intra_succ[before].add(item)
                else:
                    inter_pred[group[item]].add(group[before])
                    inter_succ[group[before]].add(group[item])

        group_order = tpSort(list(group_item.keys()), inter_pred, inter_succ)
        if not group_order:
            return []

        result = []
        for group in group_order:
            order = tpSort(group_item[group], intra_pred, intra_succ)
            if not order:
                return []
            result.extend(order)
        
        return result
        


        

