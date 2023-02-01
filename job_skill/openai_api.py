import openai
import pandas as pd
import altair as alt

pd.options.display.max_colwidth = None

def get_skills(response):
    """
    Extract only the skills with percentage line from api's response. Used to help call_api function. Not for direct use.

    Parameters
    ----------
    response : object 
        response got from openai api
        
    Returns
    -------
    list
        list containg skills and percentages with some extra html tags
        
    Examples
    --------
    >>> get_skills([<OpenAIObject at 0x23beb78d040> JSON: {
        "finish_reason": "stop",
        "index": 0,
        "logprobs": null,
        "text": "\na) Data Science: 30%\n\nb) Communications: 20%\n\nc) Relationship Building: 15%\n\nd) Planning: 10%\n\ne) Analytics: 10%\n\nf) Data Visualization: 5%\n\ng) Data Modeling: 5%\n\nh) Storytelling: 5%"}])
    
    ['\na) Data Science: 30%\n\nb) Communications: 20%\n\nc) Relationship Building: 15%\n\nd) Planning: 10%\n\ne) Analytics: 10%\n\nf) Data Visualization: 5%\n\ng) Data Modeling: 5%\n\nh) Storytelling: 5%']
    """
    text_list = [choice.text for choice in response['choices']]
    return text_list

def skills_percentage(response):
    """
    Make a dictionary of skills with percentages. Used to help call_api function. Not for direct use.

    Parameters
    ----------
    response : object 
        response after extracted using get_skills function.
        
    Returns
    -------
    dict
        skills required for job with percentage
        
    Examples
    --------
    >>> skills_percentage([<OpenAIObject at 0x23beb78d040> JSON: {
        "finish_reason": "stop",
        "index": 0,
        "logprobs": null,
        "text": "\na) Data Science: 30%\n\nb) Communications: 20%\n\nc) Relationship Building: 15%\n\nd) Planning: 10%\n\ne) Analytics: 10%\n\nf) Data Visualization: 5%\n\ng) Data Modeling: 5%\n\nh) Storytelling: 5%"}]
        )
    
    {'Skills': ['Collecting and analyzing data',
    'Cleaning, formatting, and organizing data',
    'Creating Excel sheets or other data visualization tools',
    'Identifying trends and patterns in the data',
    'Collaborating with other teams',
    'Continuously monitoring and updating the data set'],
    'Percentage': ['20', '20', '20', '20', '10', '10']}
    """
    skills_percent = {"Skills": [], "Percentage": []}
    for text in response:
        text = text.replace('\n', '')
        for line in text.split('%'):
            if line == '':
                pass
            else:
                skill, percentage = line.split(': ')
                skills_percent["Skills"].append(skill)
                skills_percent["Percentage"].append(percentage)
    return skills_percent

def get_all(response):
    """
    Make a dictionary of programming languages, tools and technical skills. Used to help call_api function. Not for direct use.

    Parameters
    ----------
    response : object 
        response from openai.
        
    Returns
    -------
    dict
        programming languages, tools and technical skills required for job
        
    Examples
    --------
    >>> get_all({
            "finish_reason": "stop",
            "index": 0,
            "logprobs": null,
            "text": "\nRequired Programming Languages: Python, SQL\nTools: Big Query/Snowflake/Redshift, Kafka, Airflow/other\nTechnical Skills: Data Analysis, Data Transformation, Data Visualization, Statistical Analysis, Data Cleaning/Transformation, Multi-Omic Data Integration, Metabolic Modeling/Engineering, Machine Learning, Big-Data Technologies."
        })
    
    {'Skills': ['Collecting and analyzing data',
    'Cleaning, formatting, and organizing data',
    'Creating Excel sheets or other data visualization tools',
    'Identifying trends and patterns in the data',
    'Collaborating with other teams',
    'Continuously monitoring and updating the data set'],
    'Percentage': ['20', '20', '20', '20', '10', '10']}
    """
    text = response["choices"][0]["text"]

    if "Required Programming Languages:" in text:
        programming_languages = text.split("\nRequired Programming Languages: ")[1].split("\n")[0]
    elif "Programming Languages:" in text:
        programming_languages = text.split("Programming Languages: ")[1].split("\n")[0]
    else:
        programming_languages = None

    if "Tools:" in text:
        tools = text.split("Tools: ")[1].split("\n")[0]
    else:
        tools = None

    if "Technical Skills:" in text:
        technical_skills = text.split("Technical Skills: ")[1]
    else:
        technical_skills = None
    
    result = {"Programming Languages": [programming_languages],
                "Tools": [tools],
                "Technical Skills": [technical_skills]}

    return result


def call_api_skills_percent(api_key, job_description):
    """
    Call api and return Skills needed with Percentages.

    Parameters
    ----------
    api_key : str 
        api key for openai API
    job_description : str
        description of the job
        
    Returns
    -------
    dict
        skills required for job with percentage
        
    Examples
    --------
    >>> call_api_skills_percent("sk-ASCNHswueQ", "Job Description")
    
    {'Skills': ['Collecting and analyzing data',
    'Cleaning, formatting, and organizing data',
    'Creating Excel sheets or other data visualization tools',
    'Identifying trends and patterns in the data',
    'Collaborating with other teams',
    'Continuously monitoring and updating the data set'],
    'Percentage': ['20', '20', '20', '20', '10', '10']}
    """
    openai.api_key = api_key
    pre_prompt = """Based on the job description identify the required skills in percentage of 100. 
                Job Description:
                """
    post_prompt = """
                Give the answer like this-
                Skill: Percentage:"""
    prompt = pre_prompt + job_description + post_prompt

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            temperature=0.1,
            prompt=prompt,
            max_tokens=100)
        response = get_skills(response)
        result = skills_percentage(response)
        return result

    except openai.error.APIError as e:
        #Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass

    except openai.error.APIConnectionError as e:
        #Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass

    except openai.error.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass

def call_api_tech_skills(api_key, job_description):
    """
    Call api and return Techincal Skills.

    Parameters
    ----------
    api_key : str 
        api key for openai API
    job_description : str
        description of the job
        
    Returns
    -------
    dict
        programming languages, tools and technical skills required for job
        
    Examples
    --------
    >>> call_api_tech_skills("sk-ASCNHswueQ", "Job Description")
    
    {'Programming Languages': ['SQL, Python'],
    'Tools': ['Excel, Data Visualization Tools'],
    'Technical Skills': ['Data Analysis, Data Cleaning, Data Formatting, Data Organization, Data Visualization, Trend and Pattern Identification, Insights and Recommendations, Collaboration, Data Monitoring and Updating.']}
    """
    openai.api_key = api_key
    pre_prompt = """Based on the job description identify the required Programming Languages, tools and technical skills.
                Job Description:
                """
    post_prompt = """
                Answer:
                """
    prompt = pre_prompt + job_description + post_prompt

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            temperature=0.1,
            prompt=prompt,
            max_tokens=100)
        result = get_all(response)
        return result

    except openai.error.APIError as e:
        #Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass

    except openai.error.APIConnectionError as e:
        #Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass

    except openai.error.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass


def get_questions(response):

    """
    Call API and return relevant interview questions based off skills.

    Parameters
    ----------
    response : JSON object 
        This is openAI's generated response
        
    Returns
    -------
    List
        List of interview questions
        
    Examples
    --------
    >>> <OpenAIObject text_completion id=cmpl-6f1QmrpX11fDYEG01hTsiBrkyF7vc at 0x1036c43b0> JSON: {
        "choices": [
            {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": null,
            "text": "\n\n1. How have you used data to identify trends and patterns in the past?\n
                        2. Describe your experience with creating Excel sheets or other data visualization tools.\n
                        3. What techniques do you use to clean, format, and organize data?\n
                        4. How do you collaborate with other teams when working with data?\n
                        5. What processes do you use to continuously monitor and update data sets?"
            }
        ],
        "created": 1675234968,
        "id": "cmpl-6f1QmrpX11fDYEG01hTsiBrkyF7vc",
        "model": "text-davinci-003",
        "object": "text_completion",
        "usage": {
            "completion_tokens": 83,
            "prompt_tokens": 81,
            "total_tokens": 164
        }
        }
    
        ['How have you used data to identify trends and patterns in the past?',
        'Describe your experience with creating Excel sheets or other data visualization tools',
        'What strategies do you use to clean, format, and organize data?',
        'How do you collaborate with other teams when working with data?',
        'What techniques do you use to continuously monitor and update data sets?']

    """
    
    text = response["choices"][0]["text"]
    questions = text.strip().split("\n")
    questions = [q.split(".")[1].strip() for q in questions if q]
    return questions

def get_question_answers(response):

    """
    Call API and return relevant interview questions responses based off skills.

    Parameters
    ----------
    response : JSON object 
        openAI's generated response
        
    Returns
    -------
    List
        List of interview question responses
        
    Examples
    --------
    >>> <OpenAIObject text_completion id=cmpl-6f3F1O1kNGcog29AzyeqLsxTvigWV at 0x1274d8860> JSON: {
        "choices": [
            {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": null,
            "text": "\n\n1. 'I have used data collection and analysis to inform decisions when I worked on a project that involved gathering customer feedback from surveys. I analyzed the survey responses, combined it with other data points and drew insights to inform strategy for improving customer service.'\n\n
                        2. 'I have extensive experience with cleaning, formatting and organizing data. I'm well-versed in using common data transformation tools, such as Excel and SQL, to restructure raw data into more meaningful and actionable information.'\n\n
                        3. 'I am proficient in using Excel to create sheets and other data visualization tools. I'm comfortable creating dynamic visualizations that effectively present key insights, such as pie charts, bar graphs, and line graphs.'\n\n
                        4. 'I have identified trends and patterns in data by using techniques such as data mining, cluster analysis, and regression analysis. As an example, I worked on a project where I examined customer sales data to identify buying trends among different age groups.'\n\n
                        5. 'I have worked with other teams to utilize data sets by providing support to decision makers, identifying areas of potential benefit or risk and providing insights on potential strategies or solutions. I have experience in automating processes, such as extracting data from systems, databases, and external sources, which enables us to quickly obtain the data needed to make informed decisions.'"
            }
        ],
        "created": 1675241927,
        "id": "cmpl-6f3F1O1kNGcog29AzyeqLsxTvigWV",
        "model": "text-davinci-003",
        "object": "text_completion",
        "usage": {
            "completion_tokens": 271,
            "prompt_tokens": 100,
            "total_tokens": 371
        }
        }
    
        ["1. 'I have used data collection and analysis to inform decisions when I worked on a project that involved gathering customer feedback from surveys. I analyzed the survey responses, combined it with other data points and drew insights to inform strategy for improving customer service.'",
        "2. 'I have extensive experience with cleaning, formatting and organizing data. I'm well-versed in using common data transformation tools, such as Excel and SQL, to restructure raw data into more meaningful and actionable information.'",
        "3. 'I am proficient in using Excel to create sheets and other data visualization tools. I'm comfortable creating dynamic visualizations that effectively present key insights, such as pie charts, bar graphs, and line graphs.'",
        "4. 'I have identified trends and patterns in data by using techniques such as data mining, cluster analysis, and regression analysis. As an example, I worked on a project where I examined customer sales data to identify buying trends among different age groups.'",
        "5. 'I have worked with other teams to utilize data sets by providing support to decision makers, identifying areas of potential benefit or risk and providing insights on potential strategies or solutions. I have experience in automating processes, such as extracting data from systems, databases, and external sources, which enables us to quickly obtain the data needed to make informed decisions.'"]

    """
    
    text = response["choices"][0]["text"]
    responses = text.split("\n\n")
    responses = [response.strip() for response in responses if response]
    return responses


def call_api_questions(api_key, skills):

    """
    Call api and return interview questions.

    Parameters
    ----------
    api_key : str 
        api key for openai API
    Skills : List
        skills extracted from the job description
        
    Returns
    -------
    list
        list of interview questions

    Examples
    --------
    >>> call_api_questions("sk-ASCNHswueQ", "List[skills]")
    
    ['How do you go about collecting and analyzing data?',
    'What techniques do you use to clean, format and organize data?',
    'How do you create Excel sheets or other data visualization tools?']
    """
    openai.api_key = api_key
    pre_prompt = """Given the list of skills: """
    post_prompt = """Return 5 relevant interview questions."""
    prompt = pre_prompt + str(skills) + post_prompt

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            temperature=0.2,
            prompt=prompt,
            max_tokens=200)

        return get_questions(response)

    except openai.error.APIError as e:
        #Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass

    except openai.error.APIConnectionError as e:
        #Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass

    except openai.error.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass

def call_api_answers(api_key, questions):

    """
    Call api and return suggested answers to interview questions.

    Parameters
    ----------
    api_key : str 
        api key for openai API
    Questions : List
        Interview questions extracted from openAI
        
    Returns
    -------
    list
        list of AI suggested interview question repsonses 

    Examples
    --------
    >>> call_api_answers("sk-ASCNHswueQ", "List[Questions]")
    
    ['How do you go about collecting and analyzing data?',
    'What techniques do you use to clean, format and organize data?',
    'How do you create Excel sheets or other data visualization tools?']

    """
    openai.api_key = api_key
    pre_prompt = """Given the list of potential data science interview questions: """
    post_prompt = """Return a relevant response to each interview question"""
    prompt = pre_prompt + str(questions) + post_prompt

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            temperature=1,
            prompt=prompt,
            max_tokens=1000)

        # return response
        return get_question_answers(response)

    except openai.error.APIError as e:
        #Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass

    except openai.error.APIConnectionError as e:
        #Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass

    except openai.error.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass

def call_api_interview(api_key, skills):
    """
    Call functions that out put interview question and answers

    Parameters
    ----------
    api_key : str 
        api key for openai API
    Skills : Nested List
        A single list containing a list of skills for each job description
        
    Returns
    -------
    Data Frame
        a pandas data frame containing questions and answers

    Examples
    --------
    >>> call_api_interview("sk-ASCNHswueQ", "List[[skills],[skills],[skills],...]")
    
    [Questions] [Responses]
    [Q1]        [R1]
    [Q2]        [R2]
    [...]       [...]


    """
    questions = []
    answers = []
    for item in skills:
        q = call_api_questions(api_key, item)
        questions =  questions + q
        answers = answers  + call_api_answers(api_key, q)

    dictionary = {
        "Questions": questions,
        "Responses": answers
    }

    df = pd.DataFrame.from_dict(dictionary)
    return df


# this will take the dictionary from the skills output, turn it into a df and make a visual using altair
# should the user be manually inputting the dictoianry from the output or we make another api call in this function or even pass the output 
# from call_api_tech_skills and this function in that one? 

def visualize_tools(dictionary):

    #explode the df by the languages and tools
    df = pd.DataFrame.from_dict(dictionary)
    boom_lang = df.explode("Programming Languages")
    boom_tools = df.explode("Tools")        


    chart =  (alt.Chart(boom_lang).mark_bar().encode(
        alt.X('count()'),
        alt.Y('Programming Languages', sort='x')

    )) | (alt.Chart(boom_tools).mark_bar().encode(
        alt.X('count()'),
        alt.Y('Tools', sort='x')

    ))

    return chart

