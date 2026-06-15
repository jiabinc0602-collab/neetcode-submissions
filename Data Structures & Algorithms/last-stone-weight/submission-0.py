class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        maxh = [-n for n in stones]
        heapq.heapify(maxh)
    
        while len(maxh) > 1:
            y = heapq.heappop(maxh)
            x = heapq.heappop(maxh)
            if x != y:
                heapq.heappush(maxh, y - x)
        return -maxh[0] if maxh else 0