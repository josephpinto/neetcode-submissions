class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def dfs(open,close,path):
            if open == close == n:
                res.append(path)
                return
            if open > close and close < n:
                dfs(open,close+1,path+')')
            if open < n:
                dfs(open+1,close,path+'(')

        dfs(0,0,"")
        return res