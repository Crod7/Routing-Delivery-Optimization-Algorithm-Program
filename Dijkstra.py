

def dijkstra_short_path(g, start_vertex):
    unvisited_queue = []
    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)
    start_vertex.distance = 0
    while len(unvisited_queue) > 0:
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)
        #check potential path lengths from the current vertext to all neighbors
        for adj_vertex in g.adjacency_list[current_vertex]:
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = current_vertex.distance + edge_weight

            #if shorter path from start_vertex to add_vertex is found,
            #update adj_vertex's distance and predecessor

            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex

def get_shortest_path(start_vertex, end_vertex):
    path = ' '
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = '->' + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path