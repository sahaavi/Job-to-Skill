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
        jd_url= "https://www.linkedin.com/jobs/view/3442691887"
        jd_text= """Company Description Dropbox is a leading global collaboration platform that's transforming the way people work together, from the smallest business to the largest enterprise. With more than 700 million registered users across more than 180 countries, our mission is to design a more enlightened way of working. From our headquarters in San Francisco to eight dedicated Studios and a worldwide team of employees who choose where they work best, our Virtual First approach is leading the way into the future of work. Team Description Our Product team advocates for our users and our business, setting the vision for our growing family of products. We use data, research, strategy, and empathy to guide multidisciplinary teams toward a common goal, balancing diverse perspectives and empowering our teams to do great work. As we scale globally, there’s plenty of space for you to grow alongside us and simplify life for millions of people around the world in team that always focuses on we, not I, and creates delightful products that are worthy of trust. Role DescriptionHow many times you get an opportunity to be at the ground floor on a very big and important mission? What if you get to be one of the top leaders defining the mission, hiring, guiding your teams and influencing the direction of Dropbox? As a Director of Data Science for this new division, you will exactly get to do that.  You will be able to drive the future direction of this new initiative and answer key questions about revenue/user growth. You will build and lead a team of top-tier data scientists and be an inherent part of product org to create and scale this new business.As a ground floor opportunity for this startup team, we need this lead to build a top-tier data-informed culture with a lot of focus on impact and execution.ResponsibilitiesYou will lead the team in balancing urgency vs. the incredibly high quality bar expected by both our customers and the broader Dropbox organization, through clear and repeatable data informed approachYou will partner closely with leadership across all functions - Product, Engineering, Design, Research, GTM, Customer success and Sales You will have the seat at the table for every key decision for this new initiativeYou will create a culture of strong technical ownership, resulting in highly reliable products and services at scaleYou will build and manage a team of high performing data scientists to deliver best in class analytics You will leverage data-driven insights to proactively identify most impactful opportunities, and inform future experimentation design and product roadmapsRequirementsBachelors’ or above in quantitative discipline: Statistics, Applied Mathematics, Economics, Computer Science, Engineering, or related field10+ years experience of leveraging data-driven analysis to influence key business decisions, preferably in a tech company3+ years directly managing data scientists, quantitative researchers, or product analystsProven track record of being able to work independently and proactively engage with business stakeholders with minimal direction & driver measurable business impactAbility to influence prioritization and execution of high impact projects effecting customer experience and monetizationAbility to analyze large datasets and use data to inform product or business decision making, with a track record of driving directly measurable product or business impactGood Executive presence with excellent verbal and written communication skillsPrevious experience building data driven programs and teams - experience with SQL and large datasets, deep understanding of statistical analysis & experiment designTotal RewardsFor candidates hired in San Francisco metro, New York City metro, or Seattle metro, the expected salary/On-Target Earnings (OTE) range for the role is currently $237,300 - $279,200 - $321,100. For candidates hired in the following locations: Austin (TX) metro, Chicago metro, California (outside SF metro), Colorado, Connecticut (outside NYC metro), Delaware, Massachusetts, New Hampshire, New York (outside NYC metro), Oregon, Pennsylvania (outside NYC or DC metro), Washington (outside Seattle metro) and Washington DC metro, the expected salary/On-Target Earnings (OTE) range for the role is currently $213,600 - $251,300 - $289,000. For candidates hired in all other US locations, the expected salary/On-Target Earnings (OTE) range for this role is currently $189,900 - $223,400 - $256,900. Range(s) is subject to change. Dropbox takes a number of factors into account when determining individual starting pay, including job and level they are hired into, location/metropolitan area, skillset, and peer compensation. Dropbox uses the zip code of an employee’s remote work location to determine which metropolitan pay range we use. Salary/OTE is just one component of Dropbox’s total rewards package. All regular employees are also eligible for the corporate bonus program or a sales incentive (target included in OTE) as well as stock in the form of Restricted Stock Units (RSUs). Dropbox is an equal opportunity employer. We are a welcoming place for everyone, and we do our best to make sure all people feel supported and connected at work. A big part of that effort is our support for members and allies of internal groups like Asians at Dropbox, BlackDropboxers, Latinx, Pridebox (LGBTQ), Vets at Dropbox, Women at Dropbox, ATX Diversity (based in Austin, Texas) and the Dropbox Empowerment Network (based in Dublin, Ireland).        Show more                Show less                    Seniority level                      Not Applicable                    Employment type                  Full-time                    Job function                      Engineering and Information Technology                      Industries                    IT Services and IT Consulting, Software Development, and Technology, Information and Internet          Referrals increase your chances of interviewing at Dropbox by 2x              See who you know             """
        jd_title="Dropbox hiring Director of Data Science, New Initiatives "
        jd_loc="Vancouver, British Columbia, Canada "
        test_df1=pd.DataFrame({"Job URL":[jd_url],"Job Description":[jd_text],"Job Title":[jd_title],"Job Location":[jd_loc]})
 #       df2=pd.DataFrame({'ind':[1,2]})
        print(jd_url,len(jd_url))
        print(test_df1)
        assert_frame_equal(test_df1, jd.scrape_job_description("https://www.linkedin.com/jobs/view/3442691887"))

    # test case
    #def test_call_api_tech_skills(self): 
    #    self.assertIsInstance(oa.call_api_tech_skills(self.api_key, self.job_description), dict)

unittest.main(argv=[''], verbosity=2, exit=False)

