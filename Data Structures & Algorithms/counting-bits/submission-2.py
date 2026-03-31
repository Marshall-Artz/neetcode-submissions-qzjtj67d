class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            count = 0
            var   = i
            while var:
                if (var & 1):
                    count += 1
                var = var >> 1
            res.append(count)
        
        return res