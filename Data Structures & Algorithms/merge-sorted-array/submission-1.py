class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        heapq.heapify(nums2)

        for i in range(len(nums1) - n):
            heapq.heappush(nums2, nums1[i])
            nums1[i] = heapq.heappop(nums2)

        for i in range(n):
            nums1[m + i] = heapq.heappop(nums2)

        # nums1  = [1,2,10, 20,20,40]
        # nums2  = [10,20]
