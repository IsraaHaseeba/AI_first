import sys
from queue import PriorityQueue

visited = set()


def ucs(graph, source, destination):
    queue = PriorityQueue()
    queue.put((0, [source]))  # starting node

    while queue:
        # if no path is present between two nodes
        if queue.empty():
            print('there is no route ')
            return
        cost, path = queue.get()
        node = path[len(path) - 1]

        if node not in visited:
            visited.add(node)
            if node == destination:
                path.append(cost)
                return path

            for n in neighbors(graph, node):
                if n not in visited:
                    t_cost = cost + int(find_cost(graph, node, n))
                    temp = path[:]
                    temp.append(n)
                    queue.put((t_cost, temp))


# function for finding neighbors in the graph
def neighbors(graph, node):
    points = graph[node]
    return [n[0] for n in points]


# function to calculate the cost of path between two nodes
def find_cost(graph, node_A, node_B):
    location = [n[0] for n in graph[node_A]].index(node_B)
    return graph[node_A][location][2]


# print the result of search
def display_path(graph, path):
    distance = path[-1]
    print("Best route:")
    for p in path[:-2]:
        q = path.index(p)
        location = [r[0] for r in graph[p]].index(path[q + 1])
        cost = graph[p][location][2]
        print(p + ' to ' + path[q + 1] + ', ' + cost + ' km')
    print('with total distance = ' + str(distance) + ' km')


# defining the main function with all the arguments
def main():
    source = input("please enter source city: ")
    destination = list(map(str, input("Enter destination cities: ").split()))

    graph = {'Jenin': [('Tulkarm', '25', '52'), ('Nablus', '21', '43'), ('Tiberias', '23', '46'),
                       ('Nazareth', '16', '33')],
             'Tulkarm': [('Jenin', '25', '52'), ('Nablus', '15', '29'), ('Qalqilia', '17', '34'), ('Yafo', '23', '46')],
             'Nablus': [('Jenin', '21', '43'), ('Jericho', '35', '70'), ('Ramallah', '25', '50'),
                        ('Tulkarm', '15', '29'), ('Qalqilia', '16', '32'), ('Salfit', '15', '29')],
             'Tiberias': [('Jenin', '23', '46'), ('Jericho', '61', '122'), ('Nazareth', '15', '30')],
             'Nazareth': [('Jenin', '16', '33'), ('Jenin', '17', '33')],
             'Salfit': [('Qalqilia', '19', '37'), ('Ramallah', '27', '54'), ('Nablus', '15', '29'),
                        ('Yafo', '30', '60')],
             'Qalqilia': [('Tulkarm', '17', '34'), ('Salfit', '19', '37'), ('Nablus', '16', '32'),
                          ('Yafo', '19', '39')],
             'Bethlehem': [('Jerusalem', '7', '13'), ('Hebron', '12', '24')],
             'Jerusalem': [('Bethlehem', '7', '13'), ('Jericho', '19', '38'), ('Ramallah', '10', '19'),
                           ('Yafo', '34', '67')],
             'Hebron': [('Bethlehem', '12', '24')],
             'Jericho': [('Jerusalem', '19', '38'), ('Ramallah', '18', '37'), ('Nablus', '35', '70'),
                         ('Tiberias', '61', '122')],
             'Ramallah': [('Jerusalem', '10', '19'), ('Jericho', '18', '37'), ('Nablus', '25', '50'),
                          ('Salfit', '27', '54')],
             'Yafo': [('Jerusalem', '34', '67'), ('Tulkarm', '23', '46'), ('Qalqilia', '19', '39'),
                      ('Salfit', '30', '60')]}

    if source not in graph.keys():
        print('Start city not found')
        sys.exit()

    for n in destination:
        if n not in graph.keys():
            print('Destination city: ' + n + ' not found')
            continue
        print("==> route from ", source, " to ", n, ":")
        visited.clear()
        path = ucs(graph, source, n)

        if path:
            print("visited nodes: ", visited)
            display_path(graph, path)


# calling for the execution of the main function
if __name__ == '__main__':
    main()
