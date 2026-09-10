import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        res = []
        for point in points:
            euc_distance = - (math.sqrt(((point[0]) * (point[0])) + ((point[1]) * (point[1]))))
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, [euc_distance, point])
            else:
                print(f"euc_distance is {euc_distance} and maxHeap[0][0] is {maxHeap[0][0]}")
                if euc_distance > maxHeap[0][0]:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, [euc_distance, point])
        print(maxHeap)
        while maxHeap:
            dis, point = heapq.heappop(maxHeap)
            res.append(point)
        return res