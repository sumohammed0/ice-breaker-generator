from langchain_community.tools import TavilySearchResults

def get_profile_url(name: str):
    """searches for linkedin profile page"""
    
    search = TavilySearchResults()
    res = search.run(f"{name} linkedin")

    return res[1]["url"]