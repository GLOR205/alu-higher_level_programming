#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary to hold the email data
    data = {'email': email}

    # Encode the data in application/x-www-form-urlencoded format
    data = urllib.parse.urlencode(data).encode('utf-8')

    # Make the POST request with the email parameter
    with urllib.request.urlopen(url, data) as response:
        # Read and decode the response
        body = response.read().decode('utf-8')

    # Print the body of the response
    print(body)

