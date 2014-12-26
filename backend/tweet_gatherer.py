import tweepy
from app import db, Tweet
from sickness_classifier_defines import generateNgramModel, sicknessClassifier
import time
from sqlalchemy import literal

def gather_sick_tweets(search_terms, since_field=None, until_field=None):
    
    consumer_key = 'PIAQQFVJF7DB2JlrOwgUt7sXn'
    consumer_secret = 'BqqjbSFpZZ33dSQ1JHMiF0DmySUS3dFjQS73zMcjhs97uq1QDR'
    auth_key = '2293938194-pkUSFXrOhiOuU7DwBCAbBY7QGzsfqmYagCRMSKU'
    auth_secret = 'XiLUctGAZIr5hnGiHbwZoXymxseTWxSi1VfkrGRsd4EII'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(auth_key, auth_secret)
    
    api = tweepy.API(auth)
    
    healthyNgramModel = generateNgramModel('corpora/','healthy_tweets.txt')
    sickNgramModel = generateNgramModel('corpora/','sick_tweets.txt')
    
    
    for search in search_terms:
        if since_field is not None and until_field is not None:
            c = tweepy.Cursor(api.search, q=search, include_entities=True, lang='en', since=since_field, until=until_field ).items()
            print "finding tweets between " + since_field + " until " + until_field
        else:
            print "no since and until_fields given"
            c = tweepy.Cursor(api.search, q=search, include_entities=True, lang='en', wait_on_rate_limit=True, result_type="recent").items()
        iterator = 20
        while True:
            try:
                tweet = c.next()
                str = tweet.text.encode('utf-8').strip()
                if tweet.coordinates is not None:
                    print str
                    if sicknessClassifier(sickNgramModel, healthyNgramModel, str):
                        #add to database
                        print "TWEET TAGGED"
                        print db.session.query(Tweet).filter(Tweet.tweet_id == tweet.id).count() 
                        if db.session.query(Tweet).filter(Tweet.tweet_id == tweet.id).count() == 0:
                            add_tweet(tweet)
                        else:
                            print "NOT ADDED"
                if iterator <= 0:
                    db.session.commit()
                    iterator = 20
                else:
                    iterator = iterator - 1
                    
            except tweepy.TweepError:
                db.session.commit()
                time.sleep(60*15)
                continue    
            except StopIteration:
                db.session.commit()
                break
    
    #db.session.commit()
    
    tweet = Tweet.query.all()
    print len(tweet)
    
def add_tweet(tweet):
    print tweet.created_at
    print tweet.coordinates['coordinates'][0]
    
    t = Tweet(date=tweet.created_at, position_x=int(1000*tweet.coordinates['coordinates'][0]), position_y=int(1000*tweet.coordinates['coordinates'][1]), tweet_id=tweet.id)
    if int(1000*tweet.coordinates['coordinates'][0]) != 0 and int(1000*tweet.coordinates['coordinates'][1]) != 0:
        db.session.add(t)
    return

import time
from datetime import date, timedelta
tweet_date = date(2010,10,1)
#while tweet_date < date(2010,11,23):
#    gather_sick_tweets(['#flu', '#cold', '#sick'], since_field=str(tweet_date), until_field=str(tweet_date+timedelta(days=6)) )
#    tweet_date = tweet_date + timedelta(days=7)
#    print tweet_date
gather_sick_tweets(['#flu OR #fever OR #sick'])