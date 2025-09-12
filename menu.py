from tkinter import *
import json

class Menubar:
    def set_menubar(w):
        menubar = Menu(w)
        w.config(menu=menubar)
        return menubar

    def set_classmenu(menubar):
        classmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Class", menu=classmenu)

        with open("classes.json", "r") as file:
            classes = json.load(file)

        for class_ in sorted(classes, key=lambda x: x['section']):
            classmenu.add_command(label=f"{class_['section']} | {class_['course']}")
    
    def set_editmenu(menubar): 
        editmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Add Class")
        editmenu.add_command(label="Add Student")
        editmenu.add_command(label="Remove Class")
        editmenu.add_command(label="Remove Student")

    def set_settingmenu(menubar):
        settingMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Setting", menu=settingMenu)
        settingMenu.add_command(label="Grading System")
        settingMenu.add_command(label="Theme")
