from tkinter import *
import tkinter.messagebox
# import pymysql
import MySQL
import time



l = {}
def pressbutton():
    nameget = namein.get()
    ageget = agein.get()
    scoreget = scorein.get()
    if nameget and ageget and scoreget:
        l [nameget] = nameget
        l [nameget+'\''+'s age'] = ageget
        l [nameget+'\''+'s score'] = scoreget
        # db = pymysql.connect("localhost","root","97320010231","user")
        MySQL.inser_info(nameget,ageget,scoreget)
    else:
        tkinter.messagebox.showerror(title='警告',message='请输入完整信息！！！')

    listbox.insert(0,l)

def searchbutton():
    result = []
    searchnamefrom = searchname.get()
    cursor = db.cursor()
    searchfromSQL = 'select * from student WHERE name = '+"'"+searchnamefrom+"'"
    # print(searchfromSQL)
    try:
        cursor.execute(searchfromSQL)
        searchresult = cursor.fetchall()
        for row in searchresult:
            name = row[0]
            age = row[1]
            sorce = row[2]
            print(searchresult,name,age,sorce)
            result.append(searchresult)
            listbox.insert(0, result)
            print(len(row))


    except:
        tkinter.messagebox.showerror(title='警告', message='未能找到此学生！！！')
        print('Error:unable to fetch data')
    # print(searchnamefrom)
    db.close()

# db = pymysql.connect("localhost","root","97320010231","user")
db = MySQL.MySQL_connect()
cursor = db.cursor()
# cursor.execute("drop table if EXISTS student ")
# data = cursor.fetchone()
# print(1)
# sql = "create table student(name CHAR(20) NOT NULL ,age INT ,score INT )"
# cursor.execute(sql)
cursor.close()

root = Tk()
root.geometry("500x400+450+300")


#设置容器
frame_TimeLable = Frame(width = 50,height =20,padx = 2,pady = 5)
frame_nameLable = Frame(width = 50,height = 20,padx = 2,pady = 5)
frame_nameEntry = Frame(width = 50,height = 20,padx = 2,pady = 5)
frame_ageLable = Frame(width = 50,height = 20,padx = 2,pady = 5)
frame_ageEntry = Frame(width = 50,height = 20,padx = 2,pady = 5)
frame_scorceLable = Frame(width = 50,height = 20,padx = 2,pady = 5)
frame_scorceEntry = Frame(width = 50,height = 20,padx = 2,pady = 5)
frame_EntryButton = Frame(width = 50,height = 30,padx = 2,pady = 5)
frame_SearchNameLable = Frame(width = 50,height = 20,padx = 2,pady = 5)
frame_SearchNameEntry = Frame(width = 50,height = 20,padx = 2,pady = 5)
frame_SearchButton = Frame(width = 50,height = 30,padx = 2,pady = 5)
frame_ListBox = Frame(width = 50,height = 50,padx = 2,pady = 5)


#设置容器位置
frame_nameLable.grid(row = 0,column = 1)
frame_nameEntry.grid(row = 0,column = 2)
frame_TimeLable.grid(row = 0,column = 3)
frame_ageLable.grid(row = 1,column = 1)
frame_ageEntry.grid(row = 1,column = 2)
frame_scorceLable.grid(row = 2,column = 1)
frame_scorceEntry.grid(row = 2,column = 2)
frame_EntryButton.grid(row = 3,column = 1,rowspan = 2)
frame_SearchNameLable.grid(row = 5,column = 1)
frame_SearchNameEntry.grid(row = 5,column =2)
frame_SearchButton.grid(row = 6,column = 1)
frame_ListBox.grid(row = 7, column =1,rowspan = 4,columnspan = 4)


nameLable = Label(frame_nameLable,text = '姓名')
nameLable.pack()
namein = Entry(frame_nameEntry)
namein.pack()
Labeltime = Label(frame_TimeLable,text = time.strftime('%Y-%M-%D %H:%M:%S',time.localtime(time.time())))
Labeltime.pack()
def trickit():
    currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    Labeltime.config(text=currentTime)
    root.update()
    Labeltime.after(1000, trickit)
Labeltime.after(1000, trickit)
ageLable = Label(frame_ageLable,text = '年龄')
ageLable.pack()
agein = Entry(frame_ageEntry)
agein.pack()
scoreLable = Label(frame_scorceLable,text = '成绩')
scoreLable.pack()
scorein = Entry(frame_scorceEntry)
scorein.pack()
button = Button(frame_EntryButton,text = "存入",command = pressbutton)
button.pack()
searchnameLable = Label(frame_SearchNameLable,text = '查找姓名')
searchnameLable.pack()
searchname = Entry(frame_SearchNameEntry)
searchname.pack()
search = Button(frame_SearchButton,text = "查找",command = searchbutton)
search.pack()
listbox = Listbox(frame_ListBox,exportselection = False,height = 10,width = 40)
listbox.pack()
root.mainloop()