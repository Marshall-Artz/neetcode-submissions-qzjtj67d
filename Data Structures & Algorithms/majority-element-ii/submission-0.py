class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        res = []

        for num in nums:
            dic[num] += 1
        
        for key, val in dic.items():
            if val > len(nums) / 3:
                res.append(key)
        
        return res