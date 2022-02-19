from http.client import HTTPException
from fastapi import FastAPI
from os import environ
import tarantool
import logging
import http

logging.basicConfig(
    filename='backend.log',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s:%(message)s',
    level=logging.DEBUG
)

logger=logging.getLogger(__name__)

logger.info("started")

spaces = {
    "student": "student_space",
    "teacher": "teacher_space",
    "parent": "parent_space",
    "event": "event_space",
    "subject": "subject_space",
}

env = {
    "host": environ['TARANTOOL_HOST'],
    "port": environ['TARANTOOL_PORT'],
    "user": environ['TARANTOOL_USER'],
    "password": environ['TARANTOOL_PASSWORD'],
}
logger.info("loaded variables:")
logger.info(f" > host: {env['host']}")
logger.info(f" > port: {env['port']}")
logger.info(f" > user: {env['user']}")

app = FastAPI()
tarantool.connect(
    host=env["host"],
    port=env["port"],
    user=env["user"],
    password=env["password"]
)

@app.post("/")
async def create_entity(space: str):
    if space not in spaces:
        raise HTTPException(status_code=406, detail="wrong space")

    
    return {"message": "Hello World"}

@app.get("/")
async def get_entity(space: str, id_: int):
    if space not in spaces:
        raise HTTPException(status_code=406, detail="wrong space")
    
    return {"message": f"{space} : {id_ + id_}"}

@app.get("/xls")
async def get_xls(space: str, id_: int):
    return {"message": f"{space} : {id_ + id_}"}
