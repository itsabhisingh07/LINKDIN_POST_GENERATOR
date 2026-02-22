from typing import TypedDict, Literal
from pydantic import BaseModel, Field

# 1. The main State of the graph
class LinkPost(TypedDict):
    topic: str
    post: str
    evaluation: Literal["approved", "needs_improvement"]
    feedback: str
    iteration: int
    max_iterations: int

# 2. The Structured Output for the Evaluator
class PostEvaluation(BaseModel):
    evaluation: Literal["approved", "needs_improvement"]
    feedback: str = Field(..., description="feedback for the post")