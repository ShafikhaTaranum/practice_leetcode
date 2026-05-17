# 1976. Number of Ways to Arrive at Destination

**LeetCode Link:** https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

## Difficulty: Hard
**Category:** Graph | Shortest Path | Dijkstra

---

## Problem Statement
You are in a city represented as a graph with `n` intersections numbered from `0` to `n - 1`, and `roads` where each road is represented as `[ui, vi, timei]`. You need to find the number of ways to go from intersection `0` to intersection `n - 1` in the shortest time.

Return the number of ways to arrive at intersection `n - 1` in the shortest time. Since the answer may be large, return it modulo `10^9 + 7`.

---

## Approach

### Algorithm: Dijkstra + Path Counting
- **Time Complexity:** O((V + E) log V)
- **Space Complexity:** O(V + E)

### Key Insight:
- Use Dijkstra's algorithm to find shortest distances
- Track the number of ways to reach each node with the shortest distance
- When we find a better path, reset the count
- When we find an equal shortest path, add to the count

---

## Solution

```python
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
```

---

## Examples

### Example 1:
```
Input: n = 6, roads = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[2,4,3],[2,5,4],[3,4,2],[4,5,5]]
Output: 3
Explanation: 3 ways to reach from 0 to 5 with shortest time 7
```
