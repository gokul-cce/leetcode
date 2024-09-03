class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1,num+1):
            total = 0
            for j in str(i):
                total += int(j)
                # print(total ,end = "")
            if total % 2 == 0:
                count += 1
        return count
        