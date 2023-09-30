#!/usr/bin/python3
""" This module takes in a URL, sends a request to the URL, and displays the
    body of the response (decoded in utf-8) """
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
