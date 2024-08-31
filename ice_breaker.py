import os
from typing import Tuple 
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from third_party.linkedin import scrape_linkedin_profile
from agents.find_linkedin_agent import find_profile as linkedin_agent
from output_parsers import summary_parser, Summary

def ice_break_with(name: str) -> Tuple[Summary, str]:
    linkedin_url = linkedin_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url, mock=True)
    
    # Define template string for summarizing information
    summary_template = """
        given the Linkedin information {information} about a person I want you to create:
        1. a short summary
        2. two interesting facts about them
        3. a short one line to use as an icebreaker introduction

        \n{format_instructions}
    """

    # Create a PromptTemplate object
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template, partial_variables={"format_instructions": summary_parser.get_format_instructions()}) 

    # Initialize ChatOpenAI object
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # Create chain by combining prompt template and langauge model
    # chain = summary_prompt_template | llm
    chain = summary_prompt_template | llm | summary_parser
    
    # Invoke chain using scraped LinkedIn data as input
    result: Summary = chain.invoke(input={"information": linkedin_data})

    return result, linkedin_data.get("profile_pic_url")


if __name__ == '__main__':
    print("Ice breaker enter")
    ice_break_with("Safa Mohammed")