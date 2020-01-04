import pprint
import requests
import time
import json

def get_comments():
    data = []
    try:
        req = requests.get('https://www.reddit.com/r/politics/comments/.json?limit=100')
        comments = json.loads(req.text)['data']['children']
        for comment in comments:
            pprint.pprint(comment)
            data.append(comment)
        return data
    except:
        print("Request Error")
        return []

if __name__ == "__main__":
    data = []
    i = 0;
    frequency = 2
    duration = 7200
    while(i <= int(duration/frequency)):
        data.extend(get_comments())
        time.sleep(frequency)
        i += 1

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
