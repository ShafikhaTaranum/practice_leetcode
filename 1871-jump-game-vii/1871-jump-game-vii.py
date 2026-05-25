class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        
        if s[-1] == '1': 
            return False
            
        dp = [False] * n
        dp[0] = True
        reach = 0
        
        for i in range(minJump, n):
            if dp[i - minJump]:
                reach += 1
                
            if i > maxJump and dp[i - maxJump - 1]:
                reach -= 1
                
            if reach > 0 and s[i] == '0':
                dp[i] = True
                
        return dp[-1]