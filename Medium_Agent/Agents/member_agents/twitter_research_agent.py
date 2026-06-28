from agno.agent import Agent
from agno.tools.x import XTools
from Agents import model
from lib.instructions.twitter_instructions import TWITTER_AGENT_INSTRUCTIONS
from dotenv import load_dotenv

load_dotenv("/Users/nilasark/AGNO_PROJECTS/Medium_Agent/.env")

x_research_model=model

x_research_agent=Agent(
    name="x_research_agent",
    id="agent_6",
    model=x_research_model,
    tools=[XTools(wait_on_rate_limit=True,include_post_metrics=True)],
    instructions=TWITTER_AGENT_INSTRUCTIONS,
    role="Agent to interact with X",
    add_datetime_to_context=True
)

x_research_agent.print_response("Latest tweets about MOdi",markdown=True,stream=True)