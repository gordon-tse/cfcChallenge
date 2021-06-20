import unittest
from HTMLParser import HTMLParser


class TestHTMLParser(unittest.TestCase):

    def test_empty(self):
        parser = HTMLParser(None)
        wordlist = ["", "a", "b", "c"]
        parser.append_wordlist(wordlist)
        self.assertNotIn("", parser.get_wordlist())

    def test_regex(self):
        parser = HTMLParser(None)
        wordlist = ["a\xa0", ",.", "1.2.3", "@|", "correct"]
        parser.append_wordlist(wordlist)
        self.assertNotIn("\xa0", parser.get_wordlist())
        self.assertNotIn(",", parser.get_wordlist())
        self.assertNotIn(".", parser.get_wordlist())
        self.assertNotIn("1", parser.get_wordlist())
        self.assertNotIn("2", parser.get_wordlist())
        self.assertNotIn("3", parser.get_wordlist())
        self.assertNotIn("@", parser.get_wordlist())
        self.assertNotIn("|", parser.get_wordlist())
        self.assertIn("correct", parser.get_wordlist())


if __name__ == '__main__':
    unittest.main()
