class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i,height in enumerate(heights):
            if not stack or stack[-1][1] <= height:
                stack.append((i,height))
            else:
                lastPoppedIdx = i
                while stack and stack[-1][1] > height:
                    seenIdx, seenHeight = stack.pop()
                    currArea = seenHeight*(i-seenIdx)
                    maxArea = max(maxArea,currArea)
                    lastPoppedIdx = seenIdx

                stack.append((lastPoppedIdx,height))
        while stack:
            seenIdx, seenHeight = stack.pop()
            currArea = seenHeight*(len(heights)-seenIdx)
            maxArea = max(maxArea,currArea)
        return maxArea
