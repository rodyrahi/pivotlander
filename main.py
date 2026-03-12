from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")



app = FastAPI()

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)