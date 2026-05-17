class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k] = max coins at (i, j) using exactly k neutralizations
        # Initialize with negative infinity since coins can be negative
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
