class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 1:
            return arr if k == 1 else []
        
        if x < arr[0]:
            return arr[:k]
        elif x > arr[-1]:
            return arr[-k:]

        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid

        l -= 1
        print(arr[l], arr[r])

        res = deque([])
        i = 0
        while len(res) < k:
            print(l, arr[l], r, arr[r])
            if l < 0:
                res.append(arr[r])
                r += 1
            elif r > len(arr) - 1:
                res.appendleft(arr[l])
                l -= 1
            elif abs(x - arr[l]) <= abs(x - arr[r]):
                res.appendleft(arr[l])
                l -= 1
            elif abs(x - arr[l]) > abs(x - arr[r]):
                res.append(arr[r])
                r += 1
        
        return list(res)

