class TimeMap:


    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        print("SET - key:", key, " value:", value, " timestamp:", timestamp)
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        print("GET - key:", key, " timestamp:", timestamp)
        print(self.dic)

        if len(self.dic[key]) == 0:
            return ""

        top = len(self.dic[key]) - 1
        bot = 0
        res = 0
        
        while bot < top:
            mid = (top + bot) // 2
            print("bot:", bot, " mid:", mid, " top:", top)
            if self.dic[key][mid][0] == timestamp:
                return self.dic[key][mid][1]
            elif self.dic[key][mid][0] < timestamp:
                bot = mid + 1
            elif self.dic[key][mid][0] > timestamp:
                top = mid - 1
            res = mid
        
        print("final... bot:", bot, " mid:", res, " top:", top)

        if self.dic[key][res]:
            print("mid value:", self.dic[key][res])
        else:
            print("no mid value")

        if self.dic[key][bot][0] > timestamp and bot - 1 < 0:
            return ""
        elif self.dic[key][bot][0] > timestamp and bot - 1 >= 0:
            return self.dic[key][bot - 1][1]

        return self.dic[key][bot][1]
        
