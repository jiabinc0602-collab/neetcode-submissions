class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        for i, row in enumerate(matrix):
            if i < len(matrix)-1 and target >= matrix[i+1][0]:
                continue
            for j, item in enumerate(row):
                if item == target:
                    res = True

        return res
