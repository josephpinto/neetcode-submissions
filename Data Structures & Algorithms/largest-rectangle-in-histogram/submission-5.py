class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i,h in enumerate(heights):
            last_popped = i
            while stack and stack[-1][1] > h:
                stored_idx, height = stack.pop()
                res = max(res, (i-stored_idx)*height)
                last_popped = stored_idx
            stack.append((last_popped,h))
        while stack:
            stored_idx, height = stack.pop()
            res = max(res, (i-stored_idx+1)*height)
        return res
