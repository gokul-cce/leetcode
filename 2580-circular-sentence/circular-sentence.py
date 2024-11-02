class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lis = sentence.split()
        print(lis)
        for i in range(len(lis)-1):
            st0 = lis[i]
            st1 = lis[i+1]
            if st0[-1] != st1[0]:
                return False
        st0 = lis[0]
        st1 = lis[-1]
        if st0[0] != st1[-1]:
            return False
        return True
        