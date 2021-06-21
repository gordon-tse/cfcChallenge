import os.path
import requests
import json
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from WordFreqCounter import WordFreqCounter
from ExternalResCatcher import ExternalResCatcher


if __name__ == '__main__':
    outdict = {}
    baseURL = "https://www.cfcunderwriting.com/"
    html = requests.get(baseURL)
    if html.status_code != 200:
        print(str(html.status_code) + ": Unsuccessful http request")
        exit(1)

    soup = BeautifulSoup(html.content, 'html.parser')

    # Step 1 and 2: Scrape the index page and find all externally hosted resources
    possibleTags = {"img": "src", "script": "src", "link": "href", "video": "src", "object": "data",
                    "audio": "src", "iframe": "src", "embed": "src", "source": "src"}

    catcher = ExternalResCatcher(soup)
    for tag in possibleTags:
        resources = catcher.find_resources(tag, possibleTags.get(tag))
        if resources is not None:
            outdict[tag] = resources

    # Step 3: Enumerating the index page to locate the "Privacy policy"
    link = ""
    for x in soup.findAll("a"):
        content = x.find(text=True)
        if content == "Privacy policy":
            link = x["href"]
    if link == "":
        print("Privacy policy not found")
        exit(1)

    # Step 4: Scraping the page and counting word frequency
    privacy = HTMLParser(baseURL + link)
    privacy.parse()
    counter = WordFreqCounter(privacy.get_wordlist())
    outdict["Word Frequency"] = counter.count()

    # Write to a json file
    dir = os.path.realpath(os.curdir) + "/"
    try:
        with open(dir + "output.json", "w") as outfile:
            json.dump(outdict, outfile)
    except IOError:
        print("Cannot open or write to a file")
        exit(1)


