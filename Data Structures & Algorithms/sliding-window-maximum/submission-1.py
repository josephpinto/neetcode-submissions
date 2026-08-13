class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        res.append(-heap[0][0])
        for i in range(1,len(nums)-k+1):
            heapq.heappush(heap,(-nums[i+k-1],i+k-1))
            while heap and heap[0][1] < i:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res