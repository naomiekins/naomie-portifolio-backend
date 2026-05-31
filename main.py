import fastapi
import fastapi.middleware.cors
from routes import profile, metrics, contact

app = fastapi.FastAPI(
    title="Naomi Msafiri Gabagambi — Portfolio API",
    description="Backend API for portfolio: profile data, live metrics, and contact form.",
    version="1.0.0",
)

ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "https://your-portfolio.vercel.app",  # replace with your Vercel URL later
]

app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile.router, prefix="/api/profile", tags=["Profile"])
app.include_router(metrics.router, prefix="/api/metrics", tags=["Metrics"])
app.include_router(contact.router, prefix="/api/contact", tags=["Contact"])


@app.get("/", tags=["Health"])
def root():
    return {
        "status": "online",
        "message": "Naomi Msafiri Gabagambi — Portfolio API is running.",
        "docs": "/docs",
    }


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
