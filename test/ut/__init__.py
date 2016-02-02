import unittest as utt

class TestCephOnly(utt.TestCase):
    def setUp(self):
        utt.TestCase.setUp(self)
    def tearDown(self):
        utt.TestCase.tearDown(self)

class TestWithOpenstack(utt.TestCase):
    def setUp(self):
        utt.TestCase.setUp(self)
    def tearDown(self):
        utt.TestCase.tearDown(self)

from test.ut.test_cmd import TestCmd

def suite():
    ts = utt.TestSuite()
    ts.addTest(TestCmd("test_list_pools"))
    ts.addTest(TestCmd("test_list_images"))
    ts.addTest(TestCmd("test_list_blocks"))
    ts.addTest(TestCmd("test_list_objects"))
    ts.addTest(TestCmd("test_list_paths"))
    return ts

def runut():
    utt.TextTestRunner().run(suite())

if __name__ == '__main__':
    runut()
