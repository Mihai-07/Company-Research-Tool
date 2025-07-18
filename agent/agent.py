from langchain.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain import hub
from .tools import Search

react_prompt = hub.pull("hwchase17/react")

template = """
    You are a helpful research assistant who is supposes to find the following
    information about {company} for a website:

    1. Official Name
    2. Ticker
    3. Market Segment
    4. CEO
    5. Founder(s)
    6. Market Cap (in USD)
    7. Revenue (in USD)
    8. Short History
    9. Fun Facts

    Make sure you find all the information mentioned above!

    Your information must be up-to-date! To do so, make sure that, when
    searching for it online, you DO NOT include any years in your query.
    INSTEAD, you should use words like LATEST!

    E.g. 'Latest <what you're looking for> about {company}.'.

    This is what your queries should look like, without including any years!
    
    However, for the first 7 facts, please mention how recent your information
    really is like this:

    E.g Market Cap: <value> as of <year>

    When you are done, your final response should look like this:

    Final Answer: <your answer>
"""

prompt = PromptTemplate(
    input_variables=["company"],
    template=template
)

tools = [
    Tool(
        name=Search.name,
        func=Search.func,
        description=Search.description
    )
]

def create_agent_executor(llm):
    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=react_prompt
    )

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True
    )