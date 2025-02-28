class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        st = ''
        result = 0
        while right < len(s):
            if s[right] not in st:
                st += s[right]
                right += 1
            else:
                result = max(result,right-left)
                left += 1 
                right = left
                st = ''
        result = max(result,right-left)
        return result

