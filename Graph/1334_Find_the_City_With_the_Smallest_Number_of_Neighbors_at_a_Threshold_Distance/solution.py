class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph=[[float('inf')] *n for _ in range(n)]
        for i in range(n):
            graph[i][i]=0
        for u,v,w in edges:
            graph[u][v]=w
            graph[v][u]=w
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j]=min(graph[i][j],graph[i][via]+graph[via][j])
        city=-1
        minc=float('inf')
        for i in range(n):
            count=0
            for j in range(n):
                if graph[i][j]<=distanceThreshold:
                    count+=1
            count-=1
            if count<=minc:
                minc=count
                city=i
        return city
