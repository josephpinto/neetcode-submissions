class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        s_new, e_new = newInterval
        for i, [s,e] in enumerate(intervals):
            # ends before new interval, just append
            if e < s_new:
                res.append([s,e])
                continue
            # after interval, clean insert no merge
            if s > e_new:
                res.append([s_new,e_new])
                res += intervals[i:]
                return res
            # overlap
            merged_s = min(s,s_new)
            merged_e = max(e,e_new)
            s_new = merged_s
            e_new = merged_e
        res.append([s_new, e_new])
        return res
