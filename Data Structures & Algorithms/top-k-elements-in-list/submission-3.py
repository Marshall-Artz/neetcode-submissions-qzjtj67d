class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        tupList = []
        ans = []

        for key, value in dic.items():
            tupList.append((value, key))

        tupList.sort(reverse = True)
        print(tupList)
        
        for i in range(k):
            ans.append(tupList[i][1])

        return ans