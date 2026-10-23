from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        visited = set() 
        queue = deque()
        fresh = 0
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
            for i in range(len(queue)):
                r,c = queue.popleft()
                
                neighbors = [[0,1], [0,-1], [1,0],[-1,0]]
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0) or r + dr >= len(grid) or c + dc >= len(grid[0]) or (r + dr,c + dc) in visited or grid[r + dr][c + dc] != 1:
                        continue 
                    
                    if grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        fresh -= 1
                        queue.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
            minute += 1

        if fresh == 0:
            return minute
        else:
            return -1



                    

            