class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)  #descending order 
        minimum_cost=0
        for i in range(len(cost)):
            if (i+1)%3==0: #checks the curr candy is 3rd(free)
                continue # if it is 3rd candy (free) so skip to the nxt iteration 
            minimum_cost+=cost[i] #adds the prizes of 1,2 candy 
        return minimum_cost