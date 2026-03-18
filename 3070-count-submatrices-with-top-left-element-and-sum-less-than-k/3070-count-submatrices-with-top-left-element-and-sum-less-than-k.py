class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        c=0
        n,m=len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                grid[i][j]+=(grid[i-1][j] if i-1>=0 else 0)
                grid[i][j]+=(grid[i][j-1] if j-1>=0 else 0)
                grid[i][j]-=(grid[i-1][j-1] if (i-1>=0 and j-1>=0) else 0)
                if grid[i][j]<=k:
                    c+=1
        return c