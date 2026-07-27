class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        longest = 0
        left = 0
        maxf = 0
        for right in range(len(s)):
            # add right character to window map
            window[s[right]] = 1 + window.get(s[right], 0)
            # gets freq of highest frequency character in window
            maxf = max(maxf, window[s[right]])

            # while window - highest freq character > k
            # = while (numbers that can't be replaced) > k, we shift window
            while (right - left + 1) - maxf > k:
                window[s[left]] -= 1
                left += 1
            
            longest = max(right-left+1, longest)
            
        return longest
                