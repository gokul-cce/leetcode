class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dic = {}
        for i in words1:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for j in words2:
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
        count = 0
        for k,v in dic.items():
            if v == 2 and k in words1 and k in words2:
                count += 1

        return count
        