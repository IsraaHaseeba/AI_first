


def sub_IDS(ajd_List,start, goal, level,exapnded,track):

    if start == goal:
        return True
    if level==0:
        return False

    for child in ajd_List[start]:
        if child not in exapnded:
            exapnded.append(child) #this child will be expanded

        if (sub_IDS(ajd_List, child, goal, level - 1, exapnded,track)):
            track.append(child)
            return True


    return False




def check_children(ajd_List,start,goal,depth):
    track=[]
    exapnded = []
    exapnded.append(start)
    tempLevel = 1
    for level in range(1, depth):
        if(sub_IDS(ajd_List,start, goal, level,exapnded,track)):
            tempLevel=level
            track.append(start)
            return exapnded,level,track
    track.append(start)
    return exapnded,tempLevel,track




