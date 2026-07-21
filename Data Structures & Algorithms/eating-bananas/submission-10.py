class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r

        while l<=r:
            cand_k = (l+r)//2
            time = self.eat(cand_k,piles)
            if time > h:
                l = cand_k +1
            else:
                res = min(cand_k,res)
                r = cand_k-1
        return res



    def eat(self, k, piles):
        time = 0
        for p in piles:
            time += math.ceil(p / k)
        return time