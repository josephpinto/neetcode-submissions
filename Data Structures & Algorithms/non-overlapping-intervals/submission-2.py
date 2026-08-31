class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # track furthest end of so far non-overlapping
        # always choose to remove one with the furthest potential end to minimize overlap (greedy)
        intervals.sort()
        curr_end = intervals[0][1]
        res = 0
        for s,e in intervals[1:]:
            if s >= curr_end:
                curr_end = e
            else:
                res += 1
                curr_end = min(curr_end,e)
        
        return res