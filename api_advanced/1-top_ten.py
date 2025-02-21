#!/usr/bin/python3
"""
Module to fetch the top 10 hot posts from a given subreddit using Reddit's API.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts from a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Custom-User-Agent/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json().get('data', {})
        posts = data.get('children', [])

        if not posts:
            print("None")
            return

        for post in posts:
            print(post['data'].get('title', "None"))

    except (ValueError, KeyError):
        print("None")
