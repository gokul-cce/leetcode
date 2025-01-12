class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        col0 = 1
        # row = [0] * m
        # col = [0] * n
        # def markrow(i):
        #     for j in range(n):
        #         if matrix[i][j] != 0:
        #             matrix[i][j] = float(-inf)
        
        # def markcol(j):
        #     for i in range(m):
        #         if matrix[i][j] != 0:
        #             matrix[i][j] = float(-inf)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # row[i] = 1
                    matrix[i][0] = 0
                    # col[j] = 1
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
                    

        for i in range(1,m):
            for j in range(1,n):
                # if row[i] or col[j]:
                #     matrix[i][j] = 0
                if matrix[i][j] != 0:
                    if (matrix[i][0] == 0) or (matrix[0][j] == 0):
                        matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(1,n):
                matrix[0][j] = 0

        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0

        return matrix
    


        