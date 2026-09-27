class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        maxx = 0
        while l<r:
            maxx = max(maxx, min(heights[l],heights[r])*(r-l))
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return maxx