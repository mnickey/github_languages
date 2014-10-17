import sys
import operator
from collections import defaultdict

import requests

def get_repositories(user):
    """ Retreive a list of a user's repositories """
    url = "https://api.github.com/users/{user}/repos".format(user=user)
    response = requests.get(url)
    return response.json()

def main():
    """ Main function """
    repositories = get_repositories(sys.argv[1])
    print repositories

if __name__ == "__main__":
    main()
