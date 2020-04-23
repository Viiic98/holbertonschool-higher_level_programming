#!/usr/bin/python3
""" POST using requests """


if __name__ == "__main__":
    import sys
    import requests

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
