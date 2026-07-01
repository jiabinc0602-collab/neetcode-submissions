class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    islands += 1
                    # flip the island first
                    grid[r][c] = '0'
                    # call bfs to sink island
                    self.bfs(grid, r, c)
                    
        return islands

    def bfs(self, grid, r, c):
        queue = deque([(r,c)])
        # width and height of matrix
        w, h = len(grid), len(grid[0])

        while queue:
            r, c = queue.popleft()
            if r + 1 < w:
                if grid[r+1][c] == '1':
                    grid[r+1][c] = '0'
                    queue.append((r+1,c))
            if r - 1 >= 0:
                if grid[r-1][c] == '1':
                    grid[r-1][c] = '0'
                    queue.append((r-1,c))
            if c+1 < h:
                if grid[r][c+1] == '1':
                    grid[r][c+1] = '0'
                    queue.append((r,c+1))
            if c-1 >= 0:
                if grid[r][c-1] == '1':
                    grid[r][c-1] = '0'
                    queue.append((r,c-1))
            
                

    