class Solution:
    def maxRepOpt1(self, text: str) -> int:
        d = {}
        for c in text:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        # RLE : aaabaaa ----> [(a, 3), (b, 1), (a, 3)]
        g, c = [], text[0]
        tmp = 1
        for char in text[1:]:
            if char == c:
                tmp += 1
            else:
                g.append((c, tmp))
                tmp = 1
                c = char
        g.append((c, tmp))

        # case 1 : extend by one
        ans = max(min(i + 1, d[char]) for char, i in g)
        
        # merging the groups
        for i in range(1, len(g) - 1):
            # if both sides have the same char and are separated by only 1 char
            if g[i - 1][0] == g[i + 1][0] and g[i][1] == 1:
                ans = max(ans, min(g[i - 1][1] + g[i + 1][1] + 1, d[g[i + 1][0]]))
        return ans