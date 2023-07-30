'''
Minimum path sum: 
Given a matrix (non- negative numbers), find the path with minimum cost to travel from top left corner to bottom right corner.
Directions : horizantal or vertical

Logic: In top-down approach, for every element in the matrix, consider minimum cost in top or left elements and add them to its value
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])

        for i in range(1,n):
            grid[i][0] += grid[i-1][0]
        for i in range(1,m):
            grid[0][i] += grid[0][i-1]
        for i in range(1,n):
            for j in range(1,m):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[n-1][m-1]
                        

