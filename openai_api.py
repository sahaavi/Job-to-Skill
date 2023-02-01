import openai
import altair as alt

def get_skills(response):
    """
    Extract only the skills with percentage lines
    from api's response.
    """
    text_list = [choice.text for choice in response['choices']]
    return text_list

def skills_percentage(response):
    """
    Make a dictionary of skills with percentages. 
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

def get_questions(response):
    text = response["choices"][0]["text"]
    questions = text.strip().split("\n")
    questions = [q.split(".")[1].strip() for q in questions if q]
    return questions
    


def call_api(api_key, job_description):
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


#return interview questions based on inputted skills
def call_api_questions(api_key, skills):
    openai.api_key = api_key
    pre_prompt = """Given the list of skills: """
    post_prompt = """Return 5 relevant interview questions."""
    prompt = pre_prompt + str(skills) + post_prompt

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            temperature=0.1,
            prompt=prompt,
            max_tokens=100)

        return get_questions(response)

    except openai.error.APIError as e:
        #Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass

    except openai.error.APIConnectionError as e:
        #Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass

    except openai.CompletionError as e:
        #Handle Completino Error
        print(f"OpenAI API returned a Completion Error: {e}")
        pass

    except openai.error.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass
    
    
    
  
def skills_visual(df):
    pass