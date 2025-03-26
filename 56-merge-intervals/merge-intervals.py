class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for i in range(1,len(intervals)):
            temp = intervals[i]
            if temp[0] <= result[-1][-1]:
                result[-1][-1] = max(temp[1],result[-1][-1])
            else:
                result.append(temp)
        return result

        