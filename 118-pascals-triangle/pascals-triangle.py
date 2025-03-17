class Solution:
    def generaterow(self,row):
        temp = [1]
        res = 1
        for col in range(1,row):
            res = (res * (row-col)) // col
            temp.append(res)
        return temp

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1,numRows+1):
            ans.append(self.generaterow(i))
        return ans
        