class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in edges: #start and end doa varaiale since each edges ka list ka har item 2 var rakhta hai
            if start in self.graph_dict:# jab key dekhn hoa toa only name start and value toa [start] ka value
                self.graph_dict[start].append(end)
                #end if mai end and else mai [end] yese use hua hai since append hai toa jaisa already hai
                #usea hi kar degga and [end] mai since 1st time jaa raha hai an humlog ko
                #joa chahiya bus [] yese form mai hi chaiya list ke form
            else:
                self.graph_dict[start]=[end]

        print(self.graph_dict)

    def get_paths(self,start,end,path=[]):
        path = path + [start]   #start ko [] iske andar taki start ka value '' iske sath ayea
        #ye path only to see yahah se yaha yak yaea hoa ye final output nahi hai joa pass hota hai result mai
        if start not in self.graph_dict:
            return []
        if start == end :
            return [path]

        temp_path=[]  # ye hai final value hai joa pass hota hai result mai
        for node in self.graph_dict[start]:
            if node not in path:#for check ki kahi loop wala scen na ho jayea
                new_path = self.get_paths(node,end,path)
                #new path sab path ka vaule rakhta hai isliye isko append karte hai temp_path since woa hamara
                #ans hai
                for p in new_path:
                    temp_path.append(p)
                    #append karte hai taki joa iss function ko call kiya hai usko sara result mil jayea and temp_path
                    #ans hai
        #at last jab sara case traveal ho ajyega toa sabkoi apna result new path ko return kar degga
        #mtlb 1st time jab ye funcion call hua tha soa sabka phir last mai append hoa jayega
        #toa sabko append karke ans le loa bus and for shortest mai ek chahiya soa lengh leke
        #minimum dekh loa bus

        return temp_path






if __name__=='__main__':
    routes=[
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    route_graph=Graph(routes)
    start = "Mumbai"
    end = "New York"
    print(route_graph.get_paths(start,end))

