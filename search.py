import got3 as got
import json


def printTweet(filename, t, lang='en'):
    t_dict = {}
    if t.language == lang:
        t_dict['id'] = t.id
        t_dict['date'] = t.formatted_date
        t_dict['username'] = t.username
        t_dict['retweets'] = t.retweets
        t_dict['favorites'] = t.favorites
        t_dict['text'] = t.text
        t_dict['language'] = t.language
        t_dict['mentions'] = t.mentions
        t_dict['hashtags'] = t.hashtags
        with open(filename, 'a') as f:
            f.write(json.dumps(t_dict))
            f.write('\n')


def getTweets(team_name="nyxl", time_since="2019-02-15", time_until="2019-02-16", lang='en'):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(
        team_name).setSince(time_since).setUntil(time_until)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for tweet in tweets:
        printTweet("data/%s_%s_%s.json" %
                   (team_name, time_since, time_until), tweet, lang=lang)


time_stage1 = [
    ["2019-02-14", "2019-02-19"],
    ["2019-02-21", "2019-02-26"],
    ["2019-02-28", "2019-03-05"],
    ["2019-03-07", "2019-03-12"],
    ["2019-03-16", "2019-03-19"],
    ["2019-03-21", "2019-03-23"]
]
time_stage2 = [
    ["2019-04-04", "2019-04-09"],
    ["2019-04-11", "2019-04-16"],
    ["2019-04-18", "2019-04-21"],
]
stages = [time_stage1, time_stage2]
teams = ["Atlanta Reign", "Boston Uprising",
         "Florida Mayhem", "Houston Outlaws",
         "London Spitfire", "NYXL",
         "Paris Eternal", "Philadelphia Fusion",
         "Toronto Defiant", "Washington Justice", "Chengdu Hunters", "Dallas Fuel",
         "Guangzhou Charge", "Hangzhou Spark",
         "Los Angeles Gladiators", "Los Angeles Valiant",
         "SFShock", "Seoul Dynasty",
         "Shanghai Dragons", "Vancouver Titans"]

for team in teams:
    print("Crawling teams: ", team)
    for i, time_stage in enumerate(stages):
        print("  Stage: ", (i+1))
        for week, date in enumerate(time_stage):
            print("    Week: ", (week+1))
            getTweets(team_name=team, time_since=date[0], time_until=date[1])
