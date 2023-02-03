#!/usr/bin/env python
# coding: utf-8
import pandas as pd

def scrape_job_description(job_array):
    
    """
    short desc.

    Parameters
    ----------
    job_array : list
    job links
        
    Returns
    -------
    pandas dataframe
        job link, job description, job title, job location
        
    Examples
    --------
    >>> scrape_job_description(input)
    input:
    ['https://www.linkedin.com/jobs/view/3442691887',
     'https://ca.linkedin.com/jobs/view/lead-software-engineering-decision-management-platform-at-mastercard-3378359650']
    output:
    Job URL|Job Description|Job Title|Job Location
0|https://ca.linkedin.com/jobs/view/lead-software|Our PurposeWe ...|Mastercard hiring Lead, Software Eng..|Vancouver, British Columbia, Canada|
1|https://www.linkedin.com/jobs/view/3442691887|Company Description...|Dropbox hiring Director of Data S..|Vancouver, British Columbia, Canada|
    
    """
    #create beautifulsoup object
    #process job url by url and scrape job description if url is valid
    #if url not valid, display error. open.ai is expected to skip these entries

    #also get title related information
    inputarr=job_array
    job_desc_lst=list()
    job_title_lst=list()
    job_loc_lst=list()
    titstr=list()

    for job in inputarr:
        
        try:
            url=job
            get_info = requests.get(url)
            if get_info.status_code == 200:
                #process and get job desc
                get_jd_info = BeautifulSoup(get_info.text)
                trim_jd=get_jd_info.select('div')
                
                job_desc=trim_jd[85].text.replace('\n','')

                job_desc_lst.append(job_desc)
                
                #Get job title, city and country
                title=get_jd_info.title.string
                title,_=title.split('|')
                titstr=title.rsplit('in ',)
                job_title_lst.append(titstr[0])
                job_loc_lst.append(titstr[1])
            else:
                job_desc_lst.append("Invalid URL, analysis skipped")
                job_title_lst.append("")
                job_loc_lst.append("")

        except:
            #Handle exceptions with processing
            print(f"Error, analysis skipped for this job")
            job_desc_lst.append("Invalid URL, analysis skipped")
            job_title_lst.append("")
            job_loc_lst.append("")


    #build pandas dataframe as output of scraped and parsed data

    df1 = pd.DataFrame(list(zip(inputarr, job_desc_lst,job_title_lst,job_loc_lst)), columns = ["Job URL","Job Description","Job Title","Job Location"])
    


    return df1

