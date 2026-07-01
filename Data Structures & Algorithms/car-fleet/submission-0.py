class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        positionSpeeds = [(position[i],speed[i]) for i in range(len(position))]
        positionSpeeds.sort(reverse=True)
        for position,speed in positionSpeeds:
            timeTaken = (target-position) / speed
            if stack and stack[-1] >= timeTaken:
                continue
            stack.append(timeTaken)
        return len(stack)
                