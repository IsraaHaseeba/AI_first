import sys
from queue import PriorityQueue

visited = set()
def ucs(graph, source, destination):
    path=[]
    cost=0
    queue = PriorityQueue()
    queue.put((0, [source]))  # starting node

    while queue:
        # if no path is present beteween two nodes
        if queue.empty():
            print('there is no route ')
            return path,cost
        cost, path = queue.get()
        node = path[len(path) - 1]

        if node not in visited:
            visited.add(node)
            if node == destination:

                return path,cost

            for n in neighbors(graph, node):
                if n not in visited:
                    t_cost = cost + int(find_cost(graph, node, n))
                    temp = path[:]
                    temp.append(n)
                    queue.put((t_cost, temp))
    return path,t_cost


# function for finding neighbors in the graph
def neighbors(graph, node):
    points = graph[node]
    return [n[0] for n in points]


# function to calculate the cost of path beteween two nodes
def find_cost(graph, node_A, node_B):
    location = [n[0] for n in graph[node_A]].index(node_B)
    return graph[node_A][location][1]


# print the result of search
def display_path(graph, path,cost):
    distance =cost

    cost=[]
    print('Best route: ')
    for p in path[:-2]:
        q = path.index(p)
        location = [r[0] for r in graph[p]].index(path[q + 1])
        cost.append(graph[p][location][1])
        #print(p + ' to ' + path[q + 1] + ', ' + cost + ' km')
    print('with distance = ' + str(distance) + ' km')
    return cost,path

# defining the main function with all the arguments
def main(source,destination):


    graph = { "Ramallah":[ ("Nablus",'50'), ("Salfit",'54'), ("Jericho",'37'), ("Jerusalem",'19')],
    "Nablus":[("Tubas",'21'), ("Tulkarm",'29'), ("Qalqilia",'32'), ("Salfit",'29'),("Ramallah",'50'), ("Jericho",'70'),("Jenin",'43')],
    "Jerusalem":[("Ramallah",'19'), ("Jericho",'38'), ("Bethlehem",'13'),("Yafo",'67')],
    "Jenin":[("Tulkarm", '52'), ("Nablus",'43'), ("Tubas",'30'),("Nazareth",'33'),("Tiberias",'46')],
    "Tubas":[("Jenin",'30'), ("Nablus",'21'),("Jericho",'50')],
    "Nazareth":[("Jenin",'33'),("Tiberias",'30'),("Carmiel",'41'),("Acre",'39')],
    "Carmiel":[("Ra's alnaqoura",'30'), ("Acre",'22'), ("Nazareth",'39'), ("Tiberias",'40')],
    "Tulkarm":[("Jenin",'52'), ("Nablus",'29'),("Qalqilia",'34'),("Yafo",'46')],
    "Qalqilia":[("Nablus",'32'), ("Tulkarm",'34'),("Salfit",'37'),("Yafo",'39')],
    "Salfit":[("Nablus",'29'),("Ramallah",'54'),("Qalqilia",'37'),("Yafo",'60')],
    "Hebron":[("Bethlehem",'24'),("Bir Alsabe'",'60')],
    "Bethlehem":[("Hebron",'24'), ("Jerusalem",'13')],
    "Jericho":[("Tubas",'50'), ("Nablus",'70'), ("Ramallah",'37'),("Jerusalem",'38'),("Tiberias",'122')],
    "Tiberias":[("Nazareth",'30'), ("Carmiel",'40'), ("Jericho",'122'), ("Jenin",'46')],
    "Haifa":[("Acre",'25'), ("Yafo",'92')],
    "Bir Alsabe'":[("Hebron",'60')],
    "Acre":[("Carmiel",'22'), ("Haifa",'25'), ("Nazareth",'39'), ("Ra's alnaqoura",'12')],
    "Yafo":[("Haifa",'92'), ("Tulkarm",'46'), ("Qalqilia",'39'), ("Salfit",'60'), ("Jerusalem",'67')],
    "Ra's alnaqoura":[("Carmiel",'30'), ("Acre",'12')]}

    if source not in graph.keys():
        print('Start city not found')
        sys.exit()

    if destination not in graph.keys():
        print('Destination city not found')
        sys.exit()

    visited.clear()
    path,cost=ucs(graph, source, destination)
    #cost,track=display_path(graph, path,cost)
    print(path)
    print(visited)
    print(cost)
    return list(visited),cost,path


if __name__ == '__main__':

    main("Ramallah", "Nablus")
    main("Nablus", "Jericho")