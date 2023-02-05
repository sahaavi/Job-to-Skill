import os

from dotenv import load_dotenv
import pandas as pd

from job_skill import job_desc as jd
from job_skill import openai_api as oa

def call_api(df1):
    # loading api key
    load_dotenv()
    api_key = os.getenv("API_KEY")

    df1['Skills_and_Percentage'] = None
    df1['Programming Languages'] = None
    df1['Tools'] = None
    df1['Technical Skills'] = None

    for index, desc in df1.iterrows():
        result = oa.call_api_skills_percent(api_key, desc['Job Description'])
        result2 = oa.call_api_tech_skills(api_key, desc['Job Description'])
        
        # Storing the values from the dictionary
        skills = result['Skills']
        percentage = result['Percentage']

        # Zipping the values together
        skills_and_percentage = zip(skills, percentage)

        # Converting the zip object to a list
        skills_and_percentage = list(skills_and_percentage)

        #storing Skills_and_Percentage in df
        df1.at[index, 'Skills_and_Percentage'] = skills_and_percentage

        # Storing the values from the dictionary
        p_lang = result2['Programming Languages']
        tools = result2['Tools']
        tech_skills = result2['Technical Skills']

        # storing in df
        df1.at[index, 'Programming Languages'] = p_lang
        df1.at[index, 'Tools'] = tools
        df1.at[index, 'Technical Skills'] = tech_skills
    return df1

def main():
    #Get user input on job description in an array
    try:
        inputarr=list()
        usr_in_op,usr_in = '',''

        while usr_in_op != 'X':
            usr_in_op = input("Would you like to enter job description or job URL A: description B. URL X. Exit \n")
            input_jobs = int(input("How many jobs would you like to enter(integers)? MIN:1 & MAX:10 \n"))

            if input_jobs < 1 or input_jobs > 10:
                print("Number of jobs anticipated is not valid. Please enter an integer between 1 and 10 (both inclusive)")
                usr_in_op = 'X' 

            if usr_in_op == 'A':

                for i in range(input_jobs):
                    print("######Job Description number######",i+1)
                    inputstr = input("\nEnter job description:")
                    #print(inputstr)
                    while inputstr == '':
                        print("You are in a time loop. Input job description to get out of it")
                        inputstr = input("\nEnter job description:")
                    inputarr.append(inputstr)
                usr_in=usr_in_op
                usr_in_op = 'X'

            elif usr_in_op == 'B':

                for i in range(input_jobs):
                    print("######Job URL number######",i+1)
                    inputstr = input("\nEnter job URL:")
                    #print(inputstr)
                    while inputstr == '':
                        print("You are in a time loop. Input job description to get out of it")
                        inputstr = input("\nEnter job description:")
                    inputarr.append(inputstr)
                    #execute function
                usr_in=usr_in_op
                usr_in_op = 'X'

        if usr_in == 'A':
            df1 = pd.DataFrame(list(zip("", "","","","")), columns = ["Job URL","Job Description","Job Title","Job Location"])
            df1["Job Description"]=inputarr
            df1 = call_api(df1)
        elif usr_in == 'B':
            df1 = jd.scrape_job_description(inputarr)
            ignore_df = None
            ignore_df = df1[df1["Job Description"] == "Invalid URL, analysis skipped"]
            
            #Output the invalid job urls and notify user
            if len(ignore_df) > 0:
                print ("Invalid jobs will be skipped. Number of jobs skipped in current run are:",len(ignore_df))
                print ("\nFollowing are the details of the jobs skipped:",(ignore_df))  

            # This is the dataframe with all valid inputs for downstream assessment
            df1 = df1[df1["Job Description"] != "Invalid URL, analysis skipped"]
            df1 = call_api(df1)

    except ValueError:
        print("Error: Number of jobs anticipated is not valid. Please enter an integer between 1 and 10 (both inclusive)")
    except Exception:
        print("An unknown error occurred. Please try again with valid inputs.")

    print(df1)

if __name__ == '__main__':
    main()