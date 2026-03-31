class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i, num in enumerate(arr):
            if i+1 >= len(arr):
                break
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr