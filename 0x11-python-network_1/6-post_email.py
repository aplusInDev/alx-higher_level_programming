#!/usr/bin/python3
""" This module fetches https://intranet.hbtn.io/status """

import requests
import sys


if __name__ == "__main__":
    text = requests.post(sys.argv[1], data={"email": sys.argv[2]}).text
    print(text)
