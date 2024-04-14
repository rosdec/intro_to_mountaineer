from mountaineer.database import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime

class BlogPost(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)

    text: str
    data: str = datetime.now().isoformat()
