class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        i   = 0

        if not digits:
            return []

        # Mapping to get characters
        getLetters = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def dfs(i: int, s: str):
            # Base case handling:
            if i >= len(digits):
                res.append(s)
                return

            # Loop for each potential letter:
            for char in getLetters[digits[i]]:
                dfs(i+1, s + char)


        dfs(0, "")
        return res