# [ Name: Design Twitter ]  [ Category: design ]  [ Topic: design ]  [ Weight: 7 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/design-twitter/ ]

"""
Design a simplified Twitter where users can post tweets, follow/unfollow others, and read the 10 most recent tweets from themselves and users they follow. 
Implement methods: postTweet(userId, tweetId), getNewsFeed(userId), follow(followerId, followeeId), and unfollow(followerId, followeeId).
1 <= userId, followerId, followeeId, tweetId <= 500
getNewsFeed returns up to 10 tweetIds, most recent first.
Example: After user 1 posts 5 tweets and follows user 2, getNewsFeed(1) returns user 1 and 2's latest tweets.
"""

from typing import List

class Twitter:
    def __init__(self):
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        pass

    def getNewsFeed(self, userId: int) -> List[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass

if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6,5]
    twitter.unfollow(1,2)
    assert twitter.getNewsFeed(1) == [5]
    twitter.postTweet(1, 7)
    assert twitter.getNewsFeed(1) == [7,5]
    twitter.postTweet(2, 8)
    twitter.follow(1,2)
    assert twitter.getNewsFeed(1) == [8,7,5]
    twitter.postTweet(2, 9)
    twitter.postTweet(2, 10)
    assert twitter.getNewsFeed(1) == [10,9,8,7,5]
    twitter.unfollow(1,2)
    assert twitter.getNewsFeed(1) == [7,5]