#!/usr/bin/python3
"""Query to Reddit Api"""

import requests


def number_of_subscribers(subreddit):
    """Returns total subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Chrome/114.0.5735.110"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
