class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        mem = {}
        def isInterleaved(pos1: int, pos2: int, pos3: int) -> bool:
            if (pos1, pos2) in mem:
                return mem[(pos1, pos2)]
            if pos3 == len(s3):
                return True if pos1 == len(s1) and pos2 == len(s2) else False
            
            res = False
            if pos1 < len(s1) and s1[pos1] == s3[pos3]:
                res = res or isInterleaved(pos1 + 1, pos2, pos3 + 1)
            if pos2 < len(s2) and s2[pos2] == s3[pos3]:
                res = res or isInterleaved(pos1, pos2 + 1, pos3 + 1)
            
            mem[(pos1, pos2)] = res
            return res

        
        return isInterleaved(0, 0, 0)