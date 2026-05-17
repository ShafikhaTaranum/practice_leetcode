# 1631. Path With Minimum Effort

**LeetCode Link:** https://leetcode.com/problems/path-with-minimum-effort/

## Difficulty: Medium
**Category:** Graph | Dijkstra | Matrix

---

## Problem Statement
You are a hiker preparing for an upcoming hike. You are given a 2D `heights` array of size `rows x columns`, where `heights[row][col]` represents the height at location (row, col).

The *effort* of a path is defined as the **maximum absolute difference in heights** between two *consecutive cells* of the path.

Return the minimum effort required to travel from the top-left cell (0, 0) to the bottom-right cell (rows - 1, columns - 1).

---

## Approach

### Algorithm: Dijkstra's Algorithm on Grid
- **Time Complexity:** O(rows × cols × log(rows × cols))
- **Space Complexity:** O(rows × cols)

### Key Insight:
- Use Dijkstra to find the path with minimum maximum effort
- The priority is the current effort level, not the sum
- Track the maximum effort encountered so far on the path
- Stop as soon as we reach the destination

---

## Solution

```python
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
```

---

## Examples

### Example 1:
```
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: Path with minimum effort is 1 -> 3 -> 5 -> 3 -> 5
```

### Example 2:
```
Input: heights = [[1,2,3],[3,2,1]]
Output: 1
Explanation: Path 1 -> 2 -> 3 -> 2 -> 1 with max difference 1
```
