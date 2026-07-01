class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_oranges = 0
        # initial loop to find where all the rotten fruits in grid are
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        if fresh_oranges == 0:
            return 0
        minutes, fresh_oranges_left = self.bfs(grid, queue, fresh_oranges)
        if fresh_oranges_left > 0:
            return -1
        return minutes
        
    
    def bfs(self, grid, queue, fresh_oranges):
        minutes = -1
        w, h = len(grid), len(grid[0])
        while queue:
            level_size = len(queue)

            minutes += 1
            for _ in range(level_size):
                r, c = queue.popleft()
                if r+1 < w:
                    if grid[r+1][c] == 1:
                        grid[r+1][c] = 2
                        fresh_oranges -= 1
                        queue.append((r+1,c))
                if r-1 >= 0:
                    if grid[r-1][c] == 1:
                        grid[r-1][c] = 2
                        fresh_oranges -= 1
                        queue.append((r-1,c))
                if c+1 < h:
                    if grid[r][c+1] == 1:
                        grid[r][c+1] = 2
                        fresh_oranges -= 1
                        queue.append((r,c+1))
                if c-1 >= 0:
                    if grid[r][c-1] == 1:
                        grid[r][c-1] = 2
                        fresh_oranges -= 1
                        queue.append((r,c-1))
        return minutes, fresh_oranges
                    

                
        