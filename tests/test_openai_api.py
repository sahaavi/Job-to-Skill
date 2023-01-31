import sys
sys.path.append("e:\\Study\\UBC\\Block 4\\DATA 534 Web and Cloud Computing\\Project\\Job-to-Skill")

import unittest

from job_skill import openai_api as oa

class TestOpenaiApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("openai_api test starts")
        cls.api_key = 'x'
        cls.job_description = """Understand the day-to-day issues that our business faces, which can be better understood with data
            Collecting and analyzing data from a variety of sources (such as college and university websites, government databases, and industry reports)
            Cleaning, formatting, and organizing the data in a way that is useful and easy to understand
            Creating Excel sheets or other data visualization tools to display the information in a clear and visually appealing way
            Identifying trends and patterns in the data, and providing insights and recommendations based on the analysis
            Collaborating with other teams within the company to ensure that the data is accurate and relevant to their needs
            Continuously monitoring and updating the data set to ensure its relevance and accuracy
            Compile and analyze data related to business' issues
            Develop clear visualizations to convey complicated data in a straightforward fashion."""

    # setting up for test
    def setUp(self):
        print("Test Setup")

    # test end
    def tearDown(self):
        print("Test End")

    @classmethod
    def tearDownClass(cls):
        print("openai_api test finishes")

    # test case
    def test_call_api(self): 
        self.assertIsInstance(oa.call_api(self.api_key, self.job_description), dict)

unittest.main(argv=[''], verbosity=2, exit=False)
        