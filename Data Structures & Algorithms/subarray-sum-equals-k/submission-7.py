class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] += 1

        currSum, count = 0, 0
        for num in nums:
            currSum += num
            diff     = currSum - k

            if diff in prefixSum:
                count += prefixSum[diff]
            prefixSum[currSum] += 1
        
        return count