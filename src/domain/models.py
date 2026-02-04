from datetime import datetime
from typing import List, Optional
from uuid import uuid4
from pydantic import BaseModel, Field

class Highlight(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    text: str
    source_message_id: str
    created_at: datetime = Field(default_factory=datetime.now)

class Message(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    role: str  # 'user', 'assistant', 'system'
    content: str
    model_used: Optional[str] = None
    cost: float = 0.0
    timestamp: datetime = Field(default_factory=datetime.now)

class ChatSession(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str = "New Conversation"
    model_config_name: str = "gpt-4o"
    temperature: float = 0.7
    messages: List[Message] = Field(default_factory=list)
    highlights: List[Highlight] = Field(default_factory=list)

    @property
    def total_cost(self) -> float:
        return sum(m.cost for m in self.messages)