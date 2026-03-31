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
        res = ""
        
        while bot <= top:
            mid = (top + bot) // 2
            if self.dic[key][mid][0] == timestamp:
                return self.dic[key][mid][1]
            elif self.dic[key][mid][0] < timestamp:
                bot = mid + 1
                res = self.dic[key][mid][1]
            elif self.dic[key][mid][0] > timestamp:
                top = mid - 1

        return res
        
