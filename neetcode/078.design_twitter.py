"""
Design a simplified version of Twitter where users can 
post tweets, follow/unfollow another user, and is able to see the 
10 most recent tweets in the user's news feed.

Implement the Twitter class:

    - Twitter() Initializes your twitter object.

    - void postTweet(int userId, int tweetId) Composes a new tweet 
        with ID tweetId by the user userId. Each call to this function 
        will be made with a unique tweetId.

    - List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent 
        tweet IDs in the user's news feed. Each item in the news feed must 
        be posted by users who the user followed or by the user themself. 
        Tweets must be ordered from most recent to least recent.

    - void follow(int followerId, int followeeId) The user with ID 
        followerId started following the user with ID followeeId.

    - void unfollow(int followerId, int followeeId) The user with ID 
        followerId started unfollowing the user with ID followeeId.
 
Example 1:

    Input:

        ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", 
        "getNewsFeed", "unfollow", "getNewsFeed"]
        [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

    Output:
    
        [null, null, [5], null, null, [6, 5], null, [5]]
    
    Explanation:

        Twitter twitter = new Twitter();
        twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
        twitter.getNewsFeed(1);  // User 1's news feed should return a list 
        with 1 tweet id -> [5]. return [5]
        twitter.follow(1, 2);    // User 1 follows user 2.
        twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
        twitter.getNewsFeed(1);  // User 1's news feed should return a list 
        with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 
        because it is posted after tweet id 5.
        twitter.unfollow(1, 2);  // User 1 unfollows user 2.
        twitter.getNewsFeed(1);  // User 1's news feed should return a list 
        with 1 tweet id -> [5], since user 1 is no longer following user 2.

Constraints:

    1 <= userId, followerId, followeeId <= 500
    
    0 <= tweetId <= 10^4
    
    All the tweets have unique IDs.
    
    At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow

Takeaway:

    The default thinking just works. Use hashmaps that have values of lists and
        hashmaps that have values of sets.

    Better approach:

    Using defaultdict is nice when you are sure for the 
        type of values of your hashmap

    Using a minheap in this question is especially important 
        for getnewsfeed method. Getting the latest tweets from people that are tweeting
        in their own pace, min_heap helps

"""

class Twitter__:
    # FIRST try
    # does not work
    def __init__(self):
        self.user_follow_dict = {}
        self.user_content = {}
        self.tweet_id = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_content[userId] = self.user_content.get(userId, []) + [tweetId]
        
    def getNewsFeed(self, userId: int) -> "list [int]":
        other_peoples_tweets = []
        for user in self.user_follow_dict:
            other_peoples_tweets += self.user_content[user]
        
        result = other_peoples_tweets + self.user_content[userId] 
        
        return sorted(result)

    def follow(self, followerId: int, followeeId: int) -> None:
        # using the huge dict for every person
        # append to the people who someone is following
        self.user_follow_dict[followeeId] = self.user_follow_dict.get(followeeId, []) \
            [followerId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follow_dict[followeeId] = self.user_follow_dict.get(followeeId, []).remove(followeeId) \
            if self.user_follow_dict[followeeId] else []


from collections import defaultdict
from heapq import heappush, heappop, heapify


class Twitter_:
    # with expert help

    def __init__(self):
        # unique people only
        self.user_follow_dict = defaultdict(set)
        # just a lot of tweets for everyone
        self.user_content = defaultdict(list)
        # starting from 0
        self.time = 0
        # as it is given in question
        self.feed_size = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        # add the tweet to the writers content, as a tuple with id and 
        self.user_content[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int):
        tweets = []
        # all the following and user his/herself
        users = self.user_follow_dict[userId] | {userId}  # Include the user's own tweets
        for user in users:
            # extend all tweets
            tweets.extend(self.user_content[user])
        tweets.sort(key=lambda x: x[0], reverse=True)
        # only return 10 of the tweets, returning only tweetIds also
        return [tweet[1] for tweet in tweets[:self.feed_size]]

    def follow(self, followerId: int, followeeId: int) -> None:
        # add the follower to followee
        self.user_follow_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # edge case
        if followerId != followeeId:  # Ensure a user cannot unfollow themselves
            # remove followeeId from the set
            self.user_follow_dict[followerId].discard(followeeId)

class Twitter:
    
    # This approach starts from methods, not the constructor
    def __init__(self):
        # time
        self.count = 0
        self.tweet_map = defaultdict(list) # userId -> list of [count, tweetIds]
        self.follow_map = defaultdict(set) # userId -> set of followeeId
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        # a hashmap mapping userid to tweet list
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> "list[int]":
        # 10 most recent tweets
        # we cannot just compare tweetId , we also need a time.
        # because person2 might have the latest tweet in Twitter
        # compared to person1, but we might also get some tweets 
        # based on timing, from person1
        res = [] # ordered starting from recent
        min_heap = []

        # add the user themself to the list
        self.follow_map[userId].add(userId)

        for followeeId in self.follow_map[userId]:
            # does this person have at least one tweet
            if followeeId in self.tweet_map:
                # last index of the list
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][index]
                min_heap.append([count, tweetId, followeeId, index - 1])
                
        heapify(min_heap)

        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet_map[followeeId][index]
                heappush(min_heap, [count, tweetId, followeeId, index -1])

        # we will be returning tweetId's
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # we can use a hashmap that holds a list for each user - o(1)
        # But removing the people from this list would be o(n)
        # is there a more efficient way? 
        # dict(set) - which will be o(1) insert and delete
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
