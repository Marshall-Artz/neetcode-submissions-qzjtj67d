class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(int)
        trusts  = defaultdict(int)

        for person, whoTheyTrust in trust:
            trusts[person] += 1
            trusted[whoTheyTrust] += 1
        
        for i in range(1, n + 1):
            if (trusts[i] == 0 and 
                trusted[i] == n - 1):
                return i
        
        return -1
             