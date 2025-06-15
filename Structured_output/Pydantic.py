from pydantic import BaseModel,Field
from typing import Optional

class Student(BaseModel):
    key_themes=list[str]=Field(description="write down all the key themes discussed in the review in a list")
    summary:str=Field(description="A brief summary of the ")
    name: str='Anirban'
    age:Optional[int]=None
    cgpa:float=Field(gt=0,lt=10)


new_student={'age':32}
student=Student(**new_student)
print(student)