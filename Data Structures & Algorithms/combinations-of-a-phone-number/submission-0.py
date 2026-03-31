class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        i   = 0

        if not digits:
            return []

        def getLetters(num: int) -> list:
            if   num == '1': return []
            elif num == '2': return ['a', 'b', 'c']
            elif num == '3': return ['d', 'e', 'f']
            elif num == '4': return ['g', 'h', 'i']
            elif num == '5': return ['j', 'k', 'l']
            elif num == '6': return ['m', 'n', 'o']
            elif num == '7': return ['p', 'q', 'r', 's']
            elif num == '8': return ['t', 'u', 'v']
            elif num == '9': return ['w', 'x', 'y', 'z']

        def dfs(i: int, s: str):
            # Base case handling:
            if i >= len(digits):
                res.append(s)
                return

            # Loop for each potential letter:
            letters = getLetters(digits[i])
            for char in letters:
                dfs(i+1, s + char)


        dfs(0, "")
        return res