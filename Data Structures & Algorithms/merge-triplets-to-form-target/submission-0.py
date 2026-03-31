class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        solutions = []
        for triplet in triplets:
            if (triplet[0] <= target[0] and
                triplet[1] <= target[1] and
                triplet[2] <= target[2]):
                solutions.append(triplet)
        
        x = y = z = False
        for triplet in solutions:
            if triplet[0] == target[0]: x = True
            if triplet[1] == target[1]: y = True
            if triplet[2] == target[2]: z = True
        
        if x and y and z:
            return True
        
        return False