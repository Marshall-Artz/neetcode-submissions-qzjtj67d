class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        pos = len(nums1) - 1
        p1  = m - 1
        p2  = n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 < 0:
                while p2 >= 0:
                    nums1[pos] = nums2[p2]
                    p2 -= 1
                    pos -= 1
                break
            if p2 < 0:
                while p1 >= 0:
                    nums1[pos] = nums1[p1]
                    p1 -= 1
                    pos -= 1
                break

            if nums1[p1] >= nums2[p2]:
                nums1[pos] = nums1[p1]
                p1 -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[pos] = nums2[p2]
                p2 -= 1

            pos -= 1
