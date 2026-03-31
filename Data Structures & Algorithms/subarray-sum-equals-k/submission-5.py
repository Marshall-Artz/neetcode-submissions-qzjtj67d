class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        prefixSum  = []
        prefixHash = defaultdict(int)
        prefixHash[0] += 1
        count = 0
        for i, num in enumerate(nums):
            s += num
            prefixSum.append(s)
            
            if (s - k) in prefixHash:
                count += prefixHash[(s - k)]
            prefixHash[s] += 1

        return count