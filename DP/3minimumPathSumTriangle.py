'''
Question: In a given triangle, find the minimum sum to reach from top to last row.
current element can access the next row elements either direct below or next element 
      i.e suppose (i,j), can access the elements in indices ((i+1,j), (i+1,j+1)) 

Logic: In a top-down approach, while iterating the triangle, add the min value in indices((i-1,j-1), (i-1,j)) to the current element
      Finally return min value in the last row

Implementation:  
 triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])  
    --> 2 loops, iterate through rows(i) and columns(j)
        -->handle 3 cases and modify the same triangle.
            --> if the element is in extreme left then simply add the above element triangle[i-1][j]
            --> if the element is in extreme right then simply add the eleement triangle[i-1][j-1]
            -->else check two (min(triangle[i-1][j-1],triangle[i-1][j]))
        -->return minimum value in last row of triangle

code:
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
            
        for i in range(2,n):
            for j in range(i+1):
                if j == 0:
                   triangle[i][j] += triangle[i-1][j]
                elif j == i:
                   triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])  
        return min(triangle[n-1])+triangle[0][0]
