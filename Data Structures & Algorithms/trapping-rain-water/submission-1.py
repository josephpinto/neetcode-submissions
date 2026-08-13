class Solution:
    def trap(self, height: List[int]) -> int:
        big_left = []
        big_right = [0]

        biggest = 0
        for i in range(len(height)):
            biggest = max(biggest, height[i])
            big_left.append(biggest)
        
        biggest = 0
        for i in range(len(height)-1,-1,-1):
            biggest = max(biggest, height[i])
            big_right.append(biggest)
        big_right.reverse()
        
        res =0
        for i,h in enumerate(height): 
            vol = max(min(big_left[i],big_right[i])-h,0)
            res += vol
        return res