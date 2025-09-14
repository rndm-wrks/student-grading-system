from tkinter import *
from tkinter import ttk
from menu import Menubar as M
import json

# make column row for the attendance. make new nb or just new window when selecting section.
# shows the current section in top.
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




def make_subnb(parent):
    subnb = ttk.Notebook(parent)
    att = Frame(subnb)
    reci = Frame(subnb)
    grp = Frame(subnb)  
    grd = Frame(subnb)
    summ = Frame(subnb)

    subnb.add(att, text="Attendance")
    subnb.add(reci, text="Recitation")
    subnb.add(grp, text="Groupings")
    subnb.add(grd, text="Grades")
    subnb.add(summ, text="Summary")
    subnb.pack(expand=True, fill="both")

    Label(att, text="Students").grid(row=0, column=0)
    

    
def make_nb(w):
    nb = ttk.Notebook(w)
    pre = Frame(nb)
    mid = Frame(nb)
    fin = Frame(nb)
    overall = Frame(nb)
    
    nb.add(pre, text="Prelim")
    nb.add(mid, text="Midterm")
    nb.add(fin, text="Final")
    nb.add(overall, text="Overall")
    nb.pack(expand=True, fill="both")
    
    # MAKE SUBNOTEBOOK FOR TERMS
    make_subnb(pre)
    make_subnb(mid)
    make_subnb(fin)
    

def main():
    w = Tk()
    # SET WINDOW
    set_window(w)
    
    # SET MENU BAR
    M.set_menubar(w)
    
    # MAKE NOTEBOOK FOR TERMS
    make_nb(w)
    
    
    with open("classes.json") as file:
        classes = json.load(file)
    
    
    
    #for i, student in enumerate(students):
    #    Label(pre_frames["attendance"], text="Students").grid(row=i, column=0)
    
    
    
    
    
    
    
    w.mainloop()


def set_window(w):
    w.geometry("1024x512")
    w.title("Student Grading System")
    


if __name__ == "__main__":
    main()