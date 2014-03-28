import os.path
import json
from getpass import getpass

import requests


def get_oauth_token():
    """
    Get or create an OAuth token for making pull requests.
    """
    cache = os.path.join(os.path.expanduser("~"), ".gitzen.gitauth")
    try:
        result = open(cache, 'r').read().strip()
    except IOError:
        username = raw_input("GitHub username: ")
        password = getpass("GitHub password: ")
        response = requests.post(
            "https://api.github.com/authorizations",
            data=json.dumps({
                "scopes": ["repo"],
                "note": "git-zen"
            }),
            auth=(username, password))
        result = response.json().get('token')
        with open(cache, 'w') as f:
            f.write(result)
    return result


def github_api(method, url, data=None, params=None):
    token = get_oauth_token()
    return requests.request(
        method, "https://api.github.com" + url, data=data, params=params,
        headers={"Authorization": "token %s" % token}
    ).json()