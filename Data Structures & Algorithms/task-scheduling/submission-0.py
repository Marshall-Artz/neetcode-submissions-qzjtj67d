class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [-count for count in Counter(tasks).values()]
        
        queue = deque()
        heapq.heapify(freq)

        res = deque()

        i = 0
        while freq or queue:
            print("freq:", freq, " queue:", queue, " i:", i)
            # Base case check queue front time
            if queue and i - queue[0][1] == n + 1:
                heapq.heappush(freq, queue.popleft()[0])

            if freq and freq[0] < 0:
                val = heapq.heappop(freq) + 1
                if val != 0:
                    queue.append((val, i))
            i += 1

        return i