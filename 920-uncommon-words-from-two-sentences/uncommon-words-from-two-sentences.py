class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        dic1 = {}
        
        for i in s1:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1
        for j in s2:
            if j in dic1:
                dic1[j] += 1
            else:
                dic1[j] = 1
        res = []
        print(dic1)
        for k,v in dic1.items():
            if v == 1:
                res.append(k)
        


        return res
        