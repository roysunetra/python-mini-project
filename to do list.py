from tkinter import*
from tkinter import Image
from tkinter import messagebox

ms = Tk()
bg = PhotoImage(file = "F:\\CodSoft\\5197214.PNG") 
# Show image using label 
label1 = Label( ms, image = bg) 
label1.place(x = 0, y = 0) 
ms.geometry('500x500+500+500')
ms.title('Tasks To Complete')
ms.resizable(width=True, height=True)
frame = Frame(ms)
frame.pack(pady=20)
list_box = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#eb8e15',
    highlightthickness=0,
    selectbackground='#eb8f2d',
    activestyle="none",   
)
list_box.pack(side=RIGHT,fill=BOTH)
task_list = ['Eat Healthy','drink water','Code daily','Sleep well','Smile']
for item in task_list:
    list_box.insert(END, item)
sb = Scrollbar(frame)
sb.pack(side=LEFT, fill=BOTH)

list_box.config(yscrollcommand=sb.set)
sb.config(command=list_box.yview)
newentry = Entry(
    ms,
    font=('Normal', 14),
    bg='#ebe3da',
    fg='#eb8f2d'
    )
newentry.pack(pady=20)
button_frame = Frame(ms)
button_frame.pack(pady=20)
def newTask():
    task = newentry.get()
    if task != "":
        list_box.insert(END, task)
        newentry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")
def deleteTask():
    list_box.delete(ANCHOR)
add_Task_btn = Button(
    button_frame,
    text='Add Task',
    font=('Normal 14'),
    fg='#faf7f5',
    bg='#eb8e15',
    padx=20,
    pady=10,
    command=newTask
)
add_Task_btn.pack(fill=BOTH, expand=True, side=LEFT)
del_Task_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Normal 14'),
    fg='#faf7f5',
    bg='#ff0000',
    padx=20,
    pady=10, 
    command=deleteTask
)
del_Task_btn.pack(fill=BOTH, expand=True, side=LEFT)
ms.mainloop()