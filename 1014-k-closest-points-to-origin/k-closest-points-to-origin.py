import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_heap = []
        res = []

        for point in points:
            distance = (point[0]) ** 2 + point[1] ** 2
            point_heap.append([distance,point])
        
        heapq.heapify(point_heap)

        for _ in range(k):
            point = heapq.heappop(point_heap)[1]
            res.append(point)

        return res

