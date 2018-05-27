#! python3

import re
import urllib.request as ureq
import sys
import urllib.error as uerr

def help():
    print("""
Usage:
    
    python3 finder.py [link to youtube video]

            """)


def get_page(URL):
    """ A function that returns a usable form of the html file of a page whose URL 
    is the only parameter to this function. """
    try:
        return ureq.urlopen(URL).read().decode("utf-8")
    except ValueError:
        help()
        print("Enter a link")
        sys.exit(0)
    except uerr.URLError:
        help()
        print("Check your link.")
        sys.exit(0)
    except UnicodeDecodeError:
        help()
        print("Check your link.")
        sys.exit(0)

def extract_keywords(webpage):
    """ A function that returns a list of keywords from the html file of a YouTube video """
    try:
        return re.findall(r"\"keywords\"\:\"(.*?)\"",webpage)[0].split(",")
    except IndexError:
        help()
        print("Check your YouTube link.")
        sys.exit(0)

def get_input():
    """ Getting the URL of the YouTube video to be scraped. """
    try:
        return sys.argv[1]
    except IndexError:
        help()
        sys.exit(0)

for i in extract_keywords(get_page(get_input())):
    print(i)

