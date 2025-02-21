#!/usr/bin/python3
"""
Fetching the hot top 10 post in a given subreddit
"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Fab'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        value = response.json()
        datas = value['data']['children']
        for data in datas:
            title = data['data']['title']
            print(title)
    else:
        print('None')
