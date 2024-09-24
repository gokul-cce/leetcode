class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        st = ''
        first = strs[0]
        length = len(first)
        for i in range(length):
            for j in strs:
                if j[i] != first[i]:
                    length = i
                    break  
            if length != len(first):
                break
            
            st += first[i]
        return st


        