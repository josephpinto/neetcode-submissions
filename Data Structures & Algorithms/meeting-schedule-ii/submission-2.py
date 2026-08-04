"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetings = sorted([(i.start,i.end) for i in intervals])
        time = 0
        res = 0
        meeting_idx = 0
        end_times = []
        while meeting_idx < len(meetings):
            time = meetings[meeting_idx][0]
            heapq.heappush(end_times,meetings[meeting_idx][1])
            while time >= end_times[0]:
                heapq.heappop(end_times)
            res = max(res,len(end_times))
            meeting_idx += 1
        return res
