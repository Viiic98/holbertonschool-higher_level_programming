#!/usr/bin/python3
""" Display github id """


if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) == 3:
        user = sys.argv[1]
        passwd = sys.argv[2]
    else:
        user = ""
        passwd = ""
    r = requests.get('https://api.github.com/user',
                     auth=requests.auth.HTTPBasicAuth(user, passwd))
    print(r.json().get('id'))
