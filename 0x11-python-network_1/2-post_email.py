#!/usr/bin/python3
""" This module takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8) """
import urllib.request
import sys


if __name__ == "__main__":
    mail = {"email": sys.argv[2]}
    encoded_mail = urllib.parse.urlencode(mail).encode("ascii")
    req = urllib.request.Request(sys.argv[1], encoded_mail)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
