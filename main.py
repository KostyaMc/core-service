from fastapi import FastAPI, HTTPException

from config import TaskModel, TaskUpdate


app = FastAPI()


tasks = []

# получить все задачи
@app.get("/tasks")
async def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    if task_id >= len(tasks) or task_id < 0:
        raise HTTPException(status_code=404, detail="Not found")
    return tasks[task_id]
        
        
@app.post("/tasks")
async def create_task(task: TaskModel):
    task_id = len(tasks)
    new_task = {
        "id": task_id,
        "task": task.task
    }
    
    tasks.append(new_task)
    return new_task


# частичное обновление задачи
@app.patch("/tasks/{task_id}")
async def update_task(task_id: int, task: TaskUpdate):
    if task_id >= len(tasks) or task_id < 0:
        raise HTTPException(status_code=..., detail="Task not found")
    else:
        if task.task is None:
            raise HTTPException(status_code=400)
        else:
            tasks[task_id]["task"] = task.task
            return tasks[task_id]