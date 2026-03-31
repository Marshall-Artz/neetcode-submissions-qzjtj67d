class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            string = "".join(sorted(s))
            dic[string].append(s)

        ans = [[] for i in range(len(dic))]

        i = 0
        for key, value in dic.items():
            for string in value:
                ans[i].append(string)
            i += 1
        
        return ans