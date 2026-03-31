class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixHash = defaultdict(int)
        prefixHash[0] += 1
        res, currSum = 0, 0

        for num in nums:
            currSum += num
            diff = currSum - k
            
            res += prefixHash[diff]
            prefixHash[currSum] += 1

        return res