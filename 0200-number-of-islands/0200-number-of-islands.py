class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        vis=[[0 for i in range(n)]for j in range(m)]
        dx=[0,0,-1,1]
        dy=[1,-1,0,0]
        islands=0
        def dfs(i,j,vis):
            vis[i][j]=1
            for k in range(4):
                r,c=i+dx[k],j+dy[k]
                if r>=0 and c>=0 and r<m and c<n and grid[r][c]=="1" and vis[r][c]==0:
                    dfs(r,c,vis)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and vis[i][j]==0:
                    dfs(i,j,vis)
                    islands+=1
        return islands
            
        