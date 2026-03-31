class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends: return -1
        if target == "0000": return 0
        
        vis   = set()
        q     = deque(["0000"])
        count = 0

        while q:
            count += 1
            for i in range(len(q)):
                code = q.popleft()

                for i in range(4):
                    newCodeUp = code[:i] + str((int(code[i]) + 1) % 10) + code[i + 1:]
                    newCodeDn = code[:i] + str((int(code[i]) - 1) % 10) + code[i + 1:]
                    if newCodeUp == target or newCodeDn == target:
                        return count
                    if newCodeUp not in deadends and newCodeUp not in vis:
                        q.append(newCodeUp)
                    if newCodeDn not in deadends and newCodeDn not in vis:
                        q.append(newCodeDn)
                    vis.add(newCodeUp)
                    vis.add(newCodeDn)
        
        return -1
            
