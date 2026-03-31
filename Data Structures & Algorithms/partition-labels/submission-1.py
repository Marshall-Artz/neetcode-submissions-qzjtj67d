class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        ans = []

        for i, char in enumerate(s):
            dic[char] = i

        size = end = 0
        for i, char in enumerate(s):
            end = max(end, dic[char])
            size += 1
            if i == end:
                ans.append(size)
                size = 0
        
        return ans