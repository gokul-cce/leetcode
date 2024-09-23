class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack.pop() != dic[i]:
                    return False
        if stack:
            return False
        return True
        