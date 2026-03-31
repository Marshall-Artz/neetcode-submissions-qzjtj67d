class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)

        for char in s:
            dic1[char] += 1
        
        for char in t:
            dic2[char] += 1
        
        if (dic1 == dic2):
            return True
        else:
            return False