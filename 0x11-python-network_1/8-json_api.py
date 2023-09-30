#!/usr/bin/python3
""" This module fetches https://intranet.hbtn.io/status """

import requests
import sys


if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        json = response.json()
        if json:
            print(f'[{json.get("id")}] {json.get("name")}')
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
