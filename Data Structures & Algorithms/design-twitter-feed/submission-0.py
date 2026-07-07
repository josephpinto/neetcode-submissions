import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.followingByUserId = defaultdict(set)
        self.tweetsByUserId = defaultdict(list)
        self.tweetCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetsByUserId[userId].append((self.tweetCount, tweetId))
        self.tweetCount -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        res = []
        total_followers = self.followingByUserId[userId].copy()
        total_followers.add(userId)
        for follower in total_followers:
            if self.tweetsByUserId[follower]:
                
                count, tweetId = self.tweetsByUserId[follower][-1]
                heapq.heappush(min_heap, (count, tweetId, follower,len(self.tweetsByUserId[follower])-2))
        while min_heap and len(res) < 10:
            count, tweetId, follower,index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >=0:
                count, tweetId = self.tweetsByUserId[follower][index]
                heapq.heappush(min_heap, (count, tweetId, follower,index-1))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingByUserId[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followingByUserId[followerId].discard(followeeId)

        
