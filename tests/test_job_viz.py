import sys
sys.path.append('/Users/nomanmohammad/Desktop/Job-to-Skill')
import os
import pandas as pd
import altair as alt

import unittest

from job_skill import job_viz as jv

class TestJobVisualization(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        print("job_viz test starts")

        cls.df = pd.DataFrame({'Job URL': ['https://www.linkedin.com/jobs/view/3472248063'], 
        'Tools': ['Azure/AWS, MLOps, Data Management and Analytics Platforms'],
        'Programming Languages': ['Java, C#, Ruby, Python'],
        'Job Location': 'Toronto, ON, Canada'})

        cls.df_tools = pd.DataFrame({'Tools': ['AWS', 'Azure', 'Excel']})

        cls.df_lang = pd.DataFrame({'Programming Languages': ['Java', 'C#', 'Ruby', 'Python']})

    # setting up for test
    def setUp(self):
        print("Test Setup")

    # test end
    def tearDown(self):
        print("Test End")

    @classmethod
    def tearDownClass(cls):
        print("job_viz test finishes")

    # test case
    def test_parse_df(self): 
        self.assertIsInstance(jv.parse_df(self.df, 'Tools'), pd.DataFrame)

unittest.main(argv=[''], verbosity=2, exit=False)

import altair as alt


