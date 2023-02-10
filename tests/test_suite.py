import unittest

from test_openai_api import TestOpenaiApi
from test_job_desc import TestJobDescScrp
from test_job_viz import TestJobVisualization
from test_integration import TestIntegration

def my_suite():
    suite = unittest.TestSuite()
    # result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestOpenaiApi))
    suite.addTest(unittest.makeSuite(TestJobDescScrp))
    suite.addTest(unittest.makeSuite(TestJobVisualization))
    suite.addTest(unittest.makeSuite(TestIntegration))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()