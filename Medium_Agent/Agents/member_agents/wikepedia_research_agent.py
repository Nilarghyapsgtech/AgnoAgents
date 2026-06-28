from agno.agent import Agent
from agno.tools.wikipedia import WikipediaTools
from Agents import model
from lib.instructions.wikipedia_instructions import WIKIPEDIA_AGENT

wikipedia_search_model=model

wikipedia_search_agent=Agent(
    name="wikipedia_search_agent",
    id="agent_5",
    model=wikipedia_search_model,
    tools=[WikipediaTools()],
    instructions=WIKIPEDIA_AGENT,
    role="An Agent to search wikipedia",
    add_datetime_to_context=True
)