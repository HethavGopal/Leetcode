from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        visited[node] = Node(node.val)

        queue = deque()
        queue.append(node)

        while queue:
            curr_node = queue.popleft()

            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                visited[curr_node].neighbors.append(visited[neighbor])

        return visited[node]