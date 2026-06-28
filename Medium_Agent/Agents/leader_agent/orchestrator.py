from Agents import model
from agno.agent import Agent
from pathlib import Path
from member_agents.arxiv_agent import arxiv_agent
from member_agents.hackernews_agent import hackernews_agent
from member_agents.newspaper_4k import newspaper_agent
from member_agents.web_search import web_search_agent
from member_agents.wikepedia_research_agent import wikipedia_search_agent
from agno.team import Team
from agno.tools.local_file_system import LocalFileSystemTools
from lib.instructions.orchestrator_instructions import ORCHESTRATOR_INSTRUCTION
from agno.db.sqlite import SqliteDb


orchestrator_model=model
db=SqliteDb("Memory/agent_memory.db")

target_directory=Path('./articles/')
target_directory.mkdir(exist_ok=True)

orchestrator_agent=Team(
    name="Medium article creation Agent",
    id="agent_8",
    model=orchestrator_model,
    members=[arxiv_agent,hackernews_agent,newspaper_agent,web_search_agent,wikipedia_search_agent],
    instructions=ORCHESTRATOR_INSTRUCTION,
    role="Lead research and content orchestration agent responsible for coordinating multiple specialized research agents and producing well-structured, evidence-based Medium articles.",
    add_datetime_to_context=True,
    add_history_to_context=True,
    tools=[LocalFileSystemTools(target_directory=target_directory,default_extension="md")],
    db=db,
    stream=True,
    markdown=True
)
