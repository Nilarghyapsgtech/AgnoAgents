from agno.tools.jira import JiraTools as AgnoJiraTools
from typing import Optional,Any,List
from os import getenv
from jira import JIRA
from agno.tools import Toolkit

class JiraTools(AgnoJiraTools):


    DEFAULT_TIMEOUT = None
    DEFAULT_MAX_RETRIES = 3
    DEFAULT_MAX_RETRY_DELAY = 60
    def __init__(
        self,
        server_url:Optional[str]=None,
        token: Optional[str] = None,
        enable_get_issue: bool = True,
        enable_create_issue: bool = True,
        enable_search_issues: bool = True,
        enable_add_comment: bool = True,
        enable_add_worklog: bool = True,
        all: bool = True,
        **kwargs:Any
    ):
        self.server_url=server_url or getenv("JIRA_SERVER_URL")
        self.token=token or getenv("JIRA_TOKEN")

        if not self.server_url:
            raise ValueError("JIRA SERVER URL NOT FOUND")
        if not self.token:
            raise ValueError("JIRA TOKEN NOT FOUND")
        self.jira=JIRA(server=self.server_url,token_auth=self.token)

        tools:List[Any]=[]
        if enable_get_issue or all:
            tools.append(self.get_issue)
        if enable_create_issue or all:
            tools.append(self.create_issue)
        if enable_search_issues or all:
            tools.append(self.search_issues)
        if enable_add_comment or all:
            tools.append(self.add_comment)
        if enable_add_worklog or all:
            tools.append(self.add_worklog)

        Toolkit.__init__(self,name="jira_tools",tools=tools,**kwargs)

    def _ensure_resilient_session_attrs(self):
            session=getattr(self.jira,"_session",None)
            if session is None:
                return
            if not hasattr(session,"timeout"):
                session.timeout=self.DEFAULT_TIMEOUT
            if not hasattr(session,"max_retries"):
                session.max_retries=self.DEFAULT_MAX_RETRIES
            if not hasattr(session,"max_retry_delay"):
                session.max_retry_delay=self.DEFAULT_MAX_RETRY_DELAY

    def get_issue(self,issue_key):
            self._ensure_resilient_session_attrs()
            return super().get_issue(issue_key)
    def create_issue(
            self,
            project_key: str,
            summary: str,
            description: str,
            issuetype: str = "Task",
            ) -> str:
            self._ensure_resilient_session_attrs()
            return super().create_issue(project_key, summary, description, issuetype)

    def search_issues(self, jql_str: str, max_results: int = 50) -> str:
            self._ensure_resilient_session_attrs()
            return super().search_issues(jql_str, max_results)

    def add_comment(self, issue_key: str, comment: str) -> str:
            self._ensure_resilient_session_attrs()
            return super().add_comment(issue_key, comment)

    def add_worklog(
            self,
            issue_key: str,
            time_spent: str,
            comment: Optional[str] = None,
            ) -> str:
            self._ensure_resilient_session_attrs()
            return super().add_worklog(issue_key, time_spent, comment)
    



        