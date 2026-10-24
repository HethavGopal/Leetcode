from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        
        fresh = 0
        queue = deque()
        minute = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        
        while queue:
            if fresh == 0:
                return minute
            for _ in range(len(queue)):
                r,c = queue.popleft()
                
                neig = [[r, c - 1],[r, c + 1], [r-1, c], [r + 1, c] ]
                for dr, dc in neig:
                    if (min(dr,dc) < 0 or dr >= len(grid) or dc >= len(grid[0]) or grid[dr][dc] != 1):
                        continue 
                    
                    queue.append((dr,dc))
                    fresh -= 1
                    grid[dr][dc] = 2
            
            minute += 1


        if fresh != 0:
            return - 1
        else:
            return minute

                
                



                    