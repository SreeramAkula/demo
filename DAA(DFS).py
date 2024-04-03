def dfs(v,visited,graph) :
    explore = []
    explore.append(v)
    if v not in visited:
        visited.append(v)

    while(len(explore) !=0 ):
        count = 0
        for i in graph[v]:

            if i not in visited:
                explore.append(i)
                visited.append(i)
                v = i
                count +=1
                break
            if count ==0:
                explore .pop()
                if(len(explore) !=0) :
                    v=explore[-1]
    print(visited)

    visited = []
    graph = dict()
    add_vertex("A")
    add_vertex("TD")
    add_vertex("C")
    add_vertex("IM")
    add_vertex("N")
    add_vertex("E")
    add_vertex("X")
    add_vertex("K")
    add_vertex("F")
    add_vertex("Y")  

    add_edge("A","TD")
    add_edge("TD","C")
    add_edge("C","IM")
    add_edge("IM","N")
    add_edge("N","A")
    add_edge("N","E")
    add_edge("X","E")
    add_edge("N","K")
    add_edge("K","F")
    add_edge("A","Y")
    

