from pydantic import BaseModel,Field
from typing import Optional

class Student(BaseModel):
    key_themes=list[str]=Field(description="write down all the key themes discussed in the review in a list")
    summary:str=Field(description="A brief summary of the Review")
    