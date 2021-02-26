# Developed by Cate Sullivan

import tkinter as tk
from PIL import ImageGrab
import numpy
import pyautogui
import time

# Fill out and complete the OH form
def fill_form():
    global location_pos
    global description_pos
    global button_pos
    global text_location
    global text_description
    
    pyautogui.click(location_pos)
    pyautogui.click(location_pos)
    pyautogui.write(text_location)
    pyautogui.click(description_pos)
    pyautogui.write(text_description)
    pyautogui.click(button_pos)

# Get position and color of OH button
location_pos = 0, 0
description_pos = 0, 0
button_pos = 0, 0
status = "getting location box"
base_color = (0, 0, 0)
def get_form(event=None):
    global location_pos
    global description_pos
    global button_pos
    global base_color
    global root
    global lbl
    global status

    if (status == "getting location box"):
        location_pos = pyautogui.position()
        lbl.pack_forget()
        text="Move your mouse over the 'Description' box and press 'Enter'"
        lbl = tk.Label(root, text=text)
        lbl.grid(row=2, column=0, columnspan=2)
        status = "getting description box"

    elif (status == "getting description box"):
        description_pos = pyautogui.position()
        lbl.pack_forget()
        text="Move your mouse over the 'Request Help' button and press 'Enter'"
        lbl = tk.Label(root, text=text)
        lbl.grid(row=2, column=0, columnspan=2)
        status = "getting button"

    elif (status == "getting button"):
        button_pos = pyautogui.position()
        img = ImageGrab.grab()
        base_color = img.getpixel(button_pos)
        root.destroy()
        status = "done"

# Check if the status of the button has changed
def check_changed(event=None):
    global button_pos
    global base_color
    #current_pos = pyautogui.position()
    #pyautogui.moveTo(button_pos)
    img = ImageGrab.grab()
    #pyautogui.moveTo(current_pos)
    color = img.getpixel(button_pos)
    if (color != base_color):
        fill_form()
        return True
    else:
        return False

text_location = ""
text_description = ""
def save_text(event=None):
    global root
    global lbl_entry_a
    global entry_location
    global lbl_entry_b
    global entry_description
    global fr_pos
    global btn_save_text
    global text_location
    global text_description
    global lbl

    text_location = entry_location.get()
    text_description = entry_description.get()

    lbl_entry_a.grid_forget()
    lbl_entry_b.grid_forget()
    entry_location.grid_forget()
    entry_description.grid_forget()
    btn_save_text.grid_forget()
    text="Move your mouse over the 'Location' box and press 'Enter'"
    lbl = tk.Label(root, text=text)
    lbl.grid(row=2, column=0, columnspan=2)
    fr_pos.focus()
    
    
# GUI
root = tk.Tk()
root.title("OHQ")

lbl_entry_a = tk.Label(root, text="Location Box Text:")
lbl_entry_a.grid(row=0, column=0)
entry_location = tk.Entry(root, width=40)
entry_location.grid(row=0, column=1)

lbl_entry_b = tk.Label(root, text="Description Box Text:")
lbl_entry_b.grid(row=1, column=0)
entry_description = tk.Entry(root, width=40)
entry_description.grid(row=1, column=1)

btn_save_text = tk.Button(root, text="Save Text", command=save_text)
btn_save_text.grid(row=2, column=0, columnspan=2)

lbl = tk.Label(root, text="placeholder")

fr_pos = tk.Frame(root)
fr_pos.bind('<Return>', get_form)
fr_pos.grid(row=4, column=0)

root.mainloop()

# Main loop
dt = 1
last = time.perf_counter()
while True:
    now = time.perf_counter()
    if (now - last > dt):
        completed = check_changed()
        if (completed):
            break
        last = now
