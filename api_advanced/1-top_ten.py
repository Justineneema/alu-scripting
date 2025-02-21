#!/usr/bin/python3
"""
A script to fetch the top 10 hot posts from a given subreddit using Reddit's API.
"""
import requests


def top_ten(subreddit):
    """Fetches and prints the titles of the top 10 hot posts from a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Custom-User-Agent/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if request is successful
    if response.status_code == 200:
        try:
            value = response.json()
            datas = value.get('data', {}).get('children', [])

            if not datas:
                print("None")
                return

            for data in datas:
                title = data['data'].get('title', "None")
                print(title)

        except ValueError:
            print("None")  
    else:
        print("None")  
