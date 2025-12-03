from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

# Serve static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class Order(BaseModel):
    name: str
    address: str
    product: str


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Example data that will be rendered in the page
    return templates.TemplateResponse(
        "index.html", {"request": request, "message": "Hello from FastAPI!"}
    )


@app.post("/api/submit")
async def submit(order: Order):
    # In a real app you would validate/save/process here
    response = {"status": "ok", "received": order.dict()}
    return JSONResponse(response)


@app.get("/api/status")
async def status():
    return {"status": "running"}
