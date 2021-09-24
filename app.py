# Copyright © 2021 TerminalWarlord
# Encoding = 'utf-8'
# Licensed under MIT License
# https://github.com/TerminalWarlord/

from fastapi import FastAPI
from main import *
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return latestepisodes()




if __name__ == "__main__":
  uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)