from agno.os import AgentOS
from Agents.leader_agent.orchestrator import orchestrator_agent
from Agents.leader_agent.orchestrator import db

agent_os=AgentOS(
    name="Medium Agent",
    id="agent_8",
    db=db,
    teams=[orchestrator_agent]
)

app=agent_os.get_app()
if __name__ == "__main__":
    agent_os.serve(
        app="main:app",
        reload=True
    )
