#!/usr/bin/python3
""" Post request """


if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        r = response.read()
        print(r.decode('utf-8'))
