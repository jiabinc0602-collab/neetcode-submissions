class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        for i, row in enumerate(matrix):
            if i < len(matrix)-1 and target >= matrix[i+1][0]:
                continue
            low = 0
            high = len(matrix[0]) - 1
            while low <= high:
                mid = (low + high)//2
                if target == matrix[i][mid]:
                    res = True
                    break
                elif target < matrix[i][mid]:
                    high = mid-1
                else:
                    low = mid+1

        return res
