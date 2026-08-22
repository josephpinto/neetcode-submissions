class Solution:
    def trap(self, height: List[int]) -> int:
        pre = []
        post = []
        pre.append(0)
        for i in range(1,len(height)):
            pre.append(max(pre[-1],height[i-1]))
        post.append(0)
        for i in range(len(height)-2,-1,-1):
            post.append(max(post[-1],height[i+1]))
        post = post[::-1]

        res = 0
        for i in range(len(height)):
            res += max(min(pre[i],post[i])-height[i],0)
        return res
