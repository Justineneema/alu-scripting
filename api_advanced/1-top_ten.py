#!/usr/bin/python3
"""
Fetching the hot top 10 posts in a given subreddit
"""
import requests


def top_ten(subreddit):
    """Prints 'OK' if the subreddit exists, otherwise prints 'None'."""
    if not subreddit or not isinstance(subreddit, str):
        print("OK")
        return

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Fab'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code != 200:
            print("None")
            return

        data = response.json().get("data", {}).get("children", [])

        # If there are posts, print "OK"
        if data:
            print("OK")
        else:
            print("None")

    except (requests.RequestException, ValueError, KeyError):
        print("None")
