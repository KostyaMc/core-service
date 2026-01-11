from fastapi import FastAPI, HTTPException


app = FastAPI()


tasks = []


@app.get("/tasks")
async def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    if task_id >= len(tasks) or task_id < 0:
        raise HTTPException(status_code=404, detail="Not found")
    return tasks[task_id]
        
        
@app.post("/tasks")
async def create_task(task: dict):
    task_id = len(tasks)
    new_task = {
        "id": task_id,
        "task": task["task"]
    }
    
    tasks.append(new_task)
    return new_task