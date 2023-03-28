import unittest

def easyint(integr):
    if integr % 2 !=0:
        return True
    else:
        return False
class Test(unittest.TestCase):

    def testeasyint(self):
        self.assertEqual(easyint(3),True)
        self.assertEqual(easyint(6),False)