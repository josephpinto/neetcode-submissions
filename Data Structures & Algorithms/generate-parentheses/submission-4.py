class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def dfs(left,right):
            nonlocal curr
            if left == 0 and right == 0:
                res.append("".join(curr))
                return
            if left > 0:
                curr+='('
                dfs(left-1,right)
                curr.pop()
            if right > 0 and right > left:
                curr+=')'
                dfs(left,right-1)
                curr.pop()
        
        dfs(n,n)
        return res