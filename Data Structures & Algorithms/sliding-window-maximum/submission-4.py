class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # l = 0
        # for r in range(len(s)):
        #     # 1. Add s[r] to the window state
        #     update_state(s[r])
            
        #     # 2. While the window meets the condition
        #     while window_is_valid():
        #         # 3. Update the best result
        #         update_best_result(l, r)
                
        #         # 4. Remove s[l] to shrink the window
        #         remove_from_state(s[l])
        #         l += 1

        heap = []
        for i in range(k - 1):
            heapq.heappush(heap, (-nums[i], i))

        res = []

        l = 0
        for r in range(k - 1, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            while heap and heap[0][1] < l:
                heapq.heappop(heap)
            if heap:
                res.append(-heap[0][0])
            l += 1

        return res