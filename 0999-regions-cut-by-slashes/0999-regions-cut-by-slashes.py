class DisjointUnion:
    def trig_ind(self, size, row, col, triangle_num):
        return (size * row + col) * 4 + triangle_num

    def union(self, root, x, y):
        rootx = self.find(root, x)
        rooty = self.find(root, y)
        if rootx != rooty:
            root[rootx] = rooty
            return 1  
        return 0  

    def find(self, root, x):
        if root[x] == -1:
            return x
        root[x] = self.find(root, root[x])
        return root[x]

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        size = len(grid)
        dsu = DisjointUnion()
        tot_trg = size * size * 4
        root = [-1] * tot_trg

        reg_count = tot_trg

        for row in range(size):
            for col in range(size):
                if row > 0:
                    reg_count -= dsu.union(
                        root,
                        dsu.trig_ind(size, row - 1, col, 2),
                        dsu.trig_ind(size, row, col, 0),
                    )
                if col > 0:
                    reg_count -= dsu.union(
                        root,
                        dsu.trig_ind(size, row, col - 1, 1),
                        dsu.trig_ind(size, row, col, 3),
                    )

                if grid[row][col] != "/":
                    reg_count -= dsu.union(
                        root,
                        dsu.trig_ind(size, row, col, 0),
                        dsu.trig_ind(size, row, col, 1),
                    )
                    reg_count -= dsu.union(
                        root,
                        dsu.trig_ind(size, row, col, 2),
                        dsu.trig_ind(size, row, col, 3),
                    )

                if grid[row][col] != "\\":
                    reg_count -= dsu.union(
                        root,
                        dsu.trig_ind(size, row, col, 0),
                        dsu.trig_ind(size, row, col, 3),
                    )
                    reg_count -= dsu.union(
                        root,
                        dsu.trig_ind(size, row, col, 2),
                        dsu.trig_ind(size, row, col, 1),
                    )

        return reg_count
