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
        printTweet("%s_%s_%s.json" %
                   (team_name, time_since, time_until), tweet, lang=lang)


getTweets()
