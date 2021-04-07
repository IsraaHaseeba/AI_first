from tkinter import*
import tkinter as tk
from tkinter import ttk
import IDS
from tkinter import messagebox
import webbrowser
import mappp




adj_List_IDS = {
    "Jenin": ["Tulkarm", "Nablus", "Tiberias", "Nazareth"],
    "Nablus": ["Tubas", "Tulkarm", "Qalqilia", "Salfit",
               "Ramallah", "Jerico","Jenin"],
    "Ramallah": ["Nablus", "Jerico", "Jerusalem", "Salfit"],
    "Jerico" : ["Ramallah", "Nablus"],
    "Jerusalem" : [ "Ramallah"],
    "Salfit" : ["Nablus", "Ramallah"],
    "Nazareth" : ["Jenin"],
    "Tulkarm" : ["Jenin", "Nablus"],
    "Tiberias" : ["Jenin"],
    "Tubas" : ["Nablus"],
    "Qalqilia" : ["Nablus"]
}

def click(args,alg):
    costs=[]
    depth=10
    dest=[]
    if (SrcCities.get() != "" and list.curselection()):
        start = (SrcCities.get())
        value = list.curselection()
        for i in value:
            dest.append(list.get(i))

        if(args==1):
            y = 0
            canvas = Canvas(gui, width=150, height=100)
            canvas.place(x=720, y=560)

            for goal in dest:
                cost=0
                expanded, cost, track = IDS.check_children(adj_List_IDS, start, goal,
                                                           depth)  # method returning track and cost of the goal
                print("Nodes visited are: \n", expanded)
                print("Cost is: \n", cost)
                track.reverse()
                print("You will go through these cities till you reach ", goal, " from ", start + ":\n ")
                print(track)
                print("NEXT\n\n")

                label = Label(canvas,  text=goal+": "+ str(cost),compound=RIGHT)
                canvas.create_window(0, y, window=label, anchor=NW)
                y += 20
                #costs.append(goal+": "+ str(cost))
            scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
            scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
            canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, y))



        elif(args==2):
            pass

        elif(args==3):
            dest=[]
            start=[]
            if (list3.curselection() and list2.curselection()):
                value1=list2.curselection()
                value2=list3.curselection()
                for i in value1:
                    start.append(list.get(i))
                for i in value2:
                    dest.append(list.get(i))
            else:
                tk.messagebox.showerror("ERROR", "Missing requirement")

    else:
        tk.messagebox.showerror("ERROR", "Missing requirement")
    #cost.config(text=costs)

def showmap():
    value = list.curselection()
    dest=[]
    for i in value:
        dest.append(list.get(i))
    start=SrcCities.get()
    mappp.func(dest,start)


#gui
gui = Tk(className='Find your destination route!')
gui.geometry("1368x2000")

#backgroung
bg = PhotoImage(file = "bg (1).png",height=2000)
bgdisplay = Label( gui, image = bg, height=2000)
bgdisplay.place(x = 0, y = 0)

#lables
srcLable= Label(bgdisplay, text="Start Location", width= 20,fg='white', bg='#324752',font=(25))
srcLable.place(x=170, y=210)
destLable= Label(bgdisplay, text="Destination", width= 20,fg='white', bg='#324752',font=(25))
destLable.place(x=170, y=260)

#SRC comboBOX
SrcCities =ttk.Combobox(bgdisplay,width= 30)
SrcCities['values']=("Ramallah","Nablus")
SrcCities.place(x=370, y=210)

#checkBOX for destinations
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
canvas.place(x=370, y=260)

#CHOICES
UCS= Button(bgdisplay, text="Uniform Cost ", width= 45,fg='white', bg='#a76316',font=(25)
            ,command=lambda :click(1,"UCS"))
UCS.place(x=170, y=460)

IDSS= Button(bgdisplay, text="Iterative Deepening ", width= 45,fg='white', bg='#a76316',font=(25)
           ,command=lambda :click(2,"IDS"))
IDSS.place(x=170, y=510)

Opt= Button(bgdisplay, text="Optimal Search",width= 45, fg='white', bg='#a76316',font=(25)
            ,command=lambda :click(3,"OPT"))
Opt.place(x=170, y=560)

mapB= Button(bgdisplay, text="Map",width=10,height=2 , fg='white', bg='#a76316',font=(25)
            ,command=lambda :showmap())
mapB.place(x=930, y=560)
'''
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
Opt2= Button(bgdisplay, text="Multiple Start-Destination Optimal Search",width= 40, fg='white',
             bg='#a76316',font=(25),command=lambda :click(3,"Bonus"))
Opt2.place(x=720, y=440)

'''


'''
#graph
graph= Button(bgdisplay, text="Click here",width= 10, height=2,fg='white', bg='#a76316',font=(25))
graph.place(x=855, y=560)

#map
map= Button(bgdisplay, text="Click here",width= 10, height=2,fg='white', bg='#a76316',font=(25))
map.place(x=1060, y=560)'''
#popup for google map
'''def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()'''


gui.mainloop()
