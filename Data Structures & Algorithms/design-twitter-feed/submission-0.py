from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        # use dictionary, key: userID, value: set of following
        # dictionary, key: user, value: list containing (time, tweetId)
        self.time = 0
        self.following = defaultdict(set) # {userID: {1, 2, 3}}
        self.tweets = defaultdict(list) # {userID: [(time, tweetId)]}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId} # all users
        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]
                heapq.heappush(heap, (-time, uid, index))
        answer = []
        while heap and len(answer) < 10:
            neg_time, uid, index = heapq.heappop(heap)
            answer.append(self.tweets[uid][index][1]) # get tweetId
            if index > 0:
                next_time, next_tweet_id = self.tweets[uid][index - 1]
                heapq.heappush(heap,(-next_time, uid, index - 1))
        return answer


    def follow(self, followerId: int, followeeId: int) -> None:
        # no need to check if key is alr in dict bc of defaultdict
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
