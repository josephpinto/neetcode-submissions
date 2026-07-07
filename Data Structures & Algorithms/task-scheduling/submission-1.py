import heapq
from collections import deque
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        heap = [(-count) for _, count in task_counts.items()]
        heapq.heapify(heap)
        time = 0
        queue = deque()

        while heap or queue:
            if heap:
                time += 1
                remaining_count = -heapq.heappop(heap)
                remaining_count -= 1
                if remaining_count > 0:
                    queue.append((time+n,remaining_count))
            else:
                # heap empty - idle time
                required_time, remaining_count = queue[0]
                if required_time > time:
                    time = required_time
            if queue and time == queue[0][0]:
                required_time, remaining_count = queue.popleft()
                heapq.heappush(heap, (-remaining_count))

        return time