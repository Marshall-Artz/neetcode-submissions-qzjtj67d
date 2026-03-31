class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            frontIndex = i
            backIndex  = len(s) - i - 1

            temp = s[frontIndex]
            s[frontIndex] = s[backIndex]
            s[backIndex] = temp