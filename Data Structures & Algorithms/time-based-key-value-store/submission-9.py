class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map: 
            return ""
        vals = self.time_map[key]
        res = ""
        res_ts = 0
        l,r = 0, len(vals)-1
        while l<=r:
            mid = (l+r)//2
            saved_ts = vals[mid][1]
            if saved_ts <= timestamp:
                
                res = vals[mid][0]
                
                l = mid + 1
            else:
                r = mid - 1

        return res
