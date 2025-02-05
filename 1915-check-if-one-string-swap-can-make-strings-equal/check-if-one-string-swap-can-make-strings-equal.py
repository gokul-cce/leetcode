class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        difference = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                difference.append(i)
                if len(difference)>2:
                    return False
        
        if len(difference) == 2 and s1[difference[0]] == s2[difference[1]] and s1[difference[1]] == s2[difference[0]]:
            return True
        return False

