class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s)) + "#" + s

        return enc

    def decode(self, s: str) -> List[str]:
        dec = []


        i = 0
        while i < len(s):
            j = s.find("#", i)
            l = int(s[i:j])

            dec.append(s[j + 1:j + 1 + l])
            i = j + 1 + l


        return dec