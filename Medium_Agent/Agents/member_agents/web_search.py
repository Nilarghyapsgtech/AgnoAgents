from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from Agents import model
from lib.instructions.duckduckgo_instructions import DUCKDUCKGO_INSTRUCTIONS

web_search_model=model

web_search_agent=Agent(
    name='web_search_agent',
    id='agent_2',
    model=model,
    tools=[DuckDuckGoTools()],
    add_datetime_to_context=True,
    instructions=DUCKDUCKGO_INSTRUCTIONS,
    role="Web Research Assistant",
    
)