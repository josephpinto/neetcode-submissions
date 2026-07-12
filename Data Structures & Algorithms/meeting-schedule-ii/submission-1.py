"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)

        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        max_rooms = 0
        curr_rooms = 0
        s = e = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                s += 1
                curr_rooms += 1
                max_rooms = max(max_rooms, curr_rooms)
            else:
                e += 1
                curr_rooms -= 1
            
        return max_rooms


