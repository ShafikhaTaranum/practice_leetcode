class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def count_upto(n):
            if n < 0: return 0
            s = str(n)
            memo = {}

            def dp(idx, last, prev, tight, started):
                if idx == len(s):
                    return (1, 0)
                
                state = (idx, last, prev, tight, started)
                if state in memo: return memo[state]
                
                total_count = 0
                total_sum = 0
                limit = int(s[idx]) if tight else 9
                
                for d in range(limit + 1):
                    new_tight = tight and (d == limit)
                    new_started = started or (d > 0)
                    
                    waviness_added = 0
                    if started and prev != -1:
                        if (prev < last > d) or (prev > last < d):
                            waviness_added = 1
                    
                    if new_started:
                        if started:
                            new_last, new_prev = d, last
                        else:
                            new_last, new_prev = d, -1 
                    else:
                        new_last, new_prev = -1, -1
                    
                    count, waviness_sum = dp(idx + 1, new_last, new_prev, new_tight, new_started)
                    
                    total_count += count
                    total_sum += waviness_sum + (count * waviness_added)
                
                memo[state] = (total_count, total_sum)
                return (total_count, total_sum)

            return dp(0, -1, -1, True, False)[1]

        return count_upto(num2) - count_upto(num1 - 1)