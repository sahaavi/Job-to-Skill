# Job-to-Skill

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


## Usage
#### `call_api_tech_skills`   
Returns the tech skills, required programming languages and tools needed based on job description. 

```python
import openai_api as oa
api_key = 'x'
job_description = 'Work on challenging and research-based initiatives using advanced machine learning......'
skills = oa.call_api_tech_skills(api_key, job_description)
```

#### `call_api_questions`
Returns interview questions based on technical skills.

```python
questions = oa.call_api_questions(api_key, skills)
```

#### `call_api_answers`
Returns answers of those interview questions.
```python
answers = oa.call_api_answers(api_key, skills)
```
#### `run`
If you run this file it will take all the user input from user and generate 2 csv file which will contain job title, url, location, tech skills, programming languages and tools required for that job, interview questions and sample answers.
```python
from job_skill import run
run.main()
```
This will generate 2 csv files named `interview.csv` and `jobs.csv`.

#### `visualize_info`
```python
from job_skill import job_viz as jv

jobs_df = pd.read_csv("jobs.csv")

lang = jv.parse_df(jobs_df, 'Programming Languages')
tools = jv.parse_df(jobs_df, 'Tools')

jv.visualize_info(lang, tools)
```
Output:  
![visualization](visualization.jpg)

#### `visualize_location`
```python
jv.visualize_location(jobs_df, 'Job Location')
```
Output:  
![location](location.jpg)