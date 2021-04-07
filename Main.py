import IDS


adj_List = {
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
start = "Ramallah"
goals = ["Tiberias","Ramallah"]
cost=0
depth=20

for goal in goals:
    expanded, cost, track = IDS.check_children(adj_List, start, goal,
                                               depth)  # method returning track and cost of the goal
    print("Nodes visited are: \n", expanded)
    print("Cost is: \n", cost)
    track.reverse()
    print("You will go through these cities till you reach ", goal, " from ", start + ":\n ")
    print(track)
    print("NEXT\n\n")












