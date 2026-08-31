class TimeMap:

    def __init__(self):
        self.hits = {} # key -> [time, val]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hits:
            self.hits[key] = []
        self.hits[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hits: 
            return ""
        vals = self.hits[key]
        res = ""
        res_ts = 0
        l,r = 0, len(vals)-1
        while l<=r:
            mid = (l+r)//2
            saved_ts = vals[mid][0]
            if saved_ts <= timestamp:
                
                res = vals[mid][1]
                
                l = mid + 1
            else:
                r = mid - 1
        return res
