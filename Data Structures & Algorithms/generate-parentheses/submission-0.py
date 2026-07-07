class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def dfs(f,b, curr_res):
            if f == b == 0:
                res.append("".join(curr_res))
            if f > 0:
                curr_res.append('(')
                dfs(f-1,b,curr_res)
                curr_res.pop()
            if b > f and b > 0:
                curr_res.append(')')
                dfs(f,b-1,curr_res)
                curr_res.pop()
        dfs(n,n,[])
        return res