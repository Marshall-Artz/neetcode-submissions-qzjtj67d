class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1
        
        heap = []
        for key, value in dic.items():
            heapq.heappush(heap, [-value, key])
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans

        # nums = [1,2,2,3,3,3], k = 2
        # dic = {
        #     1: 1,
        #     2: 2,
        #     3: 3
        # }
        # heap = [
        #     [-1, 1],
        #     [-2, 2],
        #     [-3, 3]
        # ]
        # ans = [3, 2]