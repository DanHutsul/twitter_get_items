import tweepy
import pandas as pd
import json

def main():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("ZxDwkJ0fHdqxc7Irljy82emIQ", "9NuxQMVXgOdQbo28sqOc25GhXgLr8OTrxCFE9iphwZlirRBDdN")
    auth.set_access_token("1161015575512064000-9bJgvnlgNTzx0IAudrdtT8SvgBXGvZ", "2vIYX8HLBg5uWXLREfgodKWQBT88aHgxTmFaL5JvDIv03")

    # Create API object
    api = tweepy.API(auth)
    name = "realDonaldTrump"
    user = api.get_user(screen_name = name)
    data = json.loads(json.dumps(user._json))
    value = input("Input the name of object that you are looking for: ")
    print(iterator(data, value))

def iterator(item, value):
    for i in item:
        if type(i) == dict:
            iterator(i, value)
        elif str(i) == value:
            return str("Found!\n" + str(value) + " : " + str(item[i]))

if __name__ == "__main__":
    main()