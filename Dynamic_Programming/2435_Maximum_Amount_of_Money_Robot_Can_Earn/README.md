# 2435. Maximum Amount of Money Robot Can Earn

**LeetCode Link:** https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

## Difficulty: Hard
**Category:** Dynamic Programming | Grid Traversal

---

## Problem Statement
You are in a grid with `m` rows and `n` columns. You start at cell `(0, 0)` and want to reach cell `(m - 1, n - 1)`. You can move down or right at any point in time.

The grid contains coins in each cell. You can collect the coin in a cell when you visit it. However, there are also cells with negative coins (robbers) that you want to avoid.

You have the ability to **neutralize** a robber cell (make its effect 0 instead of taking the negative value) up to **2 times**. When you neutralize a cell, you collect 0 coins from it instead of the negative value.

Return the maximum amount of coins you can collect.

---

## Approach

### Algorithm: Dynamic Programming with State Tracking
- **Time Complexity:** O(m × n × 3) = O(m × n)
- **Space Complexity:** O(m × n × 3) = O(m × n)

### Key Insight:
- Use `dp[i][j][k]` to represent the maximum coins at position `(i, j)` using exactly `k` neutralizations (0, 1, or 2)
- For each cell, try two options:
  1. Normal move: take the coin value
  2. Neutralize move (if it's negative and we have neutralizations left): take 0 instead
- Track the maximum value for each state

---

## Solution

```python
class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k] = max coins at (i, j) using exactly k neutralizations
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Base case for the starting cell (0, 0)
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0 # Use 1 neutralization right at the start
            
        for i in range(m):
            for j in range(n):
                # Skip the starting cell since we already initialized it
                if i == 0 and j == 0:
                    continue
                
                # Try all possible amounts of neutralizations used (0, 1, and 2)
                for k in range(3):
                    
                    # 1. Standard move: don't neutralize the current cell
                    prev = -float('inf')
                    if i > 0:
                        prev = max(prev, dp[i-1][j][k])
                    if j > 0:
                        prev = max(prev, dp[i][j-1][k])
                    
                    if prev != -float('inf'):
                        dp[i][j][k] = prev + coins[i][j]
                    
                    # 2. Special move: neutralize the current cell (only if it's a robber)
                    if k > 0 and coins[i][j] < 0:
                        prev_k = -float('inf')
                        if i > 0:
                            prev_k = max(prev_k, dp[i-1][j][k-1])
                        if j > 0:
                            prev_k = max(prev_k, dp[i][j-1][k-1])
                            
                        if prev_k != -float('inf'):
                            # Add 0 instead of the negative coin value
                            dp[i][j][k] = max(dp[i][j][k], prev_k) 

        # The answer is the maximum profit at the bottom-right corner 
        # out of paths that used 0, 1, or 2 neutralizations.
        return max(dp[m-1][n-1])
```

---

## Examples

### Example 1:
```
Input: coins = [[10,10],[10,10]]
Output: 40
Explanation: Collect all 4 cells
```

### Example 2:
```
Input: coins = [[-5,5],[2,-1]]
Output: 8
Explanation: Start at (0,0), collect 0 (neutralize -5). Then go (0,1) collect 5. Then (1,1) collect 2, and (1,0) collect -1. Total = 5+2-1 = 6.
```
