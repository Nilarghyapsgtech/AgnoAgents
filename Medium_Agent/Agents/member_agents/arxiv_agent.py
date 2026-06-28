from agno.agent import Agent
from Agents import model
from agno.tools.arxiv import ArxivTools
from lib.instructions.arxiv_instruction import ARXIV_INSTRUCTIONS

arxiv_model=model


arxiv_agent=Agent(
    name='arxiv_research_agent',
    id='agent_1',
    model=model,
    tools=[ArxivTools(download_dir='/Users/nilasark/AGNO_PROJECTS/Medium_Agent/Knowledge_Base')],
    add_datetime_to_context=True,
    instructions=ARXIV_INSTRUCTIONS,
    role="Arxiv Research Assistant"
)