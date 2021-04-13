import sys

paths = {}
optimalpath = []


# to save all paths from start node to each goal node


def astar(start_node, stop_node, Graph_nodes):
    open_set = [start_node]
    visited = []
    f = {}
    parents = {}

    # ditance of starting node from itself is zero
    f[start_node] = 0
    # start_node is root node i.e it has no parent nodes
    # so start_node is set to its own parent node
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        # node with lowest f() is found
        for v in open_set:
            if n is None:
                n = v
                continue
            else:
                if f[v] < f[n]:
                    n = v

        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            for (m, h, weight) in get_neighbors(n, Graph_nodes):
                if m not in open_set and m not in visited:
                    open_set.append(m)
                    parents[m] = n
                    f[m] = f[n] + int(weight) + int(h)

                else:
                    if f[m] > f[n] + int(weight) + int(h):
                        # update g(m)
                        f[m] = f[n] + int(weight) + int(h)
                        # change parent of m to n
                        parents[m] = n

                        # if m in closed set,remove and add to open
                        if m in visited:
                            visited.remove(m)
                            open_set.append(m)
                        # open_set.add(m)

        if n is None:
            print('Path does not exist!')
            return None

        # if the current node is the stop_node
        # then we begin reconstruct the path from it to the start_node
        if n == stop_node:
            path = []
            cost = []

            while parents[n] != n:
                path.append(n)
                cost.append(f[n])
                n = parents[n]

            path.append(start_node)
            cost.append(f[start_node])
            tot = cost[0]
            path.reverse()
            cost.reverse()

            #            print('Path found: {}'.format(path))
            #            print('with cost = {}'.format(cost))
            fcost = path
            fcost.append(tot)
            paths[stop_node] = list(fcost)
            #            print("here is path "+ str(paths))
            return path

        open_set.remove(n)
        visited.append(n)

    print('Path does not exist!')
    return None


# define fuction to return neighbor and its distance
# from the passed node
def get_neighbors(v, Graph_nodes):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def check_goals(start, goals, graph):
    i = 0
    num = {}
    # check path between start node with each goal node
    while i < len(goals):
        astar(start, goals[i], graph)
        i = i + 1

    # to check number of goal cities reached in each path
    for g in goals:
        num[g] = 0
        for g1 in goals:
            if g1 in paths[g]:
                num[g] = num[g] + 1

    #   to check if all have the same value so we chose least cost path
    maxx = max(num.values())
    c = list(paths.keys())[list(num.values()).index(maxx)]
    #    while len(goals) > 0:
    if len(goals) == maxx:
        print("optimal path " + str(paths[c]))
        l = len(paths[c])

        return list(paths[c][l-2]),paths[c][l-1]


#    if len(goals) == 1 and maxx == 1:
#        print("optimal path " + str(paths))
#        sys.exit()
    if maxx == 1 and len(goals) > 1:  # no more than one goal city reached
        ind = len(paths[goals[0]]) - 1  # we need to find least cost instead
        max2 = paths[goals[0]][ind]
        n = 0
        s = goals[0]  # name of city has least cost path
        while n < len(goals):
            ind = len(paths[goals[n]]) - 1
            #                ind2 = len(paths[goals[n + 1]]) - 1
            if paths[goals[n]][ind] < max2:
                max2 = paths[goals[n]][ind]
                s = goals[n]
            n = n + 1
        goals.remove(s)
#        optimalpath = paths[s]
        if len(goals) == 1:
            check_goals(s, goals, graph)

    else:
        j = len(goals) - maxx
        while len(goals) != j:
            for g2 in goals:
                if g2 in paths[c]:
                    goals.remove(g2)

        if j == 1:
            optimalpath = paths[c] + astar(c, goals[0], graph)
            print("Optimal path :{}".format(optimalpath))

        else:
#            optimalpath = paths[city]
            check_goals(c, goals, graph)
    return list(paths[c][:len(paths[c])-2]),paths[c][len(paths[c])-1]

#    pass


def main(start_city,goal_cities):
    # Describe your graph here
    Graph_nodes = {"Ramallah":[ ("Nablus",'25', '50'), ("Salfit",'27','54'), ("Jericho",'19','37'), ("Jerusalem",'10','19')],
    "Nablus":[("Tubas",'11','21'), ("Tulkarm",'15','29'), ("Qalqilia",'16','32'), ("Salfit",'15','29'),("Ramallah",'25','50'), ("Jericho",'35','70'),
              ("Jenin",'22','43')],
    "Jerusalem":[("Ramallah",'10','19'), ("Jericho",'19','38'), ("Bethlehem",'7','13'),("Yafo",'34','67')],
    "Jenin":[("Tulkarm",'21', '52'), ("Nablus",'22','43'), ("Tubas",'15','30'),("Nazareth",'20','33'),("Tiberias",'30','46')],
    "Tubas":[("Jenin",'20','30'), ("Nablus",'16','21'),("Jericho",'25','50')],
    "Nazareth":[("Jenin",'16','33'),("Tiberias",'15''30'),("Carmiel",'20','41'),("Acre",'20','39')],
    "Carmiel":[("Ra's alnaqoura",'15','30'), ("Acre",'11','22'), ("Nazareth",'20','39'), ("Tiberias",'20','40')],
    "Tulkarm":[("Jenin",'26','52'), ("Nablus",'15','29'),("Qalqilia",'19','34'),("Yafo",'25','46')],
    "Qalqilia":[("Nablus",'16','32'), ("Tulkarm",'19','34'),("Salfit",'21','37'),("Yafo",'20','39')],
    "Salfit":[("Nablus",'15','29'),("Ramallah",'30','54'),("Qalqilia",'20','37'),("Yafo",'30','60')],
    "Hebron":[("Bethlehem",'12','24'),("Bir Alsabe'",'30','60')],
    "Bethlehem":[("Hebron",'12','24'), ("Jerusalem",'10','13')],
    "Jericho":[("Tubas",'30','50'), ("Nablus",'40','70'), ("Ramallah",'26','37'),("Jerusalem",'16','38'),("Tiberias",'60','122')],
    "Tiberias":[("Nazareth",'15','30'), ("Carmiel",'20','40'), ("Jericho",'60','122'), ("Jenin",'22','46')],
    "Haifa":[("Acre",'17','25'), ("Yafo",'45','92')],
    "Bir Alsabe'":[("Hebron",'30','60')],
    "Acre":[("Carmiel",'11','22'), ("Haifa",'13','25'), ("Nazareth",'20','39'), ("Ra's alnaqoura",'7','12')],
    "Yafo":[("Haifa",'50','92'), ("Tulkarm",'30','46'), ("Qalqilia",'20','39'), ("Salfit",'35','60'), ("Jerusalem",'40','67')],
    "Ra's alnaqoura":[("Carmiel",'15','30'), ("Acre",'6','12')]}

    if start_city not in Graph_nodes:
        print("check Start city ")

    else:
        for n in goal_cities:
            if n not in Graph_nodes:
                print("check goal cities ")

    path=[]
    path,cost=check_goals(start_city, goal_cities, Graph_nodes)
    return
