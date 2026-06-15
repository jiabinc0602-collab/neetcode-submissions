class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n > 0:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = self.squares(n)

    def squares(self, n):
            sum = 0
            for c in str(n):
                sum += int(c) ** 2
            return sum