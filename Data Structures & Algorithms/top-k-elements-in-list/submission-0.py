class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        res = []
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
        
        for j in range(k):
            highest_freq = max(map.values())
            k = 0
            for k, val in map.items():
                if val == highest_freq:
                    res.append(k)
                    k = k
                    break
            map.pop(k)
        
        return res