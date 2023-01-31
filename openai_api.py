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

def call_api(api_key, job_description):
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
    >>> call_api("sk-ASCNHswueQ", "Job Description")
    
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