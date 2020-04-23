#!/usr/bin/python3
""" Json obj using requests """


if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) == 2:
        value = sys.argv[1]
    else:
        value = ""
    r = requests.post('http://96e483228857.19.hbtn-cod.io:5000/search_user',
                      data={'q': value})
    try:
        json_obj = r.json()
        if json_obj:
            print("[{}] {}".format(json_obj.get('id'), json_obj.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
