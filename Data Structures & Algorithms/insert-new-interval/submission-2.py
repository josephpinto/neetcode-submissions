class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        3 cases:
        1. curr interval is before
        2. curr interval is after
        3. curr interval overlaps -> merge
        """
        res = []
        for i, interval in enumerate(intervals):
            s,e = interval[0], interval[1]
            # case 1
            if e < newInterval[0]:
                res.append([s,e])
                continue
            # case 2
            if s > newInterval[1]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            # case 3
            new_s = min(s, newInterval[0])
            new_e = max(e, newInterval[1])
            newInterval = [new_s,new_e]
        res.append(newInterval)
        return res