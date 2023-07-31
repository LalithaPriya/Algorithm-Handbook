'''
Question: In a given matrix (n x n size), find the minimum sum to reach from first row to last row.
current element can access the next row elements either direct below or diagonally left or right 
      i.e suppose (i,j), can access the elements in indices ((i+1,j-1), (i+1,j), (i+1,j+1)) 
In Constraints its mentioned, size of square matrix is greater than 1.

Logic: In a top-down approach, while iterating the matrix, add the min value in indices((i-1,j-1), (i-1,j), (i-1,j+1)) to the current element
      Finally return min value in the last row

Implementation:  
 matrix[i][j] += min(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])  
    --> 2 loops, iterate through rows(i) and columns(j)
        -->handle 3 cases and modify the same matrix.
            --> if the element is in extreme left then handle j-1 case in the above equation
            --> if the element is in extreme left then handle j+1 case in the above equation
            -->else check all three
        -->return minimum value in last row of marix

code:
'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
       
        n = len(matrix)

        for i in range(1,n):
            for j in range(n):
                if j == 0:
                   matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j+1])
                elif j == n-1:
                   matrix[i][j] += min(matrix[i-1][j-1],matrix[i-1][j])
                else:
                    matrix[i][j] += min(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])  
        return min(matrix[n-1])
