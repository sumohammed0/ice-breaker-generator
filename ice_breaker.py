import os 
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from third_party.linkedin import scrape_linkedin_profile

if __name__ == '__main__':
    print("hello LangChain!")
    
    # Define template string for summarizing information
    summary_template = """
        given the Linkedin information {information} about a person I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    # Create a PromptTemplate object
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template) 

    # Initialize ChatOpenAI object
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # Create chain by combining prompt template and langauge model
    chain = summary_prompt_template | llm

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/eden-marco/?originalSubdomain=il', mock=True)
    
    # Invoke chain using scraped LinkedIn data as input
    res = chain.invoke(input={"information": linkedin_data})

    print(res)