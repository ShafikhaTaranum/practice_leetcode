'''class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        if n<=1:
            return 0
        queue = deque([(0, 0)]) 
        visited = {0}
        
        while queue:
            curr, steps = queue.popleft()
            
            if curr == n - 1:
                return steps
    
            if curr + 1 < n and (curr + 1) not in visited:
                visited.add(curr + 1)
                queue.append((curr + 1, steps + 1))
                
            if curr - 1 >= 0 and (curr - 1) not in visited:
                visited.add(curr - 1)
                queue.append((curr - 1, steps + 1))
                
            for i in range(n):
                if arr[i] == arr[curr] and i != curr:
                    if i not in visited:
                        visited.add(i)
                        queue.append((i, steps + 1))   
'''

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        

        value_indices = defaultdict(list)
        for i, val in enumerate(arr):
            value_indices[val].append(i)
        
        queue = deque([(0, 0)])
        visited = {0}
        
        while queue:
            curr, steps = queue.popleft()
            
            if curr == n - 1:
                return steps
            
        
            if curr + 1 < n and (curr + 1) not in visited:
                visited.add(curr + 1)
                queue.append((curr + 1, steps + 1))
            
    
            if curr - 1 >= 0 and (curr - 1) not in visited:
                visited.add(curr - 1)
                queue.append((curr - 1, steps + 1))
            
            for idx in value_indices[arr[curr]]:
                if idx not in visited:
                    visited.add(idx)
                    queue.append((idx, steps + 1))
            
            value_indices[arr[curr]] = []
        
        return -1

        