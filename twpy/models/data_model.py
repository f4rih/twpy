from typing import Union


class FF:
    def __init__(self, username: str, avatar: str, fullname: str) -> None:
        """Data model for followers/followings
        
        Arguments:
            username {str} -- [description]
            user_id {int} -- [description]
            avatar {str} -- [description]
            fullname {str} -- [description]
        """
        self.username = username
        self.avatar = avatar
        self.fullname = fullname


class Timeline:
    def __init__(self, tweet_id: int,
                 tweet_link: str,
                 conversation_id: str,
                 is_reply: str,
                 has_parent: str,
                 screen_name: str,
                 name: str,
                 user_id: str,
                 user_mentions: Union[str, list],
                 content: str,
                 reply_count: int,
                 retweet_count: int,
                 likes_count: int,
                 created_at: str) -> None:
        """

        :param tweet_id:
        :param tweet_link:
        :param conversation_id:
        :param is_reply:
        :param has_parent:
        :param screen_name:
        :param name:
        :param user_id:
        :param user_mentions:
        :param content:
        :param reply_count:
        :param retweet_count:
        :param likes_count:

        """
        self.tweet_id = tweet_id
        self.tweet_link = tweet_link
        self.conversation_id = conversation_id
        self.is_reply = is_reply
        self.has_parent = has_parent
        self.screen_name = screen_name
        self.name = name
        self.user_id = user_id
        self.user_mentions = user_mentions
        self.content = content
        self.reply_count = reply_count
        self.retweet_count = retweet_count
        self.likes_count = likes_count
        self.created_at = created_at


class Profile:
    def __init__(self, name: str,
                 verified: str,
                 protected: str,
                 username: str,
                 bio: str,
                 location: str,
                 url: str,
                 tweet_count: int,
                 following_count: int,
                 follower_count: int) -> None:
        """
        User profile data model
        """
        self.name = name
        self.verified = verified
        self.protected = protected
        self.username = username
        self.bio = bio
        self.location = location
        self.url = url
        self.tweet_count = tweet_count
        self.following_count = following_count
        self.follower_count = follower_count
