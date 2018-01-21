class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        col_limit = 0
        
        #transpose
        
        #foreach line
        for l in range(1, n):
            col_limit = col_limit + 1
            #foreach cel in the line
            for c in range(0, col_limit):
                matrix[l][c], matrix[c][l] = matrix[c][l], matrix[l][c]                    
            
        #reverse the lines
        for l in range(0, n):
            i, j = 0, n - 1
            line = matrix[l]
            while i < j:                
                line[i], line[j] = line[j], line[i]
                i, j = i + 1, j - 1