from fastapi import FastAPI, Form


app = FastAPI()                                             

print("Hello, world")

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




@app.get("/todos/{todo_id}")
def get_item(todo_id: int):
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            return todo


@app.get("/todos")
def return_todo():
    return all_todos



@app.post("/todos")
def get_todo(todo: dict):
    new_id = len(all_todos) + 1
    new_todo_list = {
        "todo_id" : new_id,
        "todo_name" : todo["todo_name"],
        "todo_description" : todo["todo_description"]
    }

    all_todos.append(new_todo_list)
    return all_todos


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            todo["todo_name"] = updated_todo["todo_name"]
            todo["todo_description"] = updated_todo["todo_description"]
            return todo
    return "Error, not found"
    


