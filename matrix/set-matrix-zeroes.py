class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Initialize flags to mark rows and columns that need to be zeroed out
        zero_rows = set()
        zero_cols = set()
        
        # Iterate through the matrix to mark zero rows and columns
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        # Set elements in zero rows and columns to zero
        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
