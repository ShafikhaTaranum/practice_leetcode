class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for _ in range(n)]
        for u,v,w in flights:
            adj[u].append((v,w))
        dist=[float('inf')]*n
        dist[src]=0
        q=deque([(src,0,0)])
        while q:
            node,cost,stops=q.popleft()
            if stops>k:
                continue
            for nei,price in adj[node]:
                new_cost=cost+price
                if new_cost<dist[nei]:
                    dist[nei]=new_cost
                    q.append((nei,new_cost,stops+1))
        if dist[dst]==float('inf'):
            return -1
        else:
            return dist[dst]
