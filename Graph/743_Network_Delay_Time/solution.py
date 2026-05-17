class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        dist=[float('inf')]*(n+1)
        dist[k]=0
        pq=[(0,k)]
        while pq:
            time,node=heapq.heappop(pq)
            if time>dist[node]:
                continue
            for nei,wt in adj[node]:
                if time+wt<dist[nei]:
                    dist[nei]=time+wt
                    heapq.heappush(pq,(dist[nei],nei))
        max_time=max(dist[1:])
        if max_time!=float('inf'):
            return max_time
        else:
            return -1
