class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == 'I' and (i != len(s)-1) and (s[i+1] == 'V' or s[i+1] == 'X'):
                total = total - dic[s[i+1]] + (dic[s[i+1]]-1)
                # print(total)
                continue
            elif s[i] == 'X' and (i != len(s)-1) and (s[i+1] == 'L' or s[i+1] == 'C'):
                total = total - dic[s[i+1]] + (dic[s[i+1]]-10)
                # print(total)
                continue
            elif s[i] == 'C' and (i != len(s)-1) and (s[i+1] == 'D' or s[i+1] == 'M'):
                total = total - dic[s[i+1]] + (dic[s[i+1]]-100)
                # print(total)
                continue
            
            total += dic[s[i]]
            # print(total)
            

        return total



        