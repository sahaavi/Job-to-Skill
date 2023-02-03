import unittest

from test_openai_api import TestOpenaiApi
from test_openai_api import TestJobDescScrp

def my_suite():
    suite = unittest.TestSuite()
    # result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestOpenaiApi))
    suite.addTest(unittest.makeSuite(TestJobDescScrp))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()