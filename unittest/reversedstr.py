import unittest

def strreversed(string):
    rstr = string[::-1]
    if rstr == string :
        print("this string palindrom")
        return rstr
    else:
        return "this string not palindrom"

class Test(unittest.TestCase):

    def teststrreversed(self):
        self.assertEqual(strreversed("asa"), "asa")
