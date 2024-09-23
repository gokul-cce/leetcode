class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif not stack or stack.pop() != dic[i]:
                return False
                
        if stack:
            return False
        return True
        