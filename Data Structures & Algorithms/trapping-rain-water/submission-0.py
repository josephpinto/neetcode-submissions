class Solution:
    def trap(self, heights: List[int]) -> int:
        biggestLefts = []
        biggestRights = [0]*len(heights)
        biggestLeft = 0
        for i in range(len(heights)):
            biggestLefts.append(biggestLeft)
            biggestLeft = max(heights[i], biggestLeft)
            

        biggestRight = 0
        for i in range(len(heights)-1,-1,-1):
            biggestRights[i] = biggestRight
            biggestRight = max(heights[i], biggestRight)
        
        result = 0
        for i,height in enumerate(heights):
            water = self.getWaterVolume(height, biggestLefts[i], biggestRights[i])
            result += water
        return result

            

    def getWaterVolume(self, floorHeight, biggestLeft, biggestRight):
        return max(0,min(biggestLeft,biggestRight) - floorHeight)