# 743. Network Delay Time

**LeetCode Link:** https://leetcode.com/problems/network-delay-time/

## Difficulty: Medium
**Category:** Graph | Shortest Path | Dijkstra

---

## Problem Statement
You are given a network of `n` nodes labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi]`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

Send a signal from node `k`. Return the time it takes for all nodes to receive the signal. If it is impossible, return `-1`.

---

## Approach

### Algorithm: Dijkstra's Shortest Path
- **Time Complexity:** O((V + E) log V)
- **Space Complexity:** O(V + E)

### Key Insight:
- Use Dijkstra's algorithm to find shortest path from source node k to all other nodes
- The answer is the maximum distance among all nodes (time for signal to reach all nodes)
- If any node is unreachable, return -1

---

## Solution

```python
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
```

---

## Examples

### Example 1:
```
Input: times = [[1,2,1],[2,3,2],[1,3,4]], n = 3, k = 1
Output: 4
Explanation: Signal takes 1 time to reach node 2, 3 times to reach node 3
```

### Example 2:
```
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
Explanation: Node 1 is unreachable
```
