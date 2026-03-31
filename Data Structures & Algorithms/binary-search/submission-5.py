class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0;
        r = len(nums) - 1

        while True:
            print("l:", l, " r:", r)
            if l == r and nums[l] == target:
                return l
            elif l == r and nums[l] != target:
                return -1

            middle = int(((r - l) / 2) + l)

            if nums[middle] > target:
                r = middle
            elif nums[middle] < target:
                l = middle + 1
            else:
                return middle


