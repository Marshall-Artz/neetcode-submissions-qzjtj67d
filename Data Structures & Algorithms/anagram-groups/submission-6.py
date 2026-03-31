class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        res = []

        for s in strs:
            sub = [0] * 26
            for char in s:
                sub[ord(char) - ord('a')] += 1
            dic[tuple(sub)].append(s)

        for lst in dic.values():
            res.append(lst)

        return res