class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        removed = 0
        for i in range(1,len(intervals)):
            curr_start, curr_end = intervals[i]
            if curr_start >= prev_end:
                prev_end = curr_end
                continue
            prev_end = min(prev_end, curr_end)
            removed += 1
        return removed
            

        