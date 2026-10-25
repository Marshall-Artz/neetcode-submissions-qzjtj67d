class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDic = defaultdict(int)
        tDic = defaultdict(int)

        for char in s:
            sDic[char] += 1
        for char in t:
            tDic[char] += 1
        
        return sDic == tDic

        # s = "racecar", t = "carrace"
        # sDic = {
        #     a: 2
        #     c: 2
        #     e: 1
        #     r: 2
        # }
        # tDic = {
        #     a: 2
        #     c: 2
        #     e: 1
        #     r: 2
        # }