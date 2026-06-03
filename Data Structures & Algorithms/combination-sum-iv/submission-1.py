class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        mem = {}
        def dfs(value: int) -> int:
            nonlocal mem
            if value in mem:
                return mem[value]
            if value <= 0:
                if value == 0:
                    return 1
                else:
                    return 0
            
            count = 0
            for num in nums:
                count += dfs(value - num)
            
            mem[value] = count
            return mem[value]
        
        return dfs(target)

        # nums = [3,1,2]
        # target = 4

        # value = 4
        #     # Subtract 3
        #     value = 1
        #         # Subtract 3
        #         value = -2 # Finish
        #         # Subtract 1
        #         value = 2
        #             # Subtract 3
        #             value = -1 # Finish
        #             # Subtract 1
        #             value = 1
        #                 # Subtract 3
        #                 value = -2 # Finish
        #                 # Subtract 1
        #                 value = 0 # Finish
        #                 # Subtract 2
        #                 value = -1 # Finish
        #             # Subtract 2
        #             value = 0 # Finish
        #         # Subtract 2
        #         value = -1
        #     # Subtract 1
        #     value = 3
        #         # Subtract 3
        #         value = 0 # Finish
        #         # Subtract 1
        #         value = 2
        #             # Subtract 3
        #             value = -1 # Finish
        #             # Subtract 1
        #             value = 1
        #                 # Subtract 3
        #                 value = -2 # Finish
        #                 # Subtract 1
        #                 value = 0 # Finish
        #                 # Subtract 2
        #                 value = -1 # Finish
        #             # Subtract 2
        #             value = 0 # Finish
        #         # Subtract 2
        #         value = 1
        #             # Subtract 3
        #             value = -2 # Finish
        #             # Subtract 1
        #             value = 0 # Finish
        #             # Subtract 2
        #             value = -1 # Finish
        #     # Subtract 2
        #     value = 2
        #         # Subtract 3
        #         value = -1 # Finish
        #         # Subtract 1
        #         value = 1
        #             # Subtract 3
        #             value = -2 # Finish
        #             # Subtract 1
        #             value = 0 # Finish
        #             # Subtract 2
        #             value = -1 # Finish
        #         # Subtract 2
        #         value = 0 # Finish

        # nums = [3,1,2]
        # target = 4

        # i, value = 0, 0
        #     i, value = 1, 3 # Include
        #         i, value = 2, 4 # Include
        #             i, value = 3, 6 # Final
        #         i, value = 2, 3 # Exclude
        #             i, value = 3, 3
        #     i, value = 1, 0 # Exclude
        #         i, value = 2, 1 # Include
        #             i, value = 3, 3 # Include
        #             i, value = 3, 1 # Exclude
        #         i, value = 2, 0 # Exclude
        #             i, value = 3, 2 # Include
        #             i, value 3, 0 # Exclude
