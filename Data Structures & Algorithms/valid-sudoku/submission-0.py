class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]
        box = [[set() for _ in range(3)] for _ in range (3)]

        for r_index, r in enumerate(board):
            row = set()
            for c_index, i in enumerate(r):
                if i == ".":
                    continue

                if i in row:
                    return False
                else:
                    row.add(i)

                if i in columns[c_index]:
                    return False
                else:
                    columns[c_index].add(i)
                
                box_r = r_index // 3
                box_c = c_index // 3

                if i in box[box_r][box_c]:
                    return False
                else:
                    box[box_r][box_c].add(i)

        return True