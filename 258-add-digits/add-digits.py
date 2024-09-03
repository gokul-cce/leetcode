class Solution:
    def addDigits(self, num: int) -> int:
        st = str(num)
        if num > 9:
            count = 0
            for i in st:
                count += int(i)
            return self.addDigits(count)
        
        else:
            return num
        