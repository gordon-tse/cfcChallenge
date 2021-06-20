import unittest
from WordFreqCounter import WordFreqCounter


class TestWordFreqCounter(unittest.TestCase):

    def test_null(self):
        testNull = WordFreqCounter(None)
        testNullResult = testNull.count()
        self.assertIsNot(bool(testNullResult), True)  # should have an empty dictionary

    def test_empty(self):
        testEmpty = WordFreqCounter([])
        testEmptyResult = testEmpty.count()
        self.assertIsNot(bool(testEmptyResult), True)  # should have an empty dictionary

    def test_one(self):
        test1word = ["This", "is", "a", "dog", "this", "dog", "is", "smelly"]
        test1 = WordFreqCounter(test1word)
        test1result = test1.count()
        assert (test1result["this"] == 2)
        assert (test1result["dog"] == 2)
        assert (test1result["smelly"] == 1)

    def test_two(self):
        test2word = ["This", "is", "1", "dog", "this", "dog", "Is", "smelly", "2", "lovely", "very", "lOvElY"]
        test2 = WordFreqCounter(test2word)
        test2result = test2.count()
        assert (test2result["lovely"] == 2)
        assert (test2result["1"] == 1)
        assert (test2result["2"] == 1)
        assert (test2result["very"] == 1)
        assert (test2result["is"] == 2)


if __name__ == '__main__':
    unittest.main()
