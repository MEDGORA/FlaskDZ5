from fastapi import FastAPI
from uvicorn import run

from app1 import app1

#http://127.0.0.1:8000/tasks/add/?task_id=3&title=Task&description=simple_task&status=done

app = FastAPI()
app.mount(path='/', app=app1)

if __name__ == "__main__":
    run("main:app", host='127.0.0.1', port=8000, reload=True)