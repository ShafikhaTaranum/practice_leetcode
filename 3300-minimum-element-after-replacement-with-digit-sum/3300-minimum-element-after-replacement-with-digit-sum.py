class Solution:
    def getdigit(self, n: int) -> int:
        m = n
        ans = 0
        while m>0:
            rem = m%10
            ans += rem
            m = m//10
        return ans

    def minElement(self, nums: List[int]) -> int:
        ans  = 1000000
        for i in nums:
            k = self.getdigit(i)
            ans = min(k,ans)


        return ans
        