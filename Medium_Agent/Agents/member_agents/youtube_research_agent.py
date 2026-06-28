from agno.agent import Agent
from agno.tools.youtube import YouTubeTools
from Agents import model
from lib.instructions.youtube_instructions import YOUTUBE_INSTRUCTIONS
youtube_research_model=model

youtube_research_agent=Agent(
    name="youtube_research_agent",
    id="agent_7",
    model=youtube_research_model,
    instructions=YOUTUBE_INSTRUCTIONS,
    role="Agent to access captions and metadata of YouTube videos",
    tools=[YouTubeTools()],
    add_datetime_to_context=True
)

youtube_research_agent.print_response("Cow videos",markdown=True,stream=True)