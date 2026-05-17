# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

**LeetCode Link:** https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

## Difficulty: Medium
**Category:** Graph | Shortest Path | Floyd-Warshall

---

## Problem Statement
There are `n` cities numbered from `0` to `n - 1`. You are given an array `edges` where `edges[i] = [fromi, toi, weighti]` represents a bidirectional edge between cities.

You are also given the integer `distanceThreshold`. Return the city with the smallest number of other cities that are at a distance **less than or equal to** `distanceThreshold`. If there are multiple cities with the same smallest number of neighbors, return the city with the **greatest number**.

---

## Approach

### Algorithm: Floyd-Warshall All-Pairs Shortest Path
- **Time Complexity:** O(n³)
- **Space Complexity:** O(n²)

### Key Insight:
- Use Floyd-Warshall algorithm to compute shortest paths between all pairs of cities
- For each city, count how many cities are within the distance threshold
- Track the city with the minimum count (ties broken by larger city number)

---

## Solution

```python
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
```

---

## Examples

### Example 1:
```
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: City 3 has neighbors at distances 4 (via 1), 1 (via 2), 0. Count = 2
```

### Example 2:
```
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: City 0 has neighbors at distances 2 (city 1), 0. Count = 1
```
