class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        heap = list(counts.keys())
        heapq.heapify(heap)
        if len(hand) % groupSize != 0:
            return False

        while heap:
            while heap and counts[heap[0]] == 0:
                heapq.heappop(heap)
            if not heap:
                return True
            min_num = heap[0]
            num_to_add = groupSize
            curr = heap[0]
            for _ in range(num_to_add):
                if not counts[curr] or counts[curr] < 1:
                    return False
                counts[curr] -= 1
                curr += 1
        return True
