class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]

        curr_r, dir = 0,1

        for c in s:
            res[curr_r]+= c
            curr_r += dir
            if curr_r == 0 or curr_r == numRows-1:
                dir*=-1
        return ''.join(''.join(r) for r in res)