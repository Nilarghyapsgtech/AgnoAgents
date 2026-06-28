from agno.agent import Agent
from agno.tools.reddit import RedditTools
from Agents import model
from lib.instructions.reddit_instructions import REDDIT_INSTRUCTIONS

reddit_research_model=model

reddit_research_agent=Agent(
    name="reddit_research_agent",
    id="agent_7",
    model=reddit_research_model,
    tools=[RedditTools(include_tools=["get_subreddit_info","get_subreddit_posts","search_subreddits","get_post_details","search_posts"])],
    instructions=REDDIT_INSTRUCTIONS,
    role="Agents to interact with Reddit",
    add_datetime_to_context=True
)