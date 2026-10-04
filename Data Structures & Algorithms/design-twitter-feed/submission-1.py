class Twitter:

    def __init__(self):
        self.tweetsByUser = defaultdict(list)
        self.followedByUser = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetsByUser[userId].append((self.count,tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        all_followed = self.followedByUser[userId].copy()
        all_followed.add(userId)
        for followee in all_followed:
            if self.tweetsByUser[followee]:
                count, tweetId = self.tweetsByUser[followee][-1]
                heapq.heappush(heap,(count,tweetId,followee,len(self.tweetsByUser[followee])-1))
        while heap and len(res) < 10:
            count,tweetId,followee,idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx>0:
                new_count, new_tweetId = self.tweetsByUser[followee][idx-1]
                heapq.heappush(heap,(new_count,new_tweetId,followee,idx-1))
        return res



        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followedByUser[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followedByUser[followerId]:
            self.followedByUser[followerId].remove(followeeId)
