import unittest

def str_list(string):
    list1 = string.split()
    return list1

class Test(unittest.TestCase):

    def test_str_list(self):
        self.assertEqual(str_list("as sa"), ["as","sa"])
        self.assertEqual(str_list(" "), [])
        self.assertEqual(str_list("asdwqd dqwdqd dqwqdq wdwq sa"), ["asdwqd","dqwdqd", "dqwqdq", "wdwq", "sa"])