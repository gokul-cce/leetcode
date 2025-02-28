class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        dic = {}
        result = 0
        while right < len(s):
            while s[right] in dic:
                del dic[s[left]]
                left += 1
            
            dic[s[right]] = right
            right += 1
            result = max(result,len(dic))
        return result

