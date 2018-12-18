import datetime
import requests
import tweepy
import os
import config
# apiを取得
auth = tweepy.OAuthHandler(config.getConsumerKey(), config.getConsumerSecret())
auth.set_access_token(config.getAccessToken(), config.getAccessSecret())
api = tweepy.API(auth)

# 検索キーワードを設定する。
# searchWord = "大阪桐蔭" #検索ワード１つ
searchWord = ["池袋", "たまごけん"]  # 検索ワード複数

# twitter内を検索する
# qに検索したいワードを指定する。
for status in api.search(q=searchWord, lang='ja', result_type='recent', count=7):
    print("ユーザーID:" + status.user.name)  # userIDを表示
    print("ユーザー名:" + status.user.screen_name)  # ユーザー名を表示
    time = status.created_at + datetime.timedelta(hours=9)
    print("投稿日時:" + str(status.created_at +
                        datetime.timedelta(hours=30)))  # 投稿日時を表示
    print(status.text)  # ツイートを表示
    print()
