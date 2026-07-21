from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        cands = self.vals[key]
        if not cands: return ""

        l,r = 0, len(cands)-1
        res = ""
        while l<=r:
            mid = (l+r)//2
            if cands[mid][0] > timestamp:
                r = mid - 1
            else:
                res = cands[mid][1]
                l = mid + 1
        return res