import IDS
from tkinter import*

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
start=''

goal="Nablus"



track=[start]
expanded= []
depth=10
cost=0
def ids():
    global cost
    global expanded
    global track
    if start == goal:
        print(start,cost)
    else:
        expanded, cost, track = IDS.check_children(adj_List_IDS, start, goal,
                                                   depth)  # method returning track and cost of the goal

        print("Nodes visited are: \n", expanded)
        print("Cost is: \n", cost)
        track.reverse()
        print("You will go through these cities till you reach ", goal, " from ", start + ":\n ")
        print(track)
        return expanded, cost, track
