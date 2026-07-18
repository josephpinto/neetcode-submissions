class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # floor, cost[0], cost[1] ... cost[n-1]
        min_costs = [0]*(len(cost)+1)

        min_costs[1] = cost[0] 

        for i in range(2,len(cost)+1):
            min_costs[i] = cost[i-1] + min(min_costs[i-1],min_costs[i-2])
        return min(min_costs[-1],min_costs[-2])