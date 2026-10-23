class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        visited = set()
          

        def dfs(r,c):
            if (r,c) in visited or r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))

            count = 1

            count += dfs(r, c -1) 
            count += dfs(r, c + 1)
            count += dfs(r - 1, c)
            count += dfs(r + 1, c)

            return count
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area, dfs(r,c))
        
        return max_area
      

        
            


        

        