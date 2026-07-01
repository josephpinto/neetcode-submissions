class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                seenIdx, _ = stack.pop()
                result[seenIdx] = idx-seenIdx

            stack.append((idx,temp))
        return result

