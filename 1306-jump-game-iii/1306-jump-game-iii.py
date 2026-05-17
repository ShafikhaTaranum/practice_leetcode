class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue=deque([start])
        visited =set()

        while queue:
            indx=queue.popleft()
            if indx<0 or indx>=len(arr) or indx in visited:
                continue
            elif arr[indx]==0:
                return True
            visited.add(indx)
            queue.append(indx+arr[indx])
            queue.append(indx-arr[indx])
        return False 
        
        