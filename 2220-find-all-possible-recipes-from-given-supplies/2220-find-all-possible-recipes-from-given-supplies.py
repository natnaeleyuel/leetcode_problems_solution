class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        size = -1  
        que = deque(range(len(recipes)))
        avlb = set(supplies)
        result = []
        while len(avlb) > size:
            size = len(avlb)
            quesize = len(que)
            while quesize > 0:
                quesize -= 1
                ind = que.popleft()
                if all(ingredient in avlb for ingredient in ingredients[ind]):
                    avlb.add(recipes[ind])
                    result.append(recipes[ind])
                else:
                    que.append(ind)
        return result