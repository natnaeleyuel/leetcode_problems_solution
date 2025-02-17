class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def tile_func(count: Counter) -> int:
            result = 0
            for i, x in count.items():
                if x > 0:
                    result += 1
                    count[i] -= 1
                    result += tile_func(count)
                    count[i] += 1
            return result

        count = Counter(tiles)
        return tile_func(count)