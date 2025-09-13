from tkinter import *
from tkinter import ttk
from menu import Menubar as M


# make column row for the attendance. make an json for students. it has so many index. like name course etc.
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

    return {
        "attendance": att,
        "recitation": reci,
        "groupings": grp,
        "grades": grd,
        "summary": summ
        }

def main():
    w = Tk()
    # SET WINDOW
    set_window(w)
    
    # SET MENU BAR
    m = M.set_menubar(w)
    M.set_classmenu(m)
    M.set_editmenu(m)
    M.set_settingmenu(m)
     
    # MAKE NOTEBOOK FOR TERMS
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
    pre_frames = make_subnb(pre)
    mid_frames = make_subnb(mid)
    fin_frames = make_subnb(fin)
    
    students = Label(pre_frames["attendance"], text="Students")
    
    students.pack(side="left")
    
    
    
    
    
    
    w.mainloop()


def set_window(w):
    w.geometry("1024x512")
    w.title("Student Grading System")
    


if __name__ == "__main__":
    main()