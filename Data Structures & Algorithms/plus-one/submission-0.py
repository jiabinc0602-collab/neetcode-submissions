class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i, n in enumerate(reversed(digits)):
            index = len(digits) - 1 - i
            if index == 0 and n == 9:
                digits[index] = 0
                newList = [1] + digits
                return newList
            if n == 9:
                digits[index] = 0
                continue
            else:
                digits[index] += 1
                break
            
        return digits
