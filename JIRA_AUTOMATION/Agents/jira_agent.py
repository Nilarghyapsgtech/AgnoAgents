from os import getenv
from typing import Any, List, Optional

from agno.agent import Agent
from agno.tools import Toolkit
from agno.tools.jira import JiraTools as AgnoJiraTools
from jira import JIRA
from . import model
from dotenv import load_dotenv
from lib.instructions.jira_instruction import JIRA_INSTRUCTION
from . import db
from lib.tools.tools import JiraTools

load_dotenv(dotenv_path="/Users/nilasark/AGNO_PROJECTS/JIRA_AUTOMATION/.env")


jira_automation_model=model

jira_agent=Agent(
    name="jira_automation_agent",
    id="agent_1",
    model=model,
    tools=[
        JiraTools(
            server_url=getenv("JIRA_SERVER_URL"),
            token=getenv("JIRA_TOKEN"),
        )
    ],
    role="Agent will use Jira API to search for issues in a project",
    add_datetime_to_context=True,
    instructions=JIRA_INSTRUCTION,
    markdown=True
)
