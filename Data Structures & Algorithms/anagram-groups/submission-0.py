class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict()
        # grouping anagrams together using if sorted version of word is equal
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in m:
                m[sorted_s].extend([s])
            else:
                m[sorted_s] = [s]
        
        return list(m.values())