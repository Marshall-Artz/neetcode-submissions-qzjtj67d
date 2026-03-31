class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary1 = {}
        dictionary2 = {}

        for char in s:
            dictionary1[char] = 0
        for char in s:
            dictionary1[char] += 1
        
        for char in t:
            dictionary2[char] = 0
        for char in t:
            dictionary2[char] += 1
        
        if (dictionary1 == dictionary2):
            return True
        else:
            return False