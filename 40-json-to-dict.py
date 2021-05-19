from datetime import date
from library.JsonParser import JsonParser


today = date.today()

# YY/mm/dd
ymd = today.strftime("%Y/%m/%d")
print(ymd)
# create a parser
parser = JsonParser()
# load json file
todos = parser.convert_json_to_python("data/todo.json")
# print saved tasks
for todo in todos:
  print(todo)


# add new task
todo = {
  "name": "dummy new task",
  "date": ymd
}
todos.append(todo)
print(todos)

# write new task to todo.json
parser.convert_python_to_json(todos, "data/todo.json")
print(">>>>>> new task saved!")