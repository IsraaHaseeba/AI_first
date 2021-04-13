from tkinter import*
import tkinter as tk
from tkinter import ttk
import IDS
from tkinter import messagebox
import webbrowser
import mappp
import UCS
import optimal



adj_List_IDS = {
    "Ramallah":["Nablus", "Salfit", "Jericho", "Jerusalem"],
    "Nablus":["Tubas", "Tulkarm", "Qalqilia", "Salfit","Ramallah", "Jericho","Jenin"],
    "Jerusalem":["Ramallah", "Jericho", "Bethlehem","Yafo"],
    "Jenin":["Tulkarm", "Nablus", "Tubas","Nazareth","Tiberias"],
    "Tubas":["Jenin", "Nablus","Jericho"],
    "Nazareth":["Jenin","Tiberias","Carmiel","Acre"],
    "Carmiel":["Ra's alnaqoura", "Acre", "Nazareth", "Tiberias"],
    "Tulkarm":["Jenin", "Nablus","Qalqilia","Yafo"],
    "Qalqilia":["Nablus", "Tulkarm","Salfit","Yafo"],
    "Salfit":["Nablus","Ramallah","Qalqilia","Yafo"],
    "Hebron":["Bethlehem","Bir Alsabe'"],
    "Bethlehem":["Hebron", "Jerusalem"],
    "Jericho":["Tubas", "Nablus", "Ramallah","Jerusalem","Tiberias"],
    "Tiberias":["Nazareth", "Carmiel", "Jericho", "Jenin"],
    "Haifa":["Acre", "Yafo"],
    "Bir Alsabe'":["Hebron"],
    "Acre":["Carmiel", "Haifa", "Nazareth", "Ra's alnaqoura"],
    "Yafo":["Haifa", "Tulkarm", "Qalqilia", "Salfit", "Jerusalem"],
    "Ra's alnaqoura":["Carmiel", "Acre"]
}


def click(args,alg):

    depth=10
    dest=[]

    if (SrcCities.get() != "" and list.curselection()):
        #take args
        start = (SrcCities.get())
        value = list.curselection()
        for i in value:
            dest.append(list.get(i))
        #start searching

        # Optimal
        if (args == 3):
            cost = 0
            track = []
            track,cost=optimal.main(start,dest)
            tracklist = ''
            expandedlist = ''

            for i in track:
                tracklist = tracklist + " -> " + str(i)
            list1.insert(END, tracklist)
            costs.insert(END, str(cost))



        else:
            for goal in dest:
                cost = 0

                #IDS
                if(args==2):
                    expanded, cost, track = IDS.check_children(adj_List_IDS, start, goal,depth)
                    track.reverse()
                #UCS
                elif(args==1):
                    expanded, cost, track = UCS.main(start,goal)


                tracklist = ''
                expandedlist = ''

                for i in track:
                    tracklist = tracklist + " -> " + str(i)
                list1.insert(END, tracklist)

                for i in expanded:
                    expandedlist = expandedlist + " -> " + str(i)
                list2.insert(END, expandedlist)

                costs.insert(END, goal+": "+ str(cost))
                #label = Label(canvas, text=goal + ": " + str(cost), compound=RIGHT)
                #canvas.create_window(0, y, window=label, anchor=NW)

            #canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, y))

    else:
        tk.messagebox.showerror("ERROR", "Missing requirement")


def showmap():
    value = list.curselection()
    dest=[]
    for i in value:
        dest.append(list.get(i))
    start=SrcCities.get()
    mappp.func(dest,start)

def showList():
    canvas = Canvas(gui, width=10, height=10)
    yscrollbar = Scrollbar(canvas)
    list = Listbox(canvas, selectmode="multiple",exportselection=0,
                   yscrollcommand=yscrollbar.set)
    yscrollbar.pack(side=RIGHT, fill=BOTH)
    list.pack(expand=YES, fill="both", side=LEFT)
    x = ["Ramallah", "Yafo","Nablus", "Jerusalem", "Jenin", "Tubas", "Nazareth",  "Carmiel",
        "Tulkarm", "Salfit", "Hebron", "Bethlehem", "Jericho", "Tiberias", "Haifa", "Bir Alsabe'",
         "Acre","Ra's alnaqoura","Qalqilia"]
    for each_item in range(len(x)):
        list.insert(END, x[each_item])
    yscrollbar.config(command=list.yview)
    canvas.place(x=500, y=260)

def reset():
    list1.delete(0, 'end')
    list2.delete(0,'end')
    list.delete(0,'end')
    costs.delete(0,'end')
    for each_item in range(len(x)):
        list.insert(END, x[each_item])
    SrcCities.set('')

#gui
gui = Tk(className='Find your destination route!')
gui.geometry("1368x2000")

#backgroung
bg = PhotoImage(file = "bg (4).png",height=2000)
bgdisplay = Label( gui, image = bg, height=2000)
bgdisplay.place(x = 0, y = 0)

#lables
srcLable= Label(bgdisplay, text="Start Location", width= 20,fg='white', bg='#324752',font=(25))
srcLable.place(x=100, y=210)
destLable= Label(bgdisplay, text="Destination", width= 20,fg='white', bg='#324752',font=(25))
destLable.place(x=100, y=260)

#SRC comboBOX
SrcCities =ttk.Combobox(bgdisplay,width= 30)
SrcCities['values']=("Ramallah","Yafo", "Nablus", "Jerusalem", "Jenin", "Tubas", "Nazareth", "Carmiel",
        "Tulkarm", "Salfit", "Hebron", "Qalqilia","Bethlehem", "Jericho", "Tiberias", "Haifa", "Bir Alsabe'",
         "Acre","Ra's alnaqoura")
SrcCities.place(x=300, y=210)

#checkBOX for destinations
canvas= Canvas(bgdisplay, width=10, height=10)
yscrollbar = Scrollbar(canvas)
list = Listbox(canvas, exportselection=0,selectmode = "multiple",
               yscrollcommand = yscrollbar.set)
yscrollbar.pack(side = RIGHT, fill = BOTH)
list.pack(  expand = YES, fill = "both", side=LEFT)
x = ["Ramallah", "Nablus", "Yafo","Jerusalem","Qalqilia", "Jenin", "Tubas", "Nazareth", "Carmiel",
        "Tulkarm", "Salfit", "Hebron", "Bethlehem", "Jericho", "Tiberias", "Haifa", "Bir Alsabe'",
         "Acre","Ra's alnaqoura"]
for each_item in range(len(x)):
    list.insert(END, x[each_item])
yscrollbar.config(command = list.yview)
canvas.place(x=300, y=260)

#CHOICES
UCSS= Button(bgdisplay, text="Uniform Cost ", width= 45,fg='white', bg='#a76316',font=(25)
            ,command=lambda :click(1,"UCS"))
UCSS.place(x=100, y=460)

IDSS= Button(bgdisplay, text="Iterative Deepening ", width= 45,fg='white', bg='#a76316',font=(25)
           ,command=lambda :click(2,"IDS"))
IDSS.place(x=100, y=510)

Opt= Button(bgdisplay, text="Optimal Search",width= 45, fg='white', bg='#a76316',font=(25)
            ,command=lambda :click(3,"OPT"))
Opt.place(x=100, y=560)

mapB= Button(bgdisplay, text="Map it!",width=14,height=3, fg='white', bg='#a76316',font=(25)
            ,command=lambda :showmap())
mapB.place(x=1070, y=590)
#cost
canvas = Canvas(gui, width=200, height=70)
scrollbar = Scrollbar(canvas, orient=VERTICAL)
costs=Listbox(canvas,yscrollcommand=scrollbar.set)
scrollbar.config( command=costs.yview)
scrollbar.pack(side = RIGHT, fill = BOTH)
costs.pack(  expand = YES, fill = "both", side=LEFT)
canvas.place(x=830, y=515)
#
Citycanvas = Canvas(gui, width=80, height=5)
scrollbar2 = Scrollbar(Citycanvas, orient=HORIZONTAL)
Vscrollbar2 = Scrollbar(Citycanvas, orient=VERTICAL)
list1 = Listbox(Citycanvas,yscrollcommand = Vscrollbar2.set, xscrollcommand=scrollbar2,width=60)
scrollbar2.pack(side = BOTTOM, fill = BOTH)
Vscrollbar2.pack(side = RIGHT, fill = BOTH)
scrollbar2.config(command = list1.xview)
Vscrollbar2.config(command = list1.yview)
list1.pack(  expand = YES, fill = "both", side=LEFT)
Citycanvas.place(x=830, y=80)

#
Citycanvas2 = Canvas(gui, width=50)
scrollbar3 = Scrollbar(Citycanvas2, orient=HORIZONTAL)
Vscrollbar3 = Scrollbar(Citycanvas2, orient=VERTICAL)
list2 = Listbox(Citycanvas2,yscrollcommand = Vscrollbar3.set, xscrollcommand=scrollbar3,width=60)
scrollbar3.pack(side = BOTTOM, fill = BOTH)
Vscrollbar3.pack(side = RIGHT, fill = BOTH)
scrollbar3.config(command = list2.xview)
Vscrollbar3.config(command = list2.yview)
list2.pack(  expand = YES, fill = "both", side=LEFT)
Citycanvas2.place(x=830, y=300)

'''
#multiple starts
mulStart= Button(bgdisplay, text="Multiple starts (*)",width=13,height=1 , fg='white', bg='#324752',font=(5)
            ,command=lambda :showList())
mulStart.place(x=520, y=210)'''

#reset button
resetB= Button(bgdisplay, text="RESET",width=7, fg='white', bg='#324752',font=(1)
            ,command=lambda :reset())
resetB.place(x=1230, y=620)



gui.mainloop()
