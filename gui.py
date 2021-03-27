from tkinter import*
import tkinter as tk
from tkinter import ttk



#gui
gui = Tk(className='Find your destination route!')
gui.geometry("1368x2000")



#backgroung
bg = PhotoImage(file = "bg (1).png",height=2000)
bgdisplay = Label( gui, image = bg, height=2000)
bgdisplay.place(x = 0, y = 0)

#bottons and lables

srcLable= Label(bgdisplay, text="Start Location", width= 20,fg='white', bg='#324752',font=(25))
srcLable.place(x=200, y=210)
destLable= Label(bgdisplay, text="Destination", width= 20,fg='white', bg='#324752',font=(25))
destLable.place(x=200, y=260)

UCS= Button(bgdisplay, text="Uniform Cost ", width= 20,fg='white', bg='#a76316',font=(25))
UCS.place(x=200, y=310)
IDS= Button(bgdisplay, text="Iterative Deepening ", width= 21,fg='white', bg='#a76316',font=(25))
IDS.place(x=400, y=310)


SrcCities =ttk.Combobox(bgdisplay,width= 30,values=['Ramallah'])
SrcCities.place(x=400, y=260)
desCities =ttk.Combobox(bgdisplay,width= 30,values=['Ramallah'])
desCities.place(x=400, y=210)

#multiple goals
srcLable2= Label(bgdisplay, text="Start Location", width= 20,fg='white', bg='#324752',font=(25))
srcLable2.place(x=200, y=435)
SrcCities2 =ttk.Combobox(bgdisplay,width= 30,values=['Ramallah'])
SrcCities2.place(x=400, y=435)
destLable2= Label(bgdisplay, text="Destinations", width= 20,fg='white', bg='#324752',font=(25))
destLable2.place(x=200, y=485)
Opt= Button(bgdisplay, text="Optimal Search",width= 20, fg='white', bg='#a76316',font=(25))
Opt.place(x=200, y=535)

#check destinations
canvas= Canvas(bgdisplay, width=10, height=10)
yscrollbar = Scrollbar(canvas)
list = Listbox(canvas, selectmode = "multiple",
               yscrollcommand = yscrollbar.set)
yscrollbar.pack(side = RIGHT, fill = BOTH)
list.pack(  expand = YES, fill = "both", side=LEFT)
x = ["Ramllah", "Nablus", "Jerusalem","Jenin", "Tubas","l","l", "l", "l", "l","l","d"]
for each_item in range(len(x)):
    list.insert(END, x[each_item])
yscrollbar.config(command = list.yview)
canvas.place(x=400, y=485)

#Bonusgoal
srcLable3= Label(bgdisplay, text="Start Locations", width= 20,fg='white', bg='#324752',font=(25))
srcLable3.place(x=720, y=210)
destLable3= Label(bgdisplay, text="Destinations", width= 20,fg='white', bg='#324752',font=(25))
destLable3.place(x=920, y=210)
#source check
canvas2= Canvas(bgdisplay, width=10, height=10)
yscrollbar2= Scrollbar(canvas2)
list2 = Listbox(canvas2, selectmode = "multiple",
               yscrollcommand = yscrollbar2.set)
yscrollbar2.pack(side = RIGHT, fill = BOTH)
list2.pack(  expand = YES, fill = "both", side=LEFT)
for each_item in range(len(x)):
    list2.insert(END, x[each_item])
yscrollbar2.config(command = list2.yview)
canvas2.place(x=720, y=250)
#check des
canvas3= Canvas(bgdisplay, width=10, height=10)
yscrollbar3 = Scrollbar(canvas3)
list3 = Listbox(canvas3, selectmode = "multiple",
               yscrollcommand = yscrollbar3.set)
yscrollbar3.pack(side = RIGHT, fill = BOTH)
list3.pack(  expand = YES, fill = "both", side=LEFT)
for each_item in range(len(x)):
    list3.insert(END, x[each_item])
yscrollbar3.config(command = list3.yview)
canvas3.place(x=920, y=250)
Opt2= Button(bgdisplay, text="Multiple Start-Destination Optimal Search",width= 40, fg='white', bg='#a76316',font=(25))
Opt2.place(x=720, y=450)






gui.mainloop()
