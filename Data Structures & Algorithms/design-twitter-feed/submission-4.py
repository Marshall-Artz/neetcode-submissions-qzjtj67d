class Twitter:

    def __init__(self):
        self.timer = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.timer, tweetId])
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []

        # Get current user tweets as well
        tweets.extend(self.tweets[userId])
        
        for userFollowing in self.following[userId]:
            if userFollowing != userId:
                tweets.extend(self.tweets[userFollowing])
        
        return [tweet[1] for tweet in heapq.nlargest(10, tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
