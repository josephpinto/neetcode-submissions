from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.myMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.myMap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.myMap[key]
        if not vals:
            return ""
        l,r = 0, len(vals)-1
        result = ""
        while l<=r:
            mid = (l+r)//2
            if vals[mid][0] == timestamp:
                return vals[mid][1]
            if vals[mid][0] > timestamp:
                r = mid-1
            else:
                result = vals[mid][1]
                l = mid+1
        return result
        
