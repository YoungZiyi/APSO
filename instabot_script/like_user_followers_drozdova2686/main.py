"""
    instabot example

    Workflow:
        Like user's, follower's media by user_id.
"""

import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
parser.add_argument('users', type=str, nargs='+', help='users')
args = parser.parse_args()

bot = Bot(max_following_to_followers_ratio=10000,
        max_followers_to_following_ratio=10000,
        max_following_to_follow=10000000)
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)

my_follower_list = bot.get_user_following(args.u)

for username in args.users:
    follower_list = bot.get_user_followers(username)
    for follower in follower_list:
        if follower not in my_follower_list:
            bot.follow(follower)
        medias = bot.get_user_medias(follower, False)
        if not medias:
            continue
        bot.like_medias(medias[:1], False)
