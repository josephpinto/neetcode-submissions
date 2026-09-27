class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals:
            return ""
        vals = self.vals[key]
        res = ""
        l,r = 0, len(vals)-1
        while l<=r:
            mid = (l+r)//2
            if vals[mid][1] > timestamp:
                r = mid - 1
            else:
                res = vals[mid][0]
                l = mid + 1
        return res
