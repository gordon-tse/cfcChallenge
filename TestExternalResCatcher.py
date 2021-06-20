import unittest
from ExternalResCatcher import ExternalResCatcher


class MyTestCase(unittest.TestCase):
    def test_http_begin(self):
        catcher = ExternalResCatcher(None)
        self.assertTrue(catcher.is_externally_hosted("https://abc.com"))
        self.assertFalse(catcher.is_externally_hosted("/abc.jpg"))

    def test_cfcurl(self):
        catcher = ExternalResCatcher(None)
        self.assertTrue(catcher.is_externally_hosted("https://abc.com"))
        self.assertTrue(catcher.is_externally_hosted("https://google.com/cfcunderwriting"))
        self.assertFalse(catcher.is_externally_hosted("http://www.cfcunderwriting.com"))
        self.assertFalse(catcher.is_externally_hosted("abc/http/cfcunderwriting.com"))


if __name__ == '__main__':
    unittest.main()
