import argparse
import urllib.request
import logging
import datetime

def downloadData(url):
    """Downloads the data"""

print('Now downloading with urllib2...')
url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
urllib.request.urlretrieve(url, 'Downloads/birthdays100.csv')
pass

def processData(file_content):
    pass


def displayPerson(id, personData):
    pass

def main(url):
    print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)