class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(nums1) <= len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1

        l1, r1 = 0, len(A)
        l2, r2 = 0, len(B) - 1

        # Pt1 get the windows
        while True:
            # Cut partitions
            mid1 = (l1 + r1) // 2
            mid2 = half - mid1
            print("mid1:", mid1, " mid2:", mid2)

            Aleft = A[mid1 - 1] if mid1 > 0 else -float('inf')
            Aright = A[mid1] if mid1 < len(A) else float('inf')
            Bleft = B[mid2 - 1] if mid2 > 0 else -float('inf')
            Bright = B[mid2] if mid2 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                break
            
            if Aleft > Bright:
                r1 = mid1 - 1
            elif Bleft > Aright:
                l1 = mid1 + 1

        # Pt2 return / calc the median
        if total % 2 == 0:
            median = (min(Aright, Bright) + max(Aleft, Bleft)) / 2
        else:
            median = min(Aright, Bright)
        
        return median