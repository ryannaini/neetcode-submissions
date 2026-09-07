class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]

        heapq.heapify(maxHeap)
        count = 0 
        while len(maxHeap) > 1:

            bigger = - heapq.heappop(maxHeap)
            big = - heapq.heappop(maxHeap)

            if bigger > big:
                heapq.heappush(maxHeap, -(bigger - big))

        return (- maxHeap[0]) if len(maxHeap) == 1 else 0