class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # eat one whole bucket an hour
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l+r) // 2
            timeTaken = self.timeTaken(piles,mid)
            if timeTaken > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        return res



    def timeTaken(self, piles, k):
        time = 0
        for p in piles:
            time += math.ceil(p / k)
        return time
