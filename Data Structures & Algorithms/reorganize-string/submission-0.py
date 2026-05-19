class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = Counter(s)
        heap    = []
        res     = ""

        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))
        
        while heap:
            firstCharCount, firstChar = heapq.heappop(heap)

            if not heap and firstCharCount < -1:
                return ""
            elif not heap and firstCharCount == -1:
                res = res + firstChar
                return res

            secCharCount, secChar = heapq.heappop(heap)

            res = res + firstChar
            res = res + secChar

            if (firstCharCount + 1) != 0:
                heapq.heappush(heap, (firstCharCount + 1, firstChar))
            if (secCharCount + 1) != 0:
                heapq.heappush(heap, (secCharCount + 1, secChar))
        
        return res

        # counter = {
        #     a: 1
        #     x: 1
        #     y: 2
        # }

        # s = "axyy"
        # heap = []
        # res  = "yaxy"
        # firstCharCount, firstChar = 0, "x"
        # secCharCount, secChar     = 0, "y"