data = json.loads(file_name)

def most_retweeted(data):
    times_retweeted_unordered = []
    for tweet in data:
        times_retweeted_unordered.append((tweet['retweet_count'], tweet['id']))
    times_retweeted_ordered = times_retweeted_unordered.sort(key=lambda x: x[0], reverse=True)[:10]
    return times_retweeted_ordered

def most_tweets_users(data):
    users_dictionary = {}
    for tweet in data:
        user_tweets = 0
        user_id = tweet['user']['id']
        if user_id not in users_dictionary:
            for tweet_2 in data:
                if user_id == tweet_2['user']['id']:
                    user_tweets += 1
            users_dictionary[user_id] = user_tweets
            users_ordered = sorted(users_dictionary.items(), key=lambda x: x[1], reverse=True)[:10]
    return users_ordered

def get_day_from_string(string_date):
    pass

def top_ten_days(data):
    days_dictionary = {}
    for tweet in data:
        day = get_day_from_string(tweet['date'])
        if day not in days_dictionary:
            days_dictionary[day] = 1
        else:
            days_dictionary[day] += 1
    days_ordered = sorted(days_dictionary.items(), key=lambda x: x[1], reverse=True)[:10]
    return days_ordered

def top_ten_hashtags(data):
    hashtags_dictionary = {}
    for tweet in data:
        for hashtag in tweet['hashtags']:
            if hashtag not in hashtags_dictionary:
                hashtags_dictionary[hashtag] = 1
            else:
                hashtags_dictionary[hashtag] += 1
    hashtags_ordered = sorted(hashtags_dictionary.items(), key=lambda x: x[1], reverse=True)[:10]
    return hashtags_ordered

def main(action):
    if action == "most retweeted":
        return most_retweeted(data)
    elif action == "top ten days":
        return top_ten_days(data)
    elif action == "most tweets users":
        return most_tweets_users(data)
    elif action == "top ten hashtags":
        return top_ten_hashtags(data)
    


        
        

    

    
    
