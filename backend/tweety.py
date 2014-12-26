import tweepy

consumer_key = 'PIAQQFVJF7DB2JlrOwgUt7sXn'
consumer_secret = 'BqqjbSFpZZ33dSQ1JHMiF0DmySUS3dFjQS73zMcjhs97uq1QDR'
auth_key = '2293938194-pkUSFXrOhiOuU7DwBCAbBY7QGzsfqmYagCRMSKU'
auth_secret = 'XiLUctGAZIr5hnGiHbwZoXymxseTWxSi1VfkrGRsd4EII'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(auth_key, auth_secret)

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print tweet.text

search = 'cold'

c = tweepy.Cursor(api.search, q=search, include_entities=True, lang='en').items(1000)

while True:
    try:
        tweet = c.next()
        
        str = tweet.text.encode('utf-8').strip()
        if tweet.coordinates is not None:
            print str
            #print tweet.coordinates
            #print tweet.created_at
    except tweepy.TweepError:
        time.sleep(60*15)
        continue    
    except StopIteration:
        break
