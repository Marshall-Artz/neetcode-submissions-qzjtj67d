class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        prefixSum  = []
        prefixHash = defaultdict(list)
        prefixHash[0].append(-1)
        for i, num in enumerate(nums):
            s += num
            prefixSum.append(s)
            prefixHash[s].append(i)
        
        print(prefixSum)
        print(prefixHash)
        
        count = 0
        for i, sm in enumerate(prefixSum):
            if (sm - k) in prefixHash:
                for index in prefixHash[sm - k]:
                    if index < i:
                        count += 1

        return count