class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestsum=float('-inf')
        currsum=0
        for num in nums:
            currsum += num
            if currsum > largestsum:
                largestsum = currsum
            if currsum <0:
                currsum =0
        return largestsum     