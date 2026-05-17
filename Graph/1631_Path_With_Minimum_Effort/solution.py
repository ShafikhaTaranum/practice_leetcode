class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n,m=len(heights),len(heights[0])
        dist=[[float('inf')]*m for i in range(n)]
        dist[0][0]=0
        pq=[(0,0,0)]
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        while pq:
            effort,r,c=heapq.heappop(pq)
            if r==n-1 and c==m-1:
                return effort
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if 0<=nr<n and 0<=nc<m:
                    neweff=max(effort,abs(heights[r][c]-heights[nr][nc]))
                    if neweff<dist[nr][nc]:
                        dist[nr][nc]=neweff
                        heapq.heappush(pq,(neweff,nr,nc))
        return 0
