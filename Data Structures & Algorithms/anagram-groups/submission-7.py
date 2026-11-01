class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for string in strs:
            lst = [0] * 26

            for char in string:
                index = ord(char.lower()) - ord("a")
                lst[index] += 1
            
            dic[tuple(lst)].append(string)
        
        return list(dic.values())