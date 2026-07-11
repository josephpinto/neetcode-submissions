class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            last_start, last_end = res[-1]
            curr_start, curr_end = intervals[i]
            if curr_start > last_end:
                res.append([curr_start,curr_end])
                continue
            res.pop()
            new_start, new_end = min(last_start,curr_start), max(last_end,curr_end)
            res.append([new_start,new_end])
        return res
