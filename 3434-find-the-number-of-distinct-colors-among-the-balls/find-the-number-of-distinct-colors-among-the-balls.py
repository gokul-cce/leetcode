from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        ball_color = {}
        color_freq = defaultdict(int)

        for k,v in queries:
            if k in ball_color: 
                prev = ball_color[k]
                color_freq[prev] -= 1
                if color_freq[prev] == 0:
                    del color_freq[prev]
            ball_color[k] = v
            color_freq[v] += 1
            res.append(len(color_freq))
        return res
    