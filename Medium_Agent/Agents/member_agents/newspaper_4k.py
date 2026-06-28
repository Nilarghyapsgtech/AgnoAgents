from agno.agent import Agent
from agno.tools.newspaper4k import Newspaper4kTools
from Agents import model
from lib.instructions.newspaper_instructions import NEWSPAPER_INSTRUCTIONS

newspaper_model=model

newspaper_agent=Agent(
    name="newspaper_agent",
    id="agent_4",
    model=model,
    tools=[Newspaper4kTools(include_summary=True)],
    add_datetime_to_context=True,
    instructions=NEWSPAPER_INSTRUCTIONS,
    role="Agent to read news articles using the Newspaper4k library"
)