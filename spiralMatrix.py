class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # print(len(matrix),len(matrix[0]))
        res = []
        rl= 0
        cl= 0
        m = len(matrix)
        n = len(matrix[0])
        # print  "a",m,n
        while rl<m and cl<n:
            i=cl
            print "b",m,n
            if rl<n-1:
                for i in range(n-1):
                    print matrix[rl][i] , "top"
                    res.append(matrix[rl][i])
                rl+= 1
            i=rl
            print "c",m,n, rl,cl
            if cl<m-1:
                for i in range(m):
                    print matrix[i][n-1], "rht"
                    res.append(matrix[i][n-1])
                n -=1
            # print "d",m,n
            
            if(rl<m):
                # print ("jhg",n-1,cl)
                for i in range(n-1,cl,-1):
                    # print "jhgsss",m-1,i
                    print matrix[m-1][i],"down"
                    res.append(matrix[m-1][i])
                m-=1
                
            if(cl<n):
                # print ("qqq",m,rl-1)
                for i in range(m,rl-1,-1):
                    # print "jhgsss",n-1,i
                    print matrix[i][cl],"lf"
                    res.append(matrix[i][cl])
                cl+=1
            print rl,cl, "--",m,n
        return res
    
            
