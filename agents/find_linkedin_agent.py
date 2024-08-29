import os

from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool # used to help agents/llms interact with external world
from langchain.agents import (create_react_agent, AgentExecutor,)

def find_profile(name: str):
    return ""