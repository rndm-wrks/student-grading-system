from tkinter import *

with open("classes.json", "r") as file:
    classes = 


window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

classMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Class", menu=classMenu)
for class_ in classes:
    classMenu.add_command(label=f"{class_['section']} | {class_['course']}")
    
editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Add Student")
editMenu.add_command(label="Add Class")
editMenu.add_command(label="Remove Student")
editMenu.add_command(label="Remove Class")

settingMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Setting", menu=settingMenu)

window.geometry("1024x512")
window.title("Student Grading System")
window.mainloop()

def main():
    ...

if __name__ == "__main__":
    main()