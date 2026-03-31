class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        st = set()
        ans = []
        
        for i, num in enumerate(nums):
            dic[num] = i

        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                diff = (nums[i] + nums[j]) * -1
                if diff in dic.keys() and dic[diff] != i and dic[diff] != j:
                    localLst = [nums[i], nums[j], diff]
                    localLst.sort()
                    localTup = (localLst[0], localLst[1], localLst[2])
                    st.add(localTup)

        for tup in st:
            ans.append(tup)

        return ans
