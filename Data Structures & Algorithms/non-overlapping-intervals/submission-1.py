class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]
        for i in range(1,len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                res += 1
                # keep the one that ends earlier
                prev_end = min(end, prev_end)
            else:
                prev_end = end


        return res