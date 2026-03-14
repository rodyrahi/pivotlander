import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )


@app.get("/models")
def read_models():
    models_path = "/static/models"

    if not os.path.exists(models_path):
        return {"error": "models folder not found"}

    files = os.listdir(models_path)

    return {"models": files}


from fastapi.responses import FileResponse
import os

@app.get("/download/{model_name}")
def download_model(model_name: str):
    path = f"/static/models/{model_name}"

    if not os.path.exists(path):
        return {"error": "Model not found"}

    return FileResponse(
        path,
        media_type="application/octet-stream",
        filename=model_name
    )
@app.get("/download/test/build/{build_name}")
def download_build(build_name: str):
    path = f"/static/builds/{build_name}"

    return FileResponse(
        path,
        media_type="application/octet-stream",
        filename=build_name
    )




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)