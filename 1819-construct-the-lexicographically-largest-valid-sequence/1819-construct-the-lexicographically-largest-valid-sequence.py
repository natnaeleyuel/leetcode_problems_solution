class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def dis_seq(pos):
            if pos == n * 2:
                return True
            if seq[pos]:
                return dis_seq(pos + 1)

            for num in range(n, 1, -1):
                if new_arr[num] and pos + num < n * 2 and seq[pos + num] == 0:
                    new_arr[num] = 0
                    seq[pos] = seq[pos + num] = num
                    if dis_seq(pos + 1):
                        return True
                    seq[pos] = seq[pos + num] = 0
                    new_arr[num] = 2

            if new_arr[1]:
                new_arr[1], seq[pos] = 0, 1
                if dis_seq(pos + 1):
                    return True
                seq[pos], new_arr[1] = 0, 1

            return False

        seq = [0] * (n * 2)
        new_arr = [2] * (n * 2)
        new_arr[1] = 1
        dis_seq(1)

        return seq[1:]




