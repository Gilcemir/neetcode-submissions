import itertools
class Twitter:

    def __init__(self):
        # user_d : {tweetId: int, timestamp: int}
        self.ps: dict[int, deque[dict]] = {} # posts
        self.rs: dict[int, set[int]] = {} # relations
        # next(self.counter)
        self.counter = itertools.count()
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.ps:
            self.ps[userId] = deque()
            # - next porque é descendente
        self.ps[userId].appendleft({"tweetId": tweetId, "timestamp": -next(self.counter)})
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        # adiciona primeiro feed dos follows
        users = self.rs[userId] if userId in self.rs else set()
        users.add(userId) # remove dependencia circular via set (seguir vc mesmo)
        h = []
        for user in users:
            if user in self.ps:
                h.append((self.ps[user][0]["timestamp"], user, 0))

        heapq.heapify(h)

        while h and len(res) < 10:
            _, uId, cursor = heapq.heappop(h)
            tweet = self.ps[uId][cursor]["tweetId"]
            res.append(tweet)
            cursor += 1
            if cursor < len(self.ps[uId]):
                heapq.heappush(h, (self.ps[uId][cursor]["timestamp"], uId, cursor))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.rs:
            self.rs[followerId] = set()
        self.rs[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.rs:
            return
        self.rs[followerId].discard(followeeId)