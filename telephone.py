from Tkinter import *
import mysql.connector as m
import os
import csv

root=Tk()
root.geometry('500x600')
root.title('Telephone')


v=StringVar() #name
v1=IntVar()  #phone_no
#create table contect(name varchar(20),number int(11) primary key);
#b=Button(root,text="screen",command=fun1).place(x=250,y=50)

s1=IntVar() #search no.
s2=StringVar() #search Name

u1=IntVar() #enter no
u2=StringVar() #enter name
u3=StringVar() #update nm
u4=IntVar() #update number

d1=StringVar()
d2=IntVar()

f1=StringVar()#file name export

i1=StringVar() #import file name

l1=Label(root,text="Name")
l2=Label(root,text="Number")
e1=Entry(root,width=20,textvariable=v)
e2=Entry(root,width=11,textvariable=v1)
l1.place(x=250,y=50)
e1.place(x=300,y=50)
l2.place(x=250,y=80)
e2.place(x=300,y=80)


def fun1():
    e2.insert(END,1)

def fun2():
    e2.insert(END,2)

def fun3():
    e2.insert(END,3)

def fun4():
    e2.insert(END,4)

def fun5():
    e2.insert(END,5)

def fun6():
    e2.insert(END,6)
    
def fun7():
    e2.insert(END,7)

def fun8():
    e2.insert(END,8)

def fun9():
    e2.insert(END,9)

def fun0():
    e2.insert(END,0)


def submit():
    db=m.connect(user='root',password="Dhrupesh123#@",database="collage")
    cursor=db.cursor()
    sql="insert into contect values('{}',{})".format(v.get(),v1.get())
    cursor.execute(sql)
    db.commit()
    db.close()
    t0=Toplevel(root)
    t0.geometry('200x25')
    l1=Label(t0,text="contact successfully saved!")
    l1.pack()


def searchfun():
    db=m.connect(user='root',password="Dhrupesh123#@",database="collage")
    cursor=db.cursor()
    sql="select * from contect where name='{}' or number={}".format(s2.get(),s1.get()) #collect data from database
    cursor.execute(sql)
    result=cursor.fetchall()
    for raw in result:
        lb=Label(t1,text="NAME :  {}    CONTACT :  {}".format(raw[0],raw[1])).place(x=50,y=180)
    db.commit()
    db.close()
    


def search():
    global t1
    t1=Toplevel(root)
    t1.geometry('300x400')
    lb1=Label(t1,text='enter number').place(x=50,y=50)
    e11=Entry(t1,width=11,textvariable=s1).place(x=140,y=50)
    lb2=Label(t1,text='or').place(x=80,y=75)
    e11=Entry(t1,width=11,textvariable=s2).place(x=140,y=100)
    lb3=Label(t1,text='enter name').place(x=50,y=100)
    
    bfind=Button(t1,text='find',command=searchfun).place(x=135,y=130)

def enterfun():
    db=m.connect(user='root',password="Dhrupesh123#@",database="collage")
    cursor=db.cursor()
    if u1.get()==0:
        sql1="select * from contect where name='{}'".format(u2.get())
        cursor.execute(sql1)
        result=cursor.fetchone()
        if result is not None:
            sql="update contect set number={} where name='{}'".format(u4.get(),u2.get()) #update database
            cursor.execute(sql)
            db.commit()
            db.close()
            ll=Label(t2,text="update successfuly!").place(x=100,y=300)
        else:
            l9=Label(t2,text="Data Not Founded,Please Enter Invalied Name").place(x=50,y=300)
            
    else:
        sql2="select * from contect where number={}".format(u1.get())
        cursor.execute(sql2)
        result1=cursor.fetchone()
        if result1 is not None:
            sql3="update contect set name='{}' where number={}".format(u3.get(),u1.get())
            cursor.execute(sql3)
            db.commit()
            db.close()
            ll=Label(t2,text="update successfuly!").place(x=100,y=300)
        else:
            l0=Label(t2,text="Data Not Founded,Please Enter Invalied Number").place(x=50,y=300)
            
    

    
def update():
    global t2
    t2=Toplevel(root)
    t2.geometry('300x400')
    lt1=Label(t2,text="if you are update Phone Number").place(x=50,y=25)
    lt=Label(t2,text="Enter Name").place(x=70,y=45)
    lt4=Label(t2,text="Updated Number").place(x=70,y=70)
    et4=Entry(t2,width=11,textvariable=u4).place(x=170,y=70)#Updated Number

    l=Label(t2,text="OR").place(x=130,y=100)
    
    lt2=Label(t2,text="if you are update Name").place(x=80,y=150)
    lt3=Label(t2,text="Enter Number").place(x=70,y=170)
    lt5=Label(t2,text="Updated Name").place(x=70,y=195)
    et1=Entry(t2,width=20,textvariable=u2).place(x=150,y=45)#enter name
    et2=Entry(t2,width=11,textvariable=u1).place(x=170,y=170)#enter number
    et3=Entry(t2,width=20,textvariable=u3).place(x=160,y=195)#update name

    bEnter=Button(t2,text="Enter",command=enterfun).place(x=130,y=250)



def deletefun():
    db=m.connect(user='root',password="Dhrupesh123#",database="collage")
    cursor=db.cursor()
    sql="delete from contect where name='{}' or number={}".format(d1.get(),d2.get())
    cursor.execute(sql)
    db.commit()
    db.close()
    l7=Label(t3,text="Data deleted!").place(x=120,y=170)
    

def delete():
    global t3
    t3=Toplevel(root)
    t3.geometry('300x400')
    lb=Label(t3,text="Enter Name").place(x=40,y=50)
    lb=Label(t3,text="OR").place(x=70,y=75)
    lbb=Label(t3,text="Enter Number").place(x=40,y=100)
    en=Entry(t3,width=20,textvariable=d1).place(x=130,y=50)
    en=Entry(t3,width=10,textvariable=d2).place(x=130,y=100)
    
    bb=Button(t3,text="Done",command=deletefun).place(x=140,y=135)
    
def list():
    t4=Toplevel(root)
    t4.geometry('200x300')
    lb4=Label(t4,text="Your Contact")
    #lb5=Label(t4,text="Contact").place(x=90,y=30)
    listbox=Listbox(t4)
    db=m.connect(user='root',password="Dhrupesh123#",database="collage")
    cursor=db.cursor()
    sql="select * from contect"
    cursor.execute(sql)
    result=cursor.fetchall()
    print result
    i=1
    for raw in result:
        listbox.insert(i,raw)
        i=i+1
    db.close()
    lb4.pack()
    listbox.pack()

def exfun():
    '''
    p="C:\ProgramData\MySQL\MySQL Server 5.7\Uploads"
    p1=f1.get()
    path=os.path.join(p,p1)
    db=m.connect(user='root',password="Dhrupesh123#",database="collage")
    cursor=db.cursor()
    #C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/test4.txt
    print path
    #sql="SELECT name,number from contect INTO OUTFILE '{}' FIELDS ENCLOSED BY '-'ESCAPED BY ',' LINES TERMINATED BY '\n\n'".format(path)
    sql="SELECT * from contect INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/{}'FIELDS ENCLOSED BY '-' ESCAPED BY ',' LINES TERMINATED BY '\n'".format(f1.get())
    cursor.execute(sql)
    os.startfile(path)
    db.close()
    '''
    db=m.connect(user='root',password="Dhrupesh123#",database="collage")
    cursor=db.cursor()
    sql="select * from contect"
    cursor.execute(sql)
    result=cursor.fetchall()
    p1=f1.get()
    p2='C:\Python27'
    path=p2+"\\"+p1
    
    with open(p1,'w') as csvFile:
        writer=csv.writer(csvFile)
        writer.writerows(result)
    csvFile.close()
    db.close()
    os.startfile(path)
    
    
    
    
    
    
def export():
    t5=Toplevel(root)
    t5.geometry('400x200')
    l=Label(t5,text="Create File Name").place(x=30,y=40)
    ll=Label(t5,text="Enter file name with extension(examlple=*.csv)").place(x=40,y=10)
    efile=Entry(t5,width=15,textvariable=f1).place(x=160,y=40)
    bfile=Button(t5,text='create',command=exfun).place(x=170,y=90)

def importfun():
    i=i1.get()
    db=m.connect(user='root',password="Dhrupesh123#",database="collage")
    cursor=db.cursor()
    #sql="LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/{}' INTO TABLE contect FIELDS TERMINATED BY ',' ENCLOSED BY '-' LINES TERMINATED BY '\n'".format(i)
    #print sql
    print i
    with open(i,'r') as f:
        data=csv.reader(f)
        for raw in data:
            sql="insert into contect values('{}',{})".format(raw[0],raw[1])
            #print sql
            cursor.execute(sql)
            db.commit()
    f.close()
    db.close()



def bimport():
    t6=Toplevel(root)
    t6.geometry('400x200')
    la=Label(t6,text="enter file full path").place(x=80,y=50)
    ea=Entry(t6,width=30,textvariable=i1).place(x=200,y=50)
    b=Button(t6,text="done",command=importfun).place(x=160,y=90)
    
    

b1=Button(root,text=1,command=fun1).place(x=50,y=50)
b2=Button(root,text=2,command=fun2).place(x=100,y=50)
b3=Button(root,text=3,command=fun3).place(x=150,y=50)
b4=Button(root,text=4,command=fun4).place(x=50,y=100)
b5=Button(root,text=5,command=fun5).place(x=100,y=100)
b6=Button(root,text=6,command=fun6).place(x=150,y=100)
b7=Button(root,text=7,command=fun7).place(x=50,y=150)
b8=Button(root,text=8,command=fun8).place(x=100,y=150)
b9=Button(root,text=9,command=fun9).place(x=150,y=150)
b0=Button(root,text=0,command=fun0).place(x=100,y=200)

bsubmit=Button(root,text="submit",command=submit).place(x=385,y=80)

bsearch=Button(root,text='search',command=search).place(x=250,y=150)

bupdate=Button(root,text="update",command=update).place(x=330,y=150)

bdelete=Button(root,text="delete",command=delete).place(x=250,y=200)

blist=Button(root,text="contact List",command=list).place(x=330,y=200)

bexport=Button(root,text="Export",command=export).place(x=250,y=250)

bimport=Button(root,text="import",command=bimport).place(x=330,y=250)

root.mainloop()

