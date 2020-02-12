import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        Q = collections.deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if (i,j) not in visited:
                        Q.append((i,j))
                        while Q:
                            "BFS"
                            cur = Q.popleft()
                            if cur in visited:
                                continue
                            visited.add(cur)
                            x,y = cur[0], cur[1]
                            for a, b in directions:
                                if not(a+x < 0 or a+x>=m or b+y <0 or b+y >= n):
                                    if grid[a+x][b+y] == "1":
                                        if grid[a+x][b+y] not in visited:
                                            Q.append((a+x,b+y))
                        count += 1
        return count