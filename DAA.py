def add_vertex(v):
    vertices.append(v)

    row = []
    for i in range(len(vertices)-1) :
        row.append(0)

    graph.append(row)
    for i in graph:
        i.append(0)

def add_edge(v1,v2):
    row = vertices.index(v1)
    column = vertices.index(v2)
    graph[row][column] = 1
    graph[column][row] = 1  

def delete_edge(v1,v2):
    row = vertices.index(v1)
    column = vertices.index(v2) 
    graph[row][column] = 0
    graph[column][row] = 0

def delete_vertex(v):
    v_index = vertices.index(v)
    graph.pop(v_index)

    for i in graph:
        i.pop(v_index)
    vertices.remove(v)

                           
vertices = []
graph = []
add_vertex("A")
add_vertex("TD")
add_vertex("N")
add_edge("A","N")
add_edge("N","TD")
add_edge("A","TD")

print(graph)
