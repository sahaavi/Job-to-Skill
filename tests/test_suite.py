import sys
sys.path.append("e:\\Study\\UBC\\Block 4\\DATA 534 Web and Cloud Computing\\Project\\Job-to-Skill")
sys.path.append("e:\\Study\\UBC\\Block 4\\DATA 534 Web and Cloud Computing\\Project\\Job-to-Skill\\tests")

import unittest

from test_openai_api import TestOpenaiApi
from test_job_desc import TestJobDescScrp
from test_job_viz import TestJobVisualization

def my_suite():
    suite = unittest.TestSuite()
    # result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestOpenaiApi))
    suite.addTest(unittest.makeSuite(TestJobDescScrp))
    suite.addTest(unittest.makeSuite(TestJobVisualization))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()