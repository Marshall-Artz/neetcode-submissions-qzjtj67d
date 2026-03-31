class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        ans = []

        for i, char in enumerate(s):
            dic[char] = i

        start = end = 0
        for i, char in enumerate(s):
            end = max(end, dic[char])
            if i == end:
                ans.append(i - start + 1)
                start = i + 1
        
        return ans