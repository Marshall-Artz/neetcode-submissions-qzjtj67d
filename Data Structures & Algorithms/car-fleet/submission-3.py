class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        stack = [[p, s] for p, s in zip(positions, speeds)]
        stack.sort(reverse=True)
        times = []

        for pair in stack:
            timeToTarget = (target - pair[0]) / pair[1]
            times.append(timeToTarget)
            if len(times) >= 2 and times[-1] <= times[-2]:
                times.pop()

        return len(times)

        