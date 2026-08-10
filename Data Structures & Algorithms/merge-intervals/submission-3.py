class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()
        for i, (s,e) in enumerate(intervals):
            if stack and stack[-1][1] >= s:
                stack_s, stack_e = stack.pop()
                new_s, new_e = min(stack_s,s), max(stack_e, e)
                stack.append([new_s,new_e])
            else:
                stack.append([s,e])
        return stack