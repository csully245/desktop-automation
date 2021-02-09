import os
import shutil
import stat
import time
from tkinter import filedialog as fd
import tkinter as tk

'''
This app is used to check which files in a particular folder (typically
Downloads) may be best to delete
'''

class Frame_File(tk.LabelFrame):
    '''
    Frame containing the options for a particular file to manage
    '''
    def delete_file(self):
        os.remove(self.file)
        self.destroy()

    def ignore(self):
        self.destroy()

    def move_file(self):
        new_dir = fd.askdirectory(initialdir="./",
                                        title="Move File: " + self.file)
        shutil.move(self.file, new_dir)
        self.destroy()

    def __init__(self, file, master, **options):
        tk.LabelFrame.__init__(self, master, **options)
        self.file = file

        lbl_file = tk.Label(self, text=file, width=60)
        lbl_file.grid(row=0, column=0)

        btn_del = tk.Button(self, text="Delete",
                            command=lambda: self.delete_file())
        btn_del.grid(row=0, column=1)

        btn_ignore = tk.Button(self, text="Ignore",
                               command=lambda: self.ignore())
        btn_ignore.grid(row=0, column=2)

        btn_move = tk.Button(self, text="Move",
                             command=lambda: self.move_file())
        btn_move.grid(row=0, column=3)
        
        
class Maintenance_Bot:
    '''
    Top-level GUI for handling bloated folders
    '''
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Maintenance Bot")

        title_text = "Maintenance Bot, reporting for duty!\n"
        title_text += "Let's clean up these files."
        self.lbl_title = tk.Label(self.root, text=title_text)
        self.lbl_title.pack()

        self.files = []
        self.fr_files = tk.Frame(self.root)
        self.fr_files.pack()

        self.btn_end = tk.Button(self.root, text="Good Bot! See You Next Week",
                                 command=lambda: self.end())
        self.btn_end.pack(pady=5)

    def start(self):
        ''' Fire the boi up and watch him help! '''
        self.root.mainloop()

    def end(self):
        ''' Duties done! Bot sleepy time. '''
        self.root.destroy()

    def add_file(self, file):
        new_file = Frame_File(file, self.fr_files)
        new_file.pack()
        self.files.append(new_file)

    def add_files(self, files):
        for file in files:
            self.add_file(file)

    def perform_maintenance(self, src, days):
        '''
        Prompts user to delete any files that have not been accessed within a
        certain period

        Input:
        src: string, source directory path
        days: numeral, number of days to check back
        '''
        cwd = os.getcwd()
        os.chdir(src)
        suspect_files = []
        for file in os.listdir():
            time_created = os.path.getctime(file)
            time_last_access = os.stat(file)[stat.ST_ATIME]
            cutoff = time.time() - days * 24 * 60 * 60
            if (min(time_created, time_last_access) < cutoff):
                suspect_files.append(file)
        self.add_files(suspect_files)
        self.start()
        os.chdir(cwd)

def operate():
    cwd = os.getcwd()
    os.chdir("C:\\Users\\jsull\\Desktop\\Programming")
    my_boi = Maintenance_Bot()
    my_boi.perform_maintenance("../../Downloads", 1)
    os.chdir(cwd)
    

operate()
