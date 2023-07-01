from typing import Union

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/hello')
def get_root(request: Request):
    return templates.TemplateResponse('home.html', {"request": request, "message": "hello temlpate"})
