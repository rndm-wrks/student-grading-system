from tkinter import *
from menu import Menubar as M

# make this tomorrow
# ------------------------------------------------------------------------------------------
# | Prelim | Midterm | Final |
# ------------------------------------------------------------------------------------------
# | * Attendance * | Recitation | Groupings | Grades | Summary |
# ------------------------------------------------------------------------------------------
# | Students                    | Week 1 | Week 2 | Week 3 | Week 4 | Week 5 | Exam | 
# | Caampued, John Kyle         |    /   |    -   |    -   |        |        |      |
# | Manicane, John Warren D.    |    /   |    /   |    -   |        |        |      |
# |                             |  Save  |  Edit  |  Edit  |  Edit  |  Edit  | Edit |
# |                             | Cancel |        |        |        |        |      |




def main():
    w = Tk()
    # SET WINDOW
    set_window(w)
    
    # SET MENU BAR
    m = M.set_menubar(w)
    M.set_classmenu(m)
    M.set_editmenu(m)
    M.set_settingmenu(m)
    
    w.mainloop()


def set_window(w):
    w.geometry("1024x512")
    w.title("Student Grading System")
    


if __name__ == "__main__":
    main()