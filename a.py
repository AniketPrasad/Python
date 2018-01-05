from Tkinter import *
import tkMessageBox
import ttk
import sqlite3
con=sqlite3.Connection('hrdb')
cur=con.cursor()
cur.execute("create table if not exists e2(boarding char(20),destination char(20),adno number,day char,time number)")
rootp=Tk()
rootp.geometry('830x400')
rootp.config(bg="brown")
topframe=Frame(rootp)
topframe.pack()
topframe.config(bg="brown")
bottomframe=Frame(rootp)
bottomframe.pack()
Label(topframe,text="Welcome to Red Bus App",font="Bold 20",bg='brown').grid(row=0)
def fun8():
    root2=Tk()
    root2.title("Welcome,Customer To our Cancellation System")
    Label(root2,text="Enter your last 4 digit of Voter Id").grid(row=0,column=0)
    e1=Entry(root2)
    e1.grid(row=0,column=1)
    Label(root2,text="select boarding").grid(row=1,column=0)
    w3=ttk.Combobox(root2,height=5,width=15,state='readonly',values=["Bangalore","Bhopal","Noida","Calcutta"])
    w3.grid(row=1,column=1)
    def fun2():
        d=e1.get()
        c=w3.get()
        if d=='' or c=='':
             tkMessageBox.showerror("Oops","You can't Enter the leave any field empty")
        else:     
            cur.execute("select * from e2 where adno=?",(d,))
            x=cur.fetchall()
            cur.execute("delete from e2 where adno=(?) and boarding=(?)",(d,c,))
            tkMessageBox.showinfo("Bus Info",'Your Bus has been cancelled')
            con.commit()
            root2.destroy()
        
    Bc=Button(root2,text="Cancel Reservation",command=fun2).grid(row=4,column=0)
    root2.mainloop()
def fun9():
    root4=Tk()
    root4.title("Welcome,Search Bus")
    Label(root4,text="Enter Boarding").grid(row=0,column=0)
    w1=ttk.Combobox(root4,height=5,width=15,state='readonly',values=["Bangalore","Bhopal","Noida","Calcutta","patna"])
    w1.grid(row=0,column=1)
    Label(root4,text="select destination").grid(row=1,column=0)
    w2=ttk.Combobox(root4,height=5,width=15,state='readonly',values=["Bangalore","Bhopal","Noida","Calcutta"])
    w2.grid(row=1,column=1)
    Label(root4,text="Choose day of travel").grid(row=2,column=0)
    w3=ttk.Combobox(root4,text="choose day",height=5,width=15,state='readonly',values=["sunday","monday","tuesday","wensday","thursday","friday","saturday"])
    w3.grid(row=2,column=1)
    def fun10():
        a=w1.get()
        b=w2.get()
        c=w3.get()
        if a=='' or b=='' or c=='':
            tkMessageBox.showerror("Error","Cant leave any field empty")
        else:
             if a!=b:
                 cur.execute("select * from e2 where boarding=? and destination=? and day=?",(a,b,c,))
                 e=cur.fetchall()
                 if e!=[]:
                     
                     tkMessageBox.showinfo("Bus availble are",e[0])
                     root4.destroy()
                 else:
                     tkMessageBox.showerror("Error",'Data not found')
                     root4.destroy()
             else:
                tkMessageBox.showerror("Oops","boarding and destination can't me same")
        
    Bs=Button(root4,text="search",command=fun10).grid(row=3,column=0)
    root4.mainloop()
def fun5():
    root=Tk()
    root.title('Bus search And booking')
    Label(root,text="From").grid(row=1,column=0)
    w=ttk.Combobox(root,height=5,width=15,state='readonly',values=["Bangalore","Bhopal","Noida","Calcutta"])
    w.grid(row=1,column=1)
    Label(root,text='To').grid(row=2,column=0)
    w1=ttk.Combobox(root,height=5,width=15,state='readonly',values=["Bangalore","Bhopal","Noida","Calcutta"])
    w1.grid(row=2,column=1)
    Label(root,text='Enter your last 4 digit of voter id').grid(row=3,column=0)
    e=Entry(root,width=20)
    e.grid(row=3,column=1)
    w2=ttk.Combobox(root,text='common',state='readonly',height=5,width=15,values=["A/C","NON A/C"])
    w2.grid(row=4,column=1)
    Label(root,text='Choose Class').grid(row=4,column=0)
    Label(root,text="Choose day of travel").grid(row=5,column=0)
    w3=ttk.Combobox(root,text="choose day",height=5,state='readonly',width=15,values=["sunday","monday","tuesday","wensday","thursday","friday","saturday"])
    w3.grid(row=5,column=1)
    Label(root,text="choose time of your bus").grid(row=6,column=0)
    w4=ttk.Combobox(root,height=5,state='readonly',width=15,values=["1:00 AM","7:00 AM","1:00 PM","4:00 PM","9:00 PM"])
    w4.grid(row=6,column=1)
    def fun():
        a=w.get()
        b=w1.get()
        c=e.get()
        d=w2.get()
        f=w3.get()
        g=w4.get()
        x=(a,b,c,f,g)
        
        if a=='' or b=='' or c=='' or d=='' or f=='' or g=='':
            tkMessageBox.showerror("OOPS","you can't leave any field empty")
        else :
            if a!=b:
                cur.execute("insert into e2 values(?,?,?,?,?)",x)
                tkMessageBox.showinfo("congrats","your seat has been Confirmed")
                con.commit()
                cur.execute("select * from e2 where adno=(?)",(c,))
                x=cur.fetchall()
                tkMessageBox.showinfo("records",x[0])
                root.destroy()
            else:
                tkMessageBox.showerror("Error","you can't choose same city")
    Bi=Button(root,text="Insert",command=fun).grid(row=7,column=1)
    root.mainloop()
bus_image=PhotoImage(file='Bus.gif')
label=Label(topframe,image=bus_image).grid(row=2)
def fun1():
    bottomframe.destroy()
    f=Frame(rootp)
    f.pack()
    Button(f,text="Cancel Booking",width=50,bg='orange',fg='white',height=2,command=fun8).grid(row=3,column=0)
    Button(f,text="See Booking",width=50,bg='orange',fg='white',height=2,command=fun9).grid(row=3,column=1)
    Button(f,text="Book Bus",width=50,bg='orange',fg='white',height=2,command=fun5).grid(row=3,column=2)
Button(bottomframe,text="Welcome",height=3,width=50,bg='Red',fg='white',command=fun1).grid(row=3)
Label(bottomframe,text='Made By- Aniket Prasad(151232)(B1)').grid(row=4,column=0)
def About_us():
    root10=Tk()
    Label(root10,text='Made By-',font='Arial 20 bold').pack()
    Label(root10,text='This is an application which will help you Book Bus\nIt is made by-',font='Arial 11 bold').pack()
    Label(root10,text='Aniket Prasad',font='Arial 10 bold').pack()
    Label(root10,text='Enrollment No.-151232',font='Arial 10 bold').pack()
    Label(root10,text='Batch-B1',font='Arial 10 bold').pack()
    root10.mainloop()
Button(bottomframe,text='About us',command=About_us).grid(row=5)
rootp.mainloop()
    
