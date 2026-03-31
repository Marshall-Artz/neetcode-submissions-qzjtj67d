class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            currChar = s[i]
            nextChar = s[i+1]
            score += abs(ord(currChar) - ord(nextChar))
        return score