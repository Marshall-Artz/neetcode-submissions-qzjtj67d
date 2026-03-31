class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a != 0: heapq.heappush(heap, (-a, 'a'))
        if b != 0: heapq.heappush(heap, (-b, 'b'))
        if c != 0: heapq.heappush(heap, (-c, 'c'))

        res = []
        
        while heap:
            firstCount, firstChar = heapq.heappop(heap)

            if len(res) >= 2 and res[-1] == res[-2] == firstChar:
                if not heap:
                    break

                secCount, secChar = heapq.heappop(heap)
                res.append(secChar)
                secCount += 1

                if secCount < 0:
                    heapq.heappush(heap, (secCount, secChar))
            else:
                res.append(firstChar)
                firstCount += 1
            
            if firstCount < 0:
                heapq.heappush(heap, (firstCount, firstChar))
        
        return "".join(res)