from agno.agent import Agent
from agno.tools .hackernews import HackerNewsTools
from lib.instructions.hackernews_instruction import HACKERNEWS_AGENT
from Agents import model

hackernews_model=model

hackernews_agent=Agent(
    name="hackernews-agent",
    id="agent_3",
    model=model,
    tools=[HackerNewsTools()],
    add_datetime_to_context=True,
    instructions=HACKERNEWS_AGENT,
    role="Hackernews Research Agent"
)