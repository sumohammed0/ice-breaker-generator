# Ice Breaker

Flask app that generates an Ice Breaker to use to connect with someone based on their LinkedIn profile data. 

After entering a name, Ice-Breaker-Generator will find their LinkedIn url using Tavily Search API, scrape LinkedIn data using Proxycurl API. Then it will utilize Langchain to generate a short summary, interesting facts, and an ice breaker to use.

To run:
`python app.py`

Tech Stack:
Langchain, OpenAI, Flask, Proxycurl API, Tavily Search API
