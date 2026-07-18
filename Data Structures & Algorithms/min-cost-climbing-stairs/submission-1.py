class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # floor, cost[0], cost[1] ... cost[n-1]
        n = len(cost)
        min_costs = [0]*(n+1)

        for i in range(2,len(cost)+1):
            min_costs[i] = min(min_costs[i-1]+ cost[i-1],min_costs[i-2] + cost[i-2])
        
        return min_costs[n]