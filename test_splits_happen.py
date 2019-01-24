import unittest
import splits_happen as sh


class TestSplitsHappens(unittest.TestCase):

    def test_splits_happen_case_one(self):
        res = sh.splits_happen('XXXXXXXXXXXX')
        self.assertEqual(res, 300)

    def test_splits_happen_case_two(self):
        res = sh.splits_happen('9-9-9-9-9-9-9-9-9-9-')
        self.assertEqual(res, 90)

    def test_splits_happen_case_three(self):
        res = sh.splits_happen('5/5/5/5/5/5/5/5/5/5/5')
        self.assertEqual(res, 150)

    def test_splits_happen_case_four(self):
        res = sh.splits_happen('X7/9-X-88/-6XXX81')
        self.assertEqual(res, 167)

    def test_splits_happen_case_five(self):
        res = sh.splits_happen('81-92/X637-52X-62/X')
        self.assertEqual(res, 122)
