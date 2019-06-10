from instabot import Bot

bot = Bot(
        filter_verified_accounts=False,
        max_followers_to_follow=10000000000,
        max_followers_to_following_ratio=10000000000,
        min_following_to_follow=0)
bot.login()
print("\n>>>>>>>>>>>>>>>>>>>>\n")
ret = bot.follow('drozdova2686')
print("\n>>>>>>>>>>>>>>>>>>>>\n")
print(ret)
