class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        appended = False
        res = []
        for i, interval in enumerate(intervals):
            start, end = interval
            if newInterval[0] > end:
                res.append([start,end])
                continue
            if newInterval[1] < start:
                res.append(newInterval)
                res += intervals[i:]
                return res
            # overlapping
            new_min = min(start,newInterval[0])
            new_max = max(end, newInterval[1])
            newInterval = [new_min,new_max]
        res.append(newInterval)
        return res

            