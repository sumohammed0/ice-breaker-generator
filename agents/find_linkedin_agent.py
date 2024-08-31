import os
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool # used to help agents/llms interact with external world
from langchain.agents import (create_react_agent, AgentExecutor)
from langchain import hub

from tools.tools import get_profile_url

def find_profile(name: str):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    template = """given the full name of a person {person_name} I want you to get me a link to their Linkedin profile page. Your answer should contain only a URL"""

    prompt_template = PromptTemplate(template=template, input_variables=["person_name"])

    tools_for_agent  = [
        Tool(
            name = "Crawl Google 4 Linkedin Profile Page",
            func = get_profile_url,
            description = "useful for when you need to get the Linkedin Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react") # reasoning engine for agent 
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt) # sent to llm
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True) # responsible for invoking functions

    result = agent_executor.invoke(input={"input" : prompt_template.format_prompt(person_name=name)})

    # parse result
    linkedin_profile_url = result["output"]
    return linkedin_profile_url

if __name__ == "__main__":
    linkedin_url = find_profile(name="safa mohammed")
    print(linkedin_url)