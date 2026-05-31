from fastapi import APIRouter
from models.profile import ProfileResponse, Skill, Project, Qualification

router = APIRouter()


@router.get("/", response_model=ProfileResponse)
def get_profile():
    return ProfileResponse(
        name="Naomi Msafiri Gabagambi",
        title="Portfolio API Developer",
        bio="Experienced backend developer building portfolio APIs and data-driven applications.",
        location="Remote",
        status="Open to opportunities",
        email="naomi@example.com",
        linkedin="https://linkedin.com/in/naomi-gabagambi",
        github="https://github.com/naomi-gabagambi",
        skills=[
            Skill(category="Languages", items=["Python", "JavaScript", "TypeScript"]),
            Skill(category="Frameworks", items=["FastAPI", "React", "Node.js"]),
            Skill(category="Tools", items=["Docker", "Git", "PostgreSQL"]),
        ],
        projects=[
            Project(
                id=1,
                title="Portfolio API",
                description="A personal portfolio backend with profile, metrics, and contact form endpoints.",
                stack=["FastAPI", "Pydantic", "Uvicorn"],
            )
        ],
        qualifications=[
            Qualification(year="2025", title="Portfolio Backend", institution="Self-study"),
        ],
    )
