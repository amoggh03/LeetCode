class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        mem={}
        count=0
        for i in range( len(board)):
            for j in range(len(board[0])):
                count = 0  # Reset count for each cell
                # Check top
                if i > 0 and board[i-1][j] == 1:
                    count += 1
                # Check bottom
                if i < len(board)-1 and board[i+1][j] == 1:
                    count += 1
                # Check left
                if j > 0 and board[i][j-1] == 1:
                    count += 1
                # Check right
                if j < len(board[0])-1 and board[i][j+1] == 1:
                    count += 1
                # Check top-left diagonal
                if i > 0 and j > 0 and board[i-1][j-1] == 1:
                    count += 1
                # Check top-right diagonal
                if i > 0 and j < len(board[0])-1 and board[i-1][j+1] == 1:
                    count += 1
                # Check bottom-left diagonal
                if i < len(board)-1 and j > 0 and board[i+1][j-1] == 1:
                    count += 1
                # Check bottom-right diagonal
                if i < len(board)-1 and j < len(board[0])-1 and board[i+1][j+1] == 1:
                    count += 1
                mem[(i,j)]=count
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = mem[(i, j)]
                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = 0  # Apply underpopulation or overpopulation rule
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 1  # Apply reproduction rule
                        