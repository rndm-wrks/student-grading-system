from tkinter import *
import json

# m = menubar 


class Menubar:
    def set_menubar(cls, w):
        m = Menu(w)
        w.config(menu=m)
        cls.set_classmenu(m)
        cls.set_editmenu(m)
        cls.set_settingmenu(m)

    def open_class(class_name):
        print(f"{class_name} example")
    
    def set_classmenu(m):
        classmenu = Menu(m, tearoff=0)
        m.add_cascade(label="Class", menu=classmenu)

        with open("classes.json", "r") as file:
            classes = json.load(file)

        for class_ in sorted(classes, key=lambda x: x['section']):
            classmenu.add_command(label=f"{class_['section']} | {class_['course']}",
                                  command=lambda x=f"{class_['section']}_{class_['course']}":
                                      )
    
    def set_editmenu(m): 
        editmenu = Menu(m, tearoff=0)
        m.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Add Class")
        editmenu.add_command(label="Add Student")
        editmenu.add_command(label="Remove Class")
        editmenu.add_command(label="Remove Student")

    def set_settingmenu(m):
        settingMenu = Menu(m, tearoff=0)
        m.add_cascade(label="Setting", menu=settingMenu)
        settingMenu.add_command(label="Grading System")
        settingMenu.add_command(label="Theme")
