class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        currSum = (n*n)*((n*n) +1)//2
        # print(currSum)
        seen = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in seen:
                    seen.add(grid[i][j])
                    currSum -= grid[i][j]
                else:
                    dup = grid[i][j]
        return [dup, currSum]

        