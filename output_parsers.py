from typing import List, Dict, Any
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")
    icebreaker: str = Field(description="ice breaker introduction")

    def to_dict(self) -> Dict[str, Any]:
        return { "summary": self.summary, "facts": self.facts, "icebreaker": self.icebreaker}
    
summary_parser = PydanticOutputParser(pydantic_object=Summary)