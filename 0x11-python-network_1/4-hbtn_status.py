#!/usr/bin/python3
""" This module fetches https://intranet.hbtn.io/status """

import requests


if __name__ == "__main__":
    text = requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print(f"\t- type: {type(text)}")
    print(f"\t- content: {text}")
