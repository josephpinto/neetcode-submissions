class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        globalMax=0
        while l<r:
            leftBar, rightBar = heights[l], heights[r]
            volume = (r-l) * min(leftBar,rightBar)
            globalMax = max(globalMax,volume)
            if leftBar < rightBar:
                l += 1
            else:
                r -= 1
        return globalMax