class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        def markrow(i):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float(-inf)
        
        def markcol(j):
            for i in range(m):
                if matrix[i][j] != 0:
                    matrix[i][j] = float(-inf)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    markrow(i)
                    markcol(j)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float(-inf):
                    matrix[i][j] = 0
        return matrix
    


        