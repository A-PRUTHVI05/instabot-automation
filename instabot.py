# import pip install instabot

from instabot import Bot
bot=Bot() #create variable and run function Bot
bot.login(username=" ",password=" ")

# bot.follow(" ")  #for follow account

# bot.unfollow(" ")  #for unfollow account

# bot.upload_photo("", caption=" ") #give path  ///

# bot.send_message("I Love Python",["name of person"])

# followers=bot.get_user_follower("user name") #follower list
# for Follower in followers:
#     print(bot.get_user_info(follower))

# following=bot.get_user_following("user name") #Following list
# for Following in following:
#     print(bot.get_user_info(Following))
