class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        groupCount = len(hand) // groupSize

        counter = Counter(hand)
        heapq.heapify(hand)


        while groupCount != 0:
            if counter[hand[0]] != 0:
                start = hand[0]
                for i in range(start, start + groupSize):
                    if i not in counter or counter[i] == 0:
                        return False
                    counter[i] -= 1
                groupCount -= 1
            else:
                heapq.heappop(hand)


        return True