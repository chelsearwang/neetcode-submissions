class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1 = cost[0]
        prev2 = cost[1]
        n = len(cost)

        for i in range(2, n):
            curr = min(prev1, prev2) + cost[i]
            prev1 = prev2
            prev2 = curr
            
        return min(prev1, prev2)