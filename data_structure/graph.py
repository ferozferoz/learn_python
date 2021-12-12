from collections import defaultdict


class Graph:

    dict_vertex_neighbours = defaultdict(list)

    def add_edge(self, key, value):

        if value not in self.dict_vertex_neighbours[key]:
            self.dict_vertex_neighbours[key].append(value)
        if key not in self.dict_vertex_neighbours[value]:
            self.dict_vertex_neighbours[value].append(key)

    def traverse_path(self,start,end,path):
        if path is None:
            path = []
        if start == end:
            path = path + [start]
            print(path)

        else:
            path = path + [start]

            #print("Start {} End {}".format(start,end))

            list_vertex = self.dict_vertex_neighbours[start]
            if end in list_vertex:
                self.traverse_path(end, end, path)
            else:
                for vertex in list_vertex:
                    if vertex not in path:
                        self.traverse_path(vertex, end, path)


    def kruskal(self):
        unique_set=[]
        spanning_tree = []
        for key in self.dict_vertex_neighbours:
            for value in self.dict_vertex_neighbours[key]:
                if key in unique_set and value in unique_set:
                    pass
                else:
                    spanning_tree.append((key,value))
                    if key not in unique_set:
                        unique_set.append(key)
                    if value not in unique_set:
                        unique_set.append(value)

        return spanning_tree

    def print_edges(self):

        unique_list = []
        count_edges = 0

        for key in self.dict_vertex_neighbours:
            for value in self.dict_vertex_neighbours[key]:
                if (key,value) not in unique_list:
                    count_edges+=1
                    print("key: "+key+" value: "+value)
                    unique_list.append((key,value))
                    unique_list.append((value, key))

        print("total edges: {}".format(count_edges))
        print(self.dict_vertex_neighbours)


if __name__ == "__main__":

    list_vertex_pair = [('a', 'b'), ('b', 'f'), ('f', 'd'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'a') , ('c','f')]
    graphDemo = Graph()
    for elements in list_vertex_pair:
        (key,value) = elements
        graphDemo.add_edge(key,value)

    #graphDemo.print_edges()

    graphDemo.traverse_path('a', 'f', None)
    #print(graphDemo.kruskal())