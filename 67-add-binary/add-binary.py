class Solution:
    def addBinary(self, a: str, b: str) -> str:
        st1 = len(a) - 1
        st2 = len(b) - 1
        st = ''
        div = 0
        while st1 >= 0 or st2 >= 0:
            total = 0
            if div:
                total += div
                div = 0
            if st1 >= 0:
                total += int(a[st1])
            if st2 >= 0:
                total += int(b[st2])
            
            if total <= 1:
                st = str(total) + st
            if total > 1:
                total = str(bin(total)[2:])
                div = int(total[-2])
                st = total[-1] + st
            
            st1 -= 1
            st2 -= 1

        if div:
            st = str(div) + st
        return st


            

        