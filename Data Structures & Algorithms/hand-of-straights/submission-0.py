import heapq
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = Counter(hand)
        heap = list(counts.keys())
        heapq.heapify(heap)

        while heap:
            while heap and counts[heap[0]] == 0:
                heapq.heappop(heap)
            if not heap:
                break
            min_val = heap[0]
            curr_val = min_val
            num_to_add = groupSize
            while num_to_add > 0:
                if not counts[curr_val] or counts[curr_val] == 0:
                    return False
                counts[curr_val] -= 1
                num_to_add -= 1
                curr_val += 1
        return True
                    

