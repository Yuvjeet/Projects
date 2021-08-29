import tkinter as tk
from tkinter import ttk
from tkinter import*
from tkinter import messagebox
import mysql.connector
win=tk.Tk()
win.title("PERIODIC TABLE")
#label_frame
root=ttk.LabelFrame(win,text="PERIODIC TABEL")
root.pack()
user=ttk.LabelFrame(win,text="USER INFO")
user.pack()
#sql connector
def conn(s):
    conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='periodic_tabel')
    cursor=conn.cursor()
    query="SELECT * FROM info"
    cursor.execute(query)
    my_data=cursor.fetchall()
    conn.commit()
    conn.close()
    for i in my_data:
        if i[0]==s:
            return i
#period
for i in range(1,8):
    lable="lable"+str(i)
    lable1=tk.Label(root,text=i,bg="white").grid(row=i,column=0)
#group
for i in range(1,19):
    if i==1 or i==18:
        lable="lable"+str(i)
        lable1=tk.Label(root,text=i,bg="white").grid(row=0,column=i)
    elif i>2 and i<13:
        lable="lable"+str(i)
        lable1=tk.Label(root,text=i,bg="white").grid(row=3,column=i)
    else:
        lable="lable"+str(i)
        lable1=tk.Label(root,text=i,bg="white").grid(row=1,column=i)
        
group_1=('H','Li','Na','K','Rb','Cs','Fr')
group_2=('Be','Mg','Ca','Sr','Ba','Ra')
group_3=('Sc','Y','La','Ac')
group_4=('Ti','Zr','Hf','Rf')
group_5=('V','Nb','Ta','Db')
group_6=('Cr','Mo','W','Sg')
group_7=('Mn','Tc','Re','Bh')
group_8=('Fe','Ru','Os','Hs')
group_9=('Co','Rh','Ir','Mt')
group_10=('Ni','Pd','Pt','Ds')
group_11=('Cu','Ag','Au','Rg')
group_12=('Zn','Cd','Hg','Cn')
group_13=('B','Al','Ga','In','Tl','Nh')
group_14=('C','Si','Ge','Sn','pb','Fl')
group_15=('N','P','As','Sb','Bi','Mc')
group_16=('O','S','Se','Te','Po','Lv')
group_17=('F','Cl','Br','I','At','Ts')
group_18=('He','Ne','Ar','Kr','Xe','Rn','Og')
ls=('Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu')
As=('Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr')
#def no
def no(no):
    symbol,name,atomic_no,atomic_mass,state,cat=conn(no)
    messagebox.showinfo(no,f"symbol-{symbol}\nname={name}\natomic no={atomic_no}\nmass={atomic_mass}\nstate={state}\ncategory={cat}")
#group_1
for i in range(0,7):
    btn_1="button_1"+str(i)
    if i==0:
        btn_1=tk.Button(root,text=group_1[0],fg="black",bg="#ffb399",width=5,command=lambda n=group_1[i]:no(n),height=2)
        btn_1.grid(row=1,column=1)
    else:
        btn_1=tk.Button(root,text=group_1[i],fg="black",bg="#ffe0b3",command=lambda n=group_1[i]:no(n),width=5,height=2)
        btn_1.grid(row=i+1,column=1)
#group_2
for i in range(2,8):
    btn_2="button_2"+str(i)
    btn_2=tk.Button(root,text=group_2[(i-2)],fg="black",bg="#ffb366",width=5,command=lambda n=group_2[(i-2)]:no(n),height=2)
    btn_2.grid(row=i,column=2)
#group_3
for i in range(3,7):
    btn_3="button_2"+str(i)
    if i==6:
        btn_3=tk.Button(root,text=group_3[3],fg="black",bg="#b3d9ff",width=5,command=lambda n=group_3[3]:no(n),height=2)
        btn_3.grid(row=i+1,column=3)
    else:
        btn_3=tk.Button(root,text=group_3[(i-3)],fg="black",bg="#ffff99",width=5,command=lambda n=group_3[(i-3)]:no(n),height=2)
        btn_3.grid(row=i+1,column=3)
#group_4
for i in range(3,7):
    btn=tk.Button(root,text=group_4[(i-3)],fg="black",bg="#ca99ff",width=5,command=lambda n=group_4[(i-3)]:no(n),height=2)
    btn.grid(row=i+1,column=4)
#group_5
for i in range(3,7):
    btn=tk.Button(root,text=group_5[(i-3)],fg="black",bg="#ca99ff",width=5,command=lambda n=group_5[(i-3)]:no(n),height=2)
    btn.grid(row=i+1,column=5)
#group_6
for i in range(3,7):
    btn=tk.Button(root,text=group_6[(i-3)],fg="black",bg="#ca99ff",width=5,command=lambda n=group_6[(i-3)]:no(n),height=2)
    btn.grid(row=i+1,column=6)
#group_7
for i in range(3,7):
    btn=tk.Button(root,text=group_7[(i-3)],fg="black",bg="#ca99ff",width=5,command=lambda n=group_7[(i-3)]:no(n),height=2)
    btn.grid(row=i+1,column=7)
#group_8
for i in range(3,7):
    btn=tk.Button(root,text=group_8[(i-3)],fg="black",bg="#ca99ff",width=5,command=lambda n=group_8[(i-3)]:no(n),height=2)
    btn.grid(row=i+1,column=8)
#group_9
for i in range(3,7):
    btn=tk.Button(root,text=group_9[(i-3)],fg="black",bg="#ca99ff",width=5,command=lambda n=group_9[(i-3)]:no(n),height=2)
    btn.grid(row=i+1,column=9)
#group_10
for i in range(3,7):
    btn=tk.Button(root,text=group_10[(i-3)],fg="black",bg="#ca99ff",width=5,command=lambda n=group_10[(i-3)]:no(n),height=2)
    btn.grid(row=i+1,column=10)
#group_11
for i in range(3,7):
    btn=tk.Button(root,text=group_11[(i-3)],fg="black",bg="#ca99ff",width=5,command=lambda n=group_11[(i-3)]:no(n),height=2)
    btn.grid(row=i+1,column=11)
#group_12
for i in range(3,7):
    btn=tk.Button(root,text=group_12[(i-3)],fg="black",bg="#ca99ff",width=5,command=lambda n=group_12[(i-3)]:no(n),height=2)
    btn.grid(row=i+1,column=12)
#group_13
for i in range(2,8):
    if i==2:
        btn=tk.Button(root,text=group_13[(i-2)],fg="black",bg="#ffb399",width=5,command=lambda n=group_13[(i-2)]:no(n),height=2)
        btn.grid(row=i,column=13)
    else:
        btn=tk.Button(root,text=group_13[(i-2)],fg="black",bg="#ffcccc",width=5,command=lambda n=group_13[(i-2)]:no(n),height=2)
        btn.grid(row=i,column=13)
#group_14
for i in range(2,8):
    if i>=2 and i<4:
        btn=tk.Button(root,text=group_14[(i-2)],fg="black",bg="#ffb399",width=5,command=lambda n=group_14[(i-2)]:no(n),height=2)
        btn.grid(row=i,column=14)
    else:
        btn=tk.Button(root,text=group_14[(i-2)],fg="black",bg="#ffcccc",width=5,command=lambda n=group_14[(i-2)]:no(n),height=2)
        btn.grid(row=i,column=14)
#group_15
for i in range(2,8):
    if i>=2 and i<5:
        btn=tk.Button(root,text=group_15[(i-2)],fg="black",bg="#ffb399",width=5,command=lambda n=group_15[(i-2)]:no(n),height=2)
        btn.grid(row=i,column=15)
    else:
        btn=tk.Button(root,text=group_15[(i-2)],fg="black",bg="#ffcccc",width=5,command=lambda n=group_15[(i-2)]:no(n),height=2)
        btn.grid(row=i,column=15)
#group_16
for i in range(2,8):
    if i>=2 and i<6:
        btn=tk.Button(root,text=group_16[(i-2)],fg="black",bg="#ffb399",width=5,command=lambda n=group_16[(i-2)]:no(n),height=2)
        btn.grid(row=i,column=16)
    else:
        btn=tk.Button(root,text=group_16[(i-2)],fg="black",bg="#ffcccc",width=5,command=lambda n=group_16[(i-2)]:no(n),height=2)
        btn.grid(row=i,column=16)
#group_17
for i in range(2,8):
    btn=tk.Button(root,text=group_17[(i-2)],fg="black",bg="#8cd98c",width=5,command=lambda n=group_17[(i-2)]:no(n),height=2)
    btn.grid(row=i,column=17)
#group_18
for i in range(len(group_18)):
    btn=tk.Button(root,text=group_18[i],fg="black",bg="#f2f2f2",width=5,command=lambda n=group_18[i]:no(n),height=2)
    btn.grid(row=i+1,column=18)
#periodic button
periodic_btn=tk.Button(root,text="PERIODIC TABLE",bg="red")
periodic_btn.grid(row=0,columnspan=17)
#lable_of_group
lanthariod_series=tk.Label(root,text="Lanthariod Series")
lanthariod_series.grid(row=20,columnspan=3)
actiniod_series=tk.Label(root,text="Actiniod Series")
actiniod_series.grid(row=21,columnspan=3)
P6=tk.Label(root,text="6",bg="white")
P6.grid(row=20,column=3)
P7=tk.Label(root,text="7",bg="white")
P7.grid(row=21,column=3)
#empty_space
for i in range(1,19):
    lable1=tk.Label(root,text=None).grid(row=19,column=i)
#ls_group
for i in range(4,(len(ls)+4)):
    btn=tk.Button(root,text=ls[i-4],fg="black",bg="#ffff99",width=5,command=lambda n=ls[i-4]:no(n),height=2)
    btn.grid(row=20,column=i)
#as_group
for i in range(4,(len(As)+4)):
    btn=tk.Button(root,text=As[i-4],fg="black",bg="#b3d9ff",width=5,command=lambda n=As[i-4]:no(n),height=2)
    btn.grid(row=21,column=i)
root.mainloop()
