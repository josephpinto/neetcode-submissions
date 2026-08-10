class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxx = 0
        stack = []
        for i, height in enumerate(heights):
            last_popped_idx = i

            while stack and stack[-1][1] > height:
                og_idx, pop_height = stack.pop()
                maxx = max(maxx,(i-og_idx)*pop_height)
                last_popped_idx = og_idx
            stack.append((last_popped_idx,height))
        while stack:
            og_idx, pop_height = stack.pop()
            maxx = max(maxx,(len(heights)-og_idx)*pop_height)
        return maxx
