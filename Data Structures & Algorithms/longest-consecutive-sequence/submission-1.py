class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0
        current_longest = 0
        stack = []

        for i in nums:
            if len(stack) == 0:
                stack.append(i)
                current_longest = 1

            elif stack[-1] == i:
                continue
            
            elif stack[-1] + 1 == i:
                stack.append(i)
                current_longest += 1
            
            else:
                stack.clear()
                stack.append(i)
                current_longest = 1
            
            if current_longest > longest:
                longest = current_longest
            

        return longest