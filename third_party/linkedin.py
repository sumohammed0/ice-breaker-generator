import os
import requests
#from dotenv import load_dotenv

# takes linkedin profile url and uses proxycurl api to help scrape linkedin information
def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from linkedin profiles, 
    Manually scrape the information from the linkedin profile"""

    if mock: # use static file stores in github 
        linkedin_profile_url = 'https://gist.githubusercontent.com/sumohammed0/e71fb935d34c2047035a0a81d57b1672/raw/f54fdf0ca6bf9a2a3b6d7abd45953588ee0caf4a/s-m.json'
        response = requests.get(linkedin_profile_url, timeout=10)

    else: # call proxycurl api
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        header_dic = {'Authorization': 'Bearer ' + os.environ.get("PROXYCURL_API_KEY")}
        params = {
            'linkedin_profile_url': linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params, headers=header_dic,
            timeout=10,)
    
    # response to dictionary
    data = response.json()

    # keep pairs if the values is not empty and if the pair is a necessary field
    data = {
        k: v for k, v in data.items() if v not in ([], "", '', None) and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data

if __name__ == '__main__':
    print(
        scrape_linkedin_profile('https://www.linkedin.com/in/eden-marco/?originalSubdomain=il', mock=True)
    )