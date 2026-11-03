class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1
        
        arr = [[] for _ in range(len(nums))]

        for key, value in dic.items():
            arr[value - 1].append(key)
        
        res = []

        for lst in reversed(arr):
            while lst:
                res.append(lst.pop())
            
                if len(res) == k:
                    return res
        
        return res