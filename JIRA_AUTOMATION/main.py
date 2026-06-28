from Agents.jira_agent import jira_agent
from agno.os import AgentOS
from Agents import db

agent_os=AgentOS(
    name="jira_automation_agent",
    id='os_1',
    agents=[jira_agent],
    db=db
)

app=agent_os.get_app()

if __name__=="__main__":
    agent_os.serve(
        app="main:app",
        reload=True
    )