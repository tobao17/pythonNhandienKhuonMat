# import tkinter as tk
# from tkinter import *
# root =tk.Tk()

# canvas=tk.Canvas(root,height=500,width=500,bg="#263D42")
# # canvas.pack()
# canvas.grid_size()
# # frame=tk.Frame(root,bg="white")
# # frame.place(relwidth=0.8,relheight=0.6,relx=0.1,rely=0.1)
# buttonNhandien=tk.Button(root,text="Nhận diện",fg="white",bg="#000")
# buttonNhandien2=tk.Button(root,text="Nhận diện",fg="white",bg="#263D42")
# buttonNhandien.grid(pady=4)
# # buttonNhandien2.pack()
# root.mainloop()
from tkinter import * 
screen =Tk()
screen.geometry("400x400")
screen.title("Nhận diện khuôn mặt")
heading =Label(text="Nhận diện khuôn mặt",bg="grey",fg="black",width="500",height="2")
heading.pack()



textid=Text( fg="black",width="20",height="1")
textid.place(x=75,y=200)
textName=Text( fg="black",width="20",height="1")
textName.place(x=75,y=230)
lblid=Label(text="Nhập vào id:",fg="black",width="10",height="1")
lblid.place(x=0,y=200)
lblid=Label(text="Nhập vào Tên:",fg="black",width="10",height="1")
lblid.place(x=0,y=230)
def showdata():
    print("kien oc cho"+textid.get("1.0","end-1c")+textName.get("1.0","end-1c"))

    
buttonNhapdulieu=Button(text="Nhập dữ liệu",fg="white",bg="#263D42", command=showdata)
buttonNhapdulieu.place(x=160,y=260)
buttonNhandien=Button(text="Nhận diện",fg="white",bg="#263D42")
buttonNhandien.place(x=300,y=300)
screen.mainloop()





