"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda i: i.start)

        last_interval = intervals[0]

        for i in range(1,len(intervals)):
            last_start,last_end = last_interval.start, last_interval.end
            curr_start,curr_end = intervals[i].start, intervals[i].end
            if curr_start < last_end:
                return False
            last_interval = intervals[i]
        return True
        