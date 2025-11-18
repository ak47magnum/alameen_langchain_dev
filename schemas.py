from typing import List

from pydantic import BaseModel, Field


class Source(BaseModel):
    """
    Schema for the source used by the agent.
    """

    source_url: str = Field(description="The url of the source")


class AgentResponse(BaseModel):
    """
    Schema for the agent's response with answer and sources.
    """

    answer: str = Field(description="The answer to the query")
    sources: List[Source] = Field(
        default_factory=list, description="The sources used to answer the query"
    )  ## The Source class in List[Source], is defined above..
