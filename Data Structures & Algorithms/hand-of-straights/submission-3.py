class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        groupCount = len(hand) // groupSize

        counter = Counter(hand)
        heapq.heapify(hand)

        while groupCount != 0:
            start = heapq.heappop(hand)
            if counter[start] != 0:
                for i in range(start, start + groupSize):
                    if counter[i] == 0:
                        return False
                    counter[i] -= 1
                groupCount -= 1

        return True