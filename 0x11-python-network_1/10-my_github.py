#!/usr/bin/python3
""" This module fetches https://intranet.hbtn.io/status """

import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    response = r = requests.get(
        f"https://api.github.com/users/{user}",
        headers={"Authorization": f"token {pwd}"},
    )
    print(response.json().get("id"))
