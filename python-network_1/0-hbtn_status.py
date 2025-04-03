#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"

    # Use a with statement to handle the request
    with urllib.request.urlopen(url) as response:
        body = response.read()

    # Print the required output
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))

