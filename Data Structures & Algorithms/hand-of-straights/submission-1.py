class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        group = []


        while hand:
            subgroup = deque([hand.pop()])
            if len(subgroup) < groupSize:
                for i in range(len(hand) - 1, -1, -1):
                    if hand[i] == (subgroup[0] - 1):
                        subgroup.appendleft(hand.pop(i))
                    if len(subgroup) == groupSize:
                        break
            if len(subgroup) != groupSize:
                return False
            group.append(subgroup.copy())
        

        return True