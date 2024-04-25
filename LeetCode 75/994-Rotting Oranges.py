class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rottenq = []
        heapq.heapify(rottenq)
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    heapq.heappush(rottenq, (0, [i, j])) # minute, [i, j]
        minutes = 0
        # BFS with heap
        while rottenq:
            local_minute, [r_i, r_j] = heapq.heappop(rottenq)
            if local_minute > minutes:
                minutes += 1
            neighbors = [[r_i + 1, r_j], 
                         [r_i, r_j + 1],
                         [r_i - 1, r_j],
                         [r_i, r_j - 1]]
            for i, j in neighbors:
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    # It is a fresh orange
                    grid[i][j] = 2
                    heapq.heappush(rottenq, (local_minute + 1, [i, j]))
        
        # Check whether if there is any fresh orange
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minutes