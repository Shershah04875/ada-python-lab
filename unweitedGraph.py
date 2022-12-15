# Edges to adjacency list of weighted undirected graph
v = int(input("Enter Number of vertices: "))

adjacency_list = {}

edges = int(input("Enter number of edges: "))

print("\nStart Entering edges (s,d,w) : ")
for i in range(edges):
    v1,v2,w = list(map(int,input().split(" ")))
    
    if v1 in adjacency_list:
        adjacency_list[v1].append((v2,w))
    else:
        adjacency_list[v1] = [(v2,w)]
    
    if v2 in adjacency_list:
        adjacency_list[v2].append((v1,w))
    else:
        adjacency_list[v2] = [(v1,w)]

print("\nAdjacency List is: ")
for vertex in adjacency_list.keys():
    print(f"{vertex} -> {adjacency_list[vertex]}")