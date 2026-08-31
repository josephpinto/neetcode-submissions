"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        maxx = 0
        starts = sorted(intervals,key=lambda i: i.start)
        ends = sorted(intervals,key=lambda i: i.end)

        s = e = 0
        curr = 0
        while s < len(intervals):
            if starts[s].start < ends[e].end:
                s += 1
                curr += 1
            else:
                e += 1
                curr -= 1
            maxx = max(maxx, curr)




        return maxx