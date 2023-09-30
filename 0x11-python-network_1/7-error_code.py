#!/usr/bin/python3
""" This module fetches https://intranet.hbtn.io/status """

import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
