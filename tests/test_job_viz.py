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

    def test_visualize_info(self): 
        self.assertEqual(jv.visualize_info(self.df_lang, self.df_tools).to_dict()['vconcat'][0]['mark']['type'], 'bar')

    def test_visualize_location(self): 
        self.assertEqual(jv.visualize_location(self.df, 'Job Location').to_dict()['layer'][0]['mark']['type'], 'text')

unittest.main(argv=[''], verbosity=2, exit=False)