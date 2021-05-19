# todo list management app
# using json as data storage
# @2021/05/18

from datetime import date
from library.JsonParser import JsonParser


def welcome():
  print("")
  print("")
  print("******  Welcome to Todo List App  ******")
  print("")
  print("")

  print("1 - View all tasks")
  print("2 - Add new task")
  print("3 - Clear all tasks")
  print("4 - Exit the program")
  print("")

  opt = input("Enter your choice number(1-4): ")
  if opt == "":
    return exitApp()

  user_input = int(opt)

  if user_input == 1:
    viewAll()
  if user_input == 2:
    addNew()
  if user_input == 3:
    clearAll()
  if user_input == 4:
    exitApp()


def exitApp():
    print("")
    print('        Thanks for visiting')
    print("             Goodbye!")
    print("")
    exit()


def _read():
  # create a parser
  parser = JsonParser()
  # load json file
  todos = parser.convert_json_to_python("data/todo.json")
  # print saved tasks
  print("")
  print("--------- MY TODO TASKS ----------")
  for i, todo in enumerate(todos):
    print(f"{i+1} - {todo.get('name')}")
  return todos


def _save(todos):
  # create a parser
  parser = JsonParser()
  # write file
  parser.convert_python_to_json(todos, "data/todo.json")


def viewAll():
  todos = _read()
  print("")
  opt = input("Enter your task number to complete or 0 to return main menu: ")
  if opt == "":
    return exitApp()

  user_input = int(opt)
  if user_input == 0:
    welcome()
  if user_input > len(todos):
    return print("Warning! input number beyond the todo list length!")

  # remove one
  todos.pop(user_input - 1)
  _save(todos)
  print(">>>>>> one task completed!")
  viewAll()


# TODO: ...
# test_list.insert(0, {})
def addNew():
  pass

# TODO: ...
# test_list.clear()
def clearAll():
  pass


# run main function
welcome()
