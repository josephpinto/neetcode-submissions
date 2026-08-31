class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        res.append(intervals[0])
        for s,e in intervals[1:]:
            curr_s, curr_e = res[-1]
            if s <= curr_e:
                res.pop()
                new_s, new_e = min(curr_s,s), max(curr_e,e)
                res.append([new_s,new_e])
            else:
                res.append([s,e])
        return res
