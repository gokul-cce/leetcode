class Solution:
    def addDigits(self, num: int) -> int:
        st = str(num)
        while num > 9:
            count = 0
            for i in st:
                count += int(i)
            st =  str(count)
            num = count
        
        return num
        