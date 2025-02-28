class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        dic = {}
        result = 0
        while right < len(s):
            if s[right] in dic and dic[s[right]]>=left:
                left = dic[s[right]] + 1
            
            dic[s[right]] = right
            right += 1
            result = max(result,right-left)
        return result

