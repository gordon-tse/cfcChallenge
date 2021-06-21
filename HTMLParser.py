import re
import requests
from bs4 import BeautifulSoup


class HTMLParser:

    def __init__(self, url):
        self.wordList = []
        if url is not None:
            html = requests.get(url)
            self.soup = BeautifulSoup(html.content, "html.parser")

    # Parameter: Iterable
    def append_wordlist(self, text):
        for word in text:
            item = re.split("[\\s\xa0()\"”“1234567890,.:;@!~|{}><©]", word)
            self.wordList.extend([each for each in item if each])

    def get_wordlist(self):
        return self.wordList

    def parse(self):
        # Remove invisible contents and the secondary-nav bar
        for s in self.soup(['style', 'script', '[document]', 'head', 'title']):
            s.extract()

        s = self.soup.find("nav", {"class": "secondary-nav"})
        s.extract()

        # Loop through the all <div> tags with attr - class=container
        for page in self.soup.find_all("div", {"class": "container"}):
            page = page.text.split("\n")
            self.append_wordlist(page)
