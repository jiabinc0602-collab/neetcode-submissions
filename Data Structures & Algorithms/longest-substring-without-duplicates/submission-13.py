class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        sub = []
        for j in range(len(s)):
            if s[j] in sub:
                # if there is a duplicate character
                while s[j] in sub:
                    # loop to iterate until substring has no duplicate character
                    sub = sub[1:]
            sub.append(s[j])
            
            longest = max(len(sub), longest)
        return longest

            
            