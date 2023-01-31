import unittest

from test_openai_api import TestOpenaiApi

def my_suite():
    suite = unittest.TestSuite()
    # result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestOpenaiApi))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()