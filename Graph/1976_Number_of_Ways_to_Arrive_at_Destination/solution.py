class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod=10**9+7
        graph=[[] for _ in range(n)]
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        dist=[float('inf')]*n
        ways=[0]*n
        pq=[(0,0)]
        dist[0]=0
        ways[0]=1
        while pq:
            d,node=heapq.heappop(pq)
            if d>dist[node]:
               continue
            for nei,wt in graph[node]:
                new=dist[node]+wt
                if new<dist[nei]:
                    dist[nei]=new
                    ways[nei]=ways[node]
                    heapq.heappush(pq,(new,nei))
                elif new==dist[nei]:
                    ways[nei]=(ways[nei]+ways[node])%mod
        return ways[n-1]%mod
