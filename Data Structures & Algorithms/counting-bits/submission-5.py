class Solution:
    def countBits(self, n: int) -> List[int]:
        dic = {0: 0}
        res = [0]
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dic[i] = 1 + dic[i - offset]
            res.append(dic[i])
        
        return res