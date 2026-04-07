class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        if not tasks:
            return []

        for i in range(len(tasks)):
            tasks[i].append(i)
        
        heapq.heapify(tasks)

        res  = []
        heap = []
        time = tasks[0][0]

        while tasks or heap:
            while tasks and tasks[0][0] <= time:
                enqTime, procTime, index = heapq.heappop(tasks)
                heapq.heappush(heap, (procTime, index))

            if not heap:
                time = tasks[0][0]
                continue

            if heap:
                procTime, index = heapq.heappop(heap)
                time += procTime
                res.append(index)

        return res