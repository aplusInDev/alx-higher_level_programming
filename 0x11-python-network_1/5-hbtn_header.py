#!/usr/bin/python3
""" This module fetches https://intranet.hbtn.io/status """

import requests
import sys


if __name__ == "__main__":
    header = requests.get(sys.argv[1]).headers
    print(header.get("X-Request-Id"))
