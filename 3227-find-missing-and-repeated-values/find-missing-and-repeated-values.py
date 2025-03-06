class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        lis = []
        dic = {}
        answer = [-1,-1]
        for i in grid:
            lis.extend(i)
        for i in range(1,len(lis)+1):
            if i not in lis:
                answer[1] = i
            if lis[i-1] in dic:
                answer[0] = lis[i-1]
            else:
                dic[lis[i-1]] = 1
        return answer

        