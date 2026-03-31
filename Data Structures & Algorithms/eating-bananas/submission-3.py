class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bot = 0
        top = max(piles) + 1
        res = []

        piles.sort()
        z = 0
        while top - bot > 1:
            mid = (top + bot) // 2
            tot = 0

            # Check value for mid:
            for pile in piles:
                tot += math.ceil(pile / mid)
            
            print(piles)
            print(res)
            print("mid:", mid, " tot:", tot)
            if tot > h:
                print("bottom moved up")
                bot = mid
            else:
                print("top moved down")
                res.append(mid)
                top = mid

        return res[-1]