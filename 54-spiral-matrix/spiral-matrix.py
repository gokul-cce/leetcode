class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row = len(matrix)
        col = len(matrix[0])
        left,right = 0,col-1
        top,buttom = 0,row-1

        while left <= right and top <= buttom:
            
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top,buttom+1):
                res.append(matrix[i][right])
            right -=1

            if top <= buttom:
                for j in range(right,left-1,-1):
                    res.append(matrix[buttom][j])
                buttom -= 1
            
            if left <= right:
                for j in range(buttom,top-1,-1):
                    res.append(matrix[j][left])
                left += 1

        return res
