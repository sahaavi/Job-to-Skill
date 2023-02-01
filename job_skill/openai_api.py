import openai

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
