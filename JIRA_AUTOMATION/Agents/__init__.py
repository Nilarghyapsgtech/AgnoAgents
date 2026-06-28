from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb



db=SqliteDb(db_file="Context_DB/memory.db")
model=OpenAIChat(id="gpt-5.4-mini")