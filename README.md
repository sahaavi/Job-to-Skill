# Job-to-Skill

## Group members: 
- Avishek Saha: avisheksaha123@gmail.com
- Noman Mohammad: noman0786@hotmail.com
- Viji Rajagopalan: vijayalakshmi_r.here@yahoo.com


## Directory Layout:
| Section | Details|
| -----------| -----------|
|Project repository:| https://github.com/sahaavi/Job-to-Skill |
|Execution:|Run driver.ipynb, this runs the main module and has commands to view the output in dataframes and show visualizations on analytics performed|
|Package details:| Modules: run.py, job_desc.py, openai_api.py, job_viz.py|
|Documentation:| README.md, add usecase flow|
|CI/CD:| Github action is used for CI/CD and details are provided below |

## Package details:
### run.py
This module accepts input from the user. This acts as the main module that calls the other .py modules for specific functions and then creates final output.
``` i. main - This module accepts input from the user and validates it. User can either provide either direct job urls if they are from LinkedIn or enter job description for upto 10 jobs of interest. 
      This invokes scrape_job_description method in job_desc.py if the user inputs URL to scrape job description. This invokes call_api and call_api_interview to   processes job description for desired output.
      This invokes call_api_interview method in openai_api.py to call open ai API to get interview questions and answers for suggested skills.
   ii. call_api - This method is used to call functions in openai_api.py to call openai API to process job description text and get analytics on skills.
   
 ```
 
### job_desc.py
``` 
This module is used if user selects to input job URL from LinkedIn. 
   iv. scrape_job_description - This method is used to create a beautifulsoup object and scrape details of the job using the urls input by the user. It processes url by url and scrapes job description if url is valid. If url is not valid, it displays an error to the user, skips particular url and processes the others. It returns a pandas dataframe with details of job description - job location, job url, job description and job title.
```

### openai_api.py
``` 
This module has all functions related to the openai API calls to get job specific skill details from the job description. It then uses the skill details as input and uses openai API call again to get relevant questions for interview preparation based on the skills identified. This has two major openai API calls.
   v. call_api_skills_percent - This method is used to call openAI api and return skills needed with Percentages. This uses two methods:
        get_skills - This method is used to extract only the skills with percentage line from api's response.
        skills_percentage - This method is used to make a dictionary of skills with percentages.
        get_all - This method is used to make a dictionary of programming languages, tools and technical skills.
  vi. call_api_tech_skills - This method is used to call openAI api and return Techincal Skills.
 vii. call_api_questions - This method is used to call api and return interview questions. This used method below.
        get_questions - This method is used to call openAI api and return return relevant interview questions based off skills.
viii. call_api_answers - This method is used to call api and return suggested answers to interview questions. This used method below.
        get_question_answers - This method is used to call API and return relevant interview questions responses based off skills.
  ix. call_api_interview - This method calls functions vii and viii and returns interview question and answers in a dataframe format.
 ```
### job_viz.py
``` 
This module has all functions related to the visualizations built for the output based on openai APIs output. 
   x. def parse_df - This method parses the dataframe with all information and selects only columns needed for different visualizations.
   xi. visualize_info - This method is to visualize tools/languages from the jobs dataframe.
  xii. visualize_location - This method is to visualize distribution of job locations (applicable only if job links were provided in input).
 ```

### output files
1. jobs.csv - has details like skills and location required for each job input 
2. interview.csv - has list of interview questions for each job input with suggested answers from openai
3. visualizations in driver.ipynb

## Documentation:
1. Training (Vignette) - Main user scenario with output and visualization
2. README.md - Comprehensive list of files and functions for the program

### Training video:
<<<upload video>>>




## Report Coverage:
![IMAGE_DESCRIPTION](https://github.com/sahaavi/Job-to-Skill/blob/main/coverage_report.PNG)


## Github Action CI Status:
[![Build Status][build-shield]][build-url]
[![Release][release-shield]][release-url]
[![Forks][forks-shield]][forks-url]
[![Downloads][downloads-shield]][downloads-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]


<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://github.com/sahaavi/Job-to-Skill/actions/workflows/build.yml/badge.svg
[release-shield]: https://img.shields.io/github/v/release/sahaavi/Job-to-Skill.svg?style=flat-square
[release-url]: https://github.com/sahaavi/Job-to-Skill/releases
[forks-shield]: https://img.shields.io/github/forks/sahaavi/Job-to-Skill.svg?style=flat-square
[forks-url]: https://github.com/sahaavi/Job-to-Skill/network/members
[downloads-shield]: https://img.shields.io/github/downloads/sahaavi/Job-to-Skill/total.svg?style=flat-square
[downloads-url]: https://github.com/sahaavi/Job-to-Skill
[stars-shield]: https://img.shields.io/github/stars/sahaavi/Job-to-Skill.svg?style=flat-square
[stars-url]: https://github.com/sahaavi/Job-to-Skill/stargazers
[license-shield]: https://img.shields.io/github/license/sahaavi/Job-to-Skill.svg?style=flat-square
[license-url]: https://github.com/sahaavi/Job-to-Skill/blob/master/LICENSE
[build-url]: https://github.com/sahaavi/Job-to-Skill/actions/workflows/build.yml
