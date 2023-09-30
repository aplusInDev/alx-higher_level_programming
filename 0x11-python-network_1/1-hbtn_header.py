#!/usr/bin/python3
""" This module fetches https://intranet.hbtn.io/status """

import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as req:
        info = req.info()
        print(info.get("X-Request-Id"))
