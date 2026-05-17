# 787. Cheapest Flights Within K Stops

**LeetCode Link:** https://leetcode.com/problems/cheapest-flights-within-k-stops/

## Difficulty: Medium
**Category:** Graph | Shortest Path | Bellman-Ford

---

## Problem Statement
There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [fromi, toi, pricei]` indicates there is a flight from city `fromi` to city `toi` with cost `pricei`.

You are also given three integers `src`, `dst`, and `k`, return the cheapest price from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.

---

## Approach

### Algorithm: BFS with Cost and Stop Tracking
- **Time Complexity:** O(n × k)
- **Space Complexity:** O(n)

### Key Insight:
- Use BFS with queue to explore paths
- Track cost and number of stops for each node
- Only proceed if we haven't exceeded k stops
- Update distance when we find a cheaper path

---

## Solution

```python
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
```

---

## Examples

### Example 1:
```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: Cheapest path is 0 -> 1 -> 2 with total cost 200
```

### Example 2:
```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: Must take direct flight with no stops
```
