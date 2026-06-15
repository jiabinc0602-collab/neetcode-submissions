class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            days = 1
            j = i+1
            while j < len(temperatures):
                if temp < temperatures[j]:
                    res[i] = days
                    break
                else:
                    days += 1
                    j += 1

        return res