from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="Test Web App")

# Mount static files and configure templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


class EchoRequest(BaseModel):
    message: str


@app.get("/api/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/api/echo")
def echo(payload: EchoRequest) -> dict:
    return {"echo": payload.message}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "FastAPI Test App"},
    )