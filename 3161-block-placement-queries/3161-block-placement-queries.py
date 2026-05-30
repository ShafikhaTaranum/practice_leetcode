from sortedcontainers import SortedList
import bisect

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MAX_X = min(50000, 3 * len(queries)) + 1
        bit = [0] * (MAX_X + 1)
        
        def update(i, val):
            i += 1
            while i <= MAX_X:
                bit[i] = max(bit[i], val)
                i += i & (-i)
                
        def query(i):
            i += 1
            res = 0
            while i > 0:
                res = max(res, bit[i])
                i -= i & (-i)
            return res

        # 1. Collect all obstacles to build the final state first
        all_obstacles = [0, MAX_X]
        for q in queries:
            if q[0] == 1:
                all_obstacles.append(q[1])
        all_obstacles.sort()
        
        # 2. Build the Fenwick Tree using the final stable gaps
        for i in range(1, len(all_obstacles)):
            update(all_obstacles[i], all_obstacles[i] - all_obstacles[i - 1])
            
        # 3. Process backward (removing obstacles converts splits into merges)
        results = []
        active = SortedList(all_obstacles)
        
        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]
                idx = active.index(x)
                L = active[idx - 1]
                R = active[idx + 1]
                
                active.remove(x)
                update(R, R - L)
                
            elif q[0] == 2:
                x, sz = q[1], q[2]
                idx = active.bisect_right(x)
                L = active[idx - 1]
                
                max_gap = max(query(L), x - L)
                results.append(max_gap >= sz)
                
        return results[::-1]