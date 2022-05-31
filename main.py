from fastapi import FastAPI
import time

import convert

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/test")
async def say_hello():
    start = time.time()
    convert.convert_to("/home/cong/Downloads/3.docx", "pdf")
    # time.sleep(3)
    end = time.time()
    print(end - start)
    return end-start
