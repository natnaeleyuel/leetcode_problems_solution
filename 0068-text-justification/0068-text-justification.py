class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        d = defaultdict(list)
        count = 1
        curr = len(words[0])
        d[count].append([[words[0]], curr])
        ind = 1
        while ind < n:
            curr_len = len(words[ind])
            l = d[count]
            if l[0][1] + 1 + curr_len <= maxWidth:
                l[0][1] += 1 + curr_len
                l[0][0].append(words[ind])
            else:
                count += 1
                d[count].append([[words[ind]], curr_len])

            ind += 1
        result = []

        for count, info in d.items():
            info = info[0]
            row = info[0]
            lw = len(row)
            group = [row[0]]
            if count == len(d) and lw != 1:
                fs = maxWidth - info[1] + lw - 1
                for i in range(1, lw):
                    fs -= 1
                    group.append(' ')
                    group.append(row[i])
                group.append(' ' * fs)

            elif lw != 1:
                ind = 1
                fs = maxWidth - info[1] + lw - 1
                space = ceil(fs / (lw - 1))
                while ind < lw and fs > 0:
                    space = ceil(fs / (lw - ind))
                    if fs >= space:
                        fs -= space
                        group.extend([' ' * space, row[ind]]) 

                    ind += 1
                
                if ind < lw and group[-1]:
                    group.extend([' ', row[ind]])

            if lw == 1:
                fs = maxWidth - info[1] + lw - 1
                group.append(' ' * fs)
            
            result.append(''.join(group))
        
        return result


            
