class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sDic = defaultdict(int)
        tDic = defaultdict(int)

        for i in range(len(s)):
            sChar, tChar = s[i], t[i]

            sDic[sChar] += 1
            tDic[tChar] += 1
        
        return True if sDic == tDic else False 