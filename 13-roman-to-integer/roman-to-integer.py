class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        tot_sum = 0
        n = len(s)
        
        for i in range(n):
            if i < n-1 and dic[s[i]] < dic[s[i+1]]:
                tot_sum -= dic[s[i]]
            else:
                tot_sum += dic[s[i]]
        
        return tot_sum



        