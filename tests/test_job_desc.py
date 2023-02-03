#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
sys.path.append("e:\\Study\\UBC\\Block 4\\DATA 534 Web and Cloud Computing\\Project\\Job-to-Skill")
sys.path.append("C:\\Users\\vijip\\DATA\DATA534\\Job-to-Skill")
import os

import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from dotenv import load_dotenv

from job_skill import job_desc as jd

class TestJobDescScrp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        print("job_Skill test starts")

    # setting up for test
    def setUp(self):
        print("Test Setup")

    # test end
    def tearDown(self):
        print("Test End")

    @classmethod
    def tearDownClass(cls):
        print("job_Skill test finishes")

    # test case
    def test_df_output(self):
        df1=pd.DataFrame({'ind':[1,2]})
        df2=pd.DataFrame({'ind':[1,2]})
        assert_frame_equal(df1, df1)

    # test case
    #def test_call_api_tech_skills(self): 
    #    self.assertIsInstance(oa.call_api_tech_skills(self.api_key, self.job_description), dict)

unittest.main(argv=[''], verbosity=2, exit=False)

