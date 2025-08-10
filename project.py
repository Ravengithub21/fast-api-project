from fastapi import FastAPI

app = FastAPI()                                             


all_todos = [
        {"todo_id" : 1, "todo_name" : "Sports", "todo_description" : "Go to the gym"},
        {"todo_id" : 2, "todo_name" : "Gaming", "todo_description" : "Playing souls"},
        {"todo_id" : 3, "todo_name" : "Shopping", "todo_description" : "Buy groceries"},
        {"todo_id" : 4, "todo_name" : "Meditate", "todo_description" : "Meditate for 20min"},
        {"todo_id" : 5, "todo_name" : "Running", "todo_description" : "Go for a 1hour run!"}
]


@app.get("/")
def read_root():
    return {"Hello" : "World"}





@app.get("/todos")
def get_todo():
    return all_todos