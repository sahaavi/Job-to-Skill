import sys
# sys.path.append("e:\\Study\\UBC\\Block 4\\DATA 534 Web and Cloud Computing\\Project\\Job-to-Skill")
sys.path.append('/Users/nomanmohammad/Desktop/Job-to-Skill')
import os
import pandas as pd

import unittest
# from dotenv import load_dotenv

from job_skill import openai_api as oa

class TestOpenaiApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # load_dotenv()
        print("openai_api test starts")
        # cls.api_key = os.getenv("API_KEY")
        cls.api_key = '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'
        cls.job_description = """Understand the day-to-day issues that our business faces, which can be better understood with data
            Collecting and analyzing data from a variety of sources (such as college and university websites, government databases, and industry reports)
            Cleaning, formatting, and organizing the data in a way that is useful and easy to understand
            Creating Excel sheets or other data visualization tools to display the information in a clear and visually appealing way
            Identifying trends and patterns in the data, and providing insights and recommendations based on the analysis
            Collaborating with other teams within the company to ensure that the data is accurate and relevant to their needs
            Continuously monitoring and updating the data set to ensure its relevance and accuracy
            Compile and analyze data related to business' issues
            Develop clear visualizations to convey complicated data in a straightforward fashion."""

        cls.job_skills = [['python', 'SQL', 'java']]
        cls.interview_questions = ['What Big Data Technologies have you worked with?', 'What strategies have you used to capture and develop ideas?']


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
    def test_call_api_skills_percent(self): 
        self.assertIsInstance(oa.call_api_skills_percent(self.api_key, self.job_description), dict)

    # test case
    def test_call_api_tech_skills(self): 
        self.assertIsInstance(oa.call_api_tech_skills(self.api_key, self.job_description), dict)

    # test case
    def test_call_api_questions(self): 
        self.assertIsInstance(oa.call_api_questions(self.api_key, self.job_skills[0]), list)

    # test case
    def test_call_api_answers(self): 
        self.assertIsInstance(oa.call_api_answers(self.api_key, self.interview_questions), list)

    # test case
    def test_call_api_interview(self): 
        self.assertIsInstance(oa.call_api_interview(self.api_key, self.job_skills), pd.DataFrame)

unittest.main(argv=[''], verbosity=2, exit=False)