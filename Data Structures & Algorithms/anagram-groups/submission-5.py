class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for string in strs:
            charList = [0] * 26
            for char in string:
                i = ord(char) - ord("a")
                charList[i] += 1
            dic[tuple(charList)].append(string)
        
        # ans = [[] for i in range(len(dic))]
        
        # for index, (key, value) in enumerate(dic.items()):
        #     ans[index].append(value)
        
        return list(dic.values())