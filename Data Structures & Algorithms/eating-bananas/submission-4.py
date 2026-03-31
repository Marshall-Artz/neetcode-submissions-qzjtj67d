class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bot = 0
        top = max(piles) + 1
        res = []

        piles.sort()
        
        while top - bot > 1:
            mid = (top + bot) // 2
            tot = 0

            # Check value for mid:
            for pile in piles:
                tot += math.ceil(pile / mid)
            
            if tot > h:
                bot = mid
            else:
                res.append(mid)
                top = mid

        return res[-1]