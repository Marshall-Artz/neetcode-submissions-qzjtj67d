class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False

        seen = {}
        for i, num in enumerate(nums):
            if num in seen and abs(seen[num] - i) <= k:
                return True
            seen[num] = i
        
        return False