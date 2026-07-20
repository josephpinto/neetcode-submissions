class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse=True)
        r = res = max(piles)
        l = 1

        while l<=r:
            cand_k = (l+r)// 2
            time_taken = self.getTime(cand_k,piles)
            if time_taken <= h:
                res = min(res,cand_k)
                r = cand_k - 1
            else:
                l = cand_k + 1
        return res

    def getTime(self, k, piles):
        time = 0
        for p in piles:
            if p < k:
                time += 1
            else:
                time += math.ceil(p/k)
        return time

