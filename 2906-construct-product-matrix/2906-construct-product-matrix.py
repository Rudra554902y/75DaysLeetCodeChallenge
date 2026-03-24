class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        pro=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                pro*=grid[i][j]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j]=(pro//grid[i][j])%12345
        return grid  