class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        isTrusted = set()
        for i in range(1, n+1):
            isTrusted.add(i)
        
        trusts = defaultdict(list)
        
        print(isTrusted)
        print(trusts)

        for pers, whoTrusts in trust:
            if pers in isTrusted:
                isTrusted.remove(pers)
            trusts[whoTrusts].append(pers)
            
        print(isTrusted)
        print(trusts)

        for pers in isTrusted:
            if len(trusts[pers]) == n - 1:
                return pers

        return -1