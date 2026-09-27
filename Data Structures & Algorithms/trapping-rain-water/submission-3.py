class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0]
        post = [0]
        for i in range(1, len(height)):
            pre.append(max(pre[-1],height[i-1]))
        for i in range(len(height)-2,-1,-1):
            post.append(max(post[-1], height[i+1]))
        post = post[::-1]
        
        res = 0
        for i,v in enumerate(height):
            res += max(0,(min(pre[i],post[i])-v))
        return res
