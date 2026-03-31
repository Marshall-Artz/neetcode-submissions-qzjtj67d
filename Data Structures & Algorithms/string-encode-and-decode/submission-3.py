class Solution:

    def encode(self, strs: List[str]) -> str:
        ecdStr = ""
        ecdRes = ""
        charCount = 0

        for s in strs:
            ecdStr = str(len(s)) + "#" + s
            ecdRes += ecdStr

        print(ecdRes)

        return ecdRes

    def decode(self, s: str) -> List[str]:
        dcdLst = []
        offset = ""
        i      = 0

        while i < len(s):
            if s[i] == "#":
                substr = s[i+1:i+1+int(offset)]
                dcdLst.append(substr)
                i += 1 + int(offset)
                offset = ""
                print(substr)
            else:
                print(s[i])
                offset += s[i]
                i += 1

        return dcdLst