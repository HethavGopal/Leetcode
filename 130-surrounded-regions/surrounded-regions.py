class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Find all edges:
        safe = set() # tuple of value

    
        
        def dfs_mark(r,c):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] == "X" or (r,c) in safe:
                return 

            safe.add((r,c))

            
            dfs_mark(r, c - 1)
            dfs_mark(r, c + 1)
            dfs_mark(r - 1,c)
            dfs_mark(r + 1, c)
    

            return
        

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and (c == 0 or c == len(board[0]) - 1 or r == 0 or r == len(board) - 1):
                    dfs_mark(r,c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r,c) not in safe and board[r][c] == "O":
                    board[r][c] = "X"
        
        return


    
            
                




        