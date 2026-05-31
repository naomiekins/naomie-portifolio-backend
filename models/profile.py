from pydantic import BaseModel
from typing import List


class Skill(BaseModel):
    category: str
    items: List[str]


class Project(BaseModel):
    id: int
    title: str
    description: str
    stack: List[str]


class Qualification(BaseModel):
    year: str
    title: str
    institution: str


class ProfileResponse(BaseModel):
    name: str
    title: str
    bio: str
    location: str
    status: str
    email: str
    linkedin: str
    github: str
    skills: List[Skill]
    projects: List[Project]
    qualifications: List[Qualification]
