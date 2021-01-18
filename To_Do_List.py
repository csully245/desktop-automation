import tkinter as tk
import json
from datetime import date

def add_todo_list(todo_list):
    ''' Adds new todo list to todo list file '''
    with open("todo.json", "r") as read_file:
        data = json.load(read_file)
    timestamp = date.today().strftime("%d %b, %Y")
    data.update({timestamp : todo_list})
    with open("todo.json", "w") as write_file:
        json.dump(data, write_file)
        
def get_todo_today():
    with open("todo.json", "r") as read_file:
        data = json.load(read_file)
    timestamp = date.today().strftime("%d %b, %Y")
    return data[timestamp]

class Todo_Screen(tk.Frame):
    ''' Frame for displaying and editing to-do lists '''
    def display_todo(self):
        ''' Displays to-do list on screen '''
        todo_list = get_todo_today()
        todo_list_tk = []
        for todo in todo_list:
            lbl = tk.Label(self.fr_main, text=todo)
            todo_list_tk.append(lbl)
            lbl.pack()

    def edit_lists(self):
        ''' Opens tool to edit to-do lists '''
        print("Called edit_lists()")
    
    def __init__(self, master, **options):
        tk.Frame.__init__(self, master, **options)
        
        lbl_title = tk.Label(self, text="To Do Bot\n")
        lbl_title.grid(row=0, column=0, columnspan=2)

        btn_display = tk.Button(self, text="See Today's List",
                                command=lambda: self.display_todo())
        btn_display.grid(row=1, column=0)

        btn_edit = tk.Button(self, text="Edit lists",
                             command=lambda: self.edit_lists())
        btn_edit.grid(row=1, column=1)
        
        self.fr_main = tk.Frame(self)
        self.fr_main.grid(row=2, column=0, columnspan=2)
    
def test():
    app = tk.Tk()
    fr_todo = Todo_Screen(app)
    fr_todo.pack()
    app.mainloop()
