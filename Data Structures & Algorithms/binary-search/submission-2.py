class Solution:
    def search(self, nums: List[int], target: int) -> int:
        offset = 0

        while True:
            if len(nums) == 1 and nums[0] != target:
                return -1

            curr = int(len(nums) / 2)

            if target < nums[curr]:
                nums = nums[:curr]
            elif target > nums[curr]:
                offset += curr
                nums = nums[curr:]
            else:
                return offset + curr
