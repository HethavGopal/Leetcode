class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        visited = set()
        
        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if r > len(board) - 1 or r < 0 or c > len(board[0]) - 1 or c < 0:
                return False

            if (r,c) in visited:
                return False

            visited.add((r,c))

            if word[i] == board[r][c]:
                found = ( dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1) or dfs(r + 1, c, i + 1) or dfs( r - 1, c, i + 1) )
                visited.remove((r,c))
                return found
            else:
                visited.remove((r,c))
                return False


            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        
        return False
            
            





            

        