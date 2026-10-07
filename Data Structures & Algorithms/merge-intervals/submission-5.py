class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for s,e in intervals[1:]:
            # overlap
            if s <= res[-1][1]:
                pre_s,pre_e = res.pop()
                new_end = max(pre_e,e)
                res.append([pre_s,new_end])
            else:
                res.append([s,e])
        return res
                