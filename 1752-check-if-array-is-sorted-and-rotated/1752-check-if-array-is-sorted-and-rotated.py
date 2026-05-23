class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        for start in range(n):
            is_sorted = True
            for i in range(n - 1):
                curr_index = (start + i) % n
                next_index = (start + i + 1) % n
                
                if nums[curr_index] > nums[next_index]:
                    is_sorted = False
                    break 
            if is_sorted:
                return True
                
        return False