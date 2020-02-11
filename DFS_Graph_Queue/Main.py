from pythonds import Graph,Vertex,DFSGraph,PriorityQueue
from Queue import Queue
import sys

mygraph = Graph()

def Main():
    done = False
    print('NOTES!! For entering manually make sure the graph is entered in the format of a-b: 1\n'
           ' when reading in the graph text files they must be in the same format a-b: 1\n'
          ' make sure to choose the correct choice when reading in the text files for directed \n'  
          'or undirected graphs\n'
          'Once a file is read in, the program must be ended and restarted to enter another graph\n'
          '\n Make sure when entering paths, the capitalization is the same or it will not work')
#main menu loops through until exit or error is thrown.
    while not done:
        print('\nMain Menu:')
        print('1. Enter a graph\n2. Read Graph from file.\n3. View graph\n'
          '4. Single-Source shortest path\n'
          '5. All-pairs shortest path\n'
          '6. Topological sort\n'
          '7. Exit the program\n')
        done = True
    
        selection = input('Enter Your Selection [1-7]: ')
# calls the create graph function to allow you to input graph manualy 
        if selection == '1':
            create_graph()
            done = False
# asks you if the graph is directed or not and calls the appropiate function based on input and create graph from that file

        if selection == '2':
            choice = input('press 1. for directed graph\npress 2. for undirected graph.')
            if choice == '1':
                file = input('Enter a file for a DIRECTED graph.')
                import_D_graph(file)
            if choice == '2':
                file = input('Enter a file for a UNDIRECTED graph.')
                import_graph(file)
            done = False
            
# prints out the graph after is is created, not in any sorted order, will be random everytime
        if selection == '3':
            print_graph(mygraph)
            done = False
            
# gets and displays the shortest path from a start vertex
        if selection == '4':
            start = input('Please enter a start vertex: ')
            print('The shortest paths from vertex',start,'are:')
            vert = mygraph.getVertex(start)
            for v in mygraph:
                ssp(mygraph,v)
                print('\n',v.getId(),vert.getDistance(),end='')
            done = False

            
# creates a matrix of all the shortest paths between all vertices    
        if selection == '5':
            for v in mygraph:
                print('\t',v.getId(),end='')
            print()
            for v in mygraph:
                print('\n',v.getId(),end='')
                ssp(mygraph,v)
                for w in mygraph:
                    print('\t',w.getDistance(),end='')
            done = False
            
# uses topological sort and return vertices in decreasing order of run time
        if selection == '6':
            key = input('Please enter a start vertex: ')
            vert = mygraph.getVertex(key)
            DFSgraph = DFSGraph()
            DFSgraph.dfs()
            DFSgraph.dfsvisit(vert)
            done = False
            
        if selection == '7':
            print('GoodBye')
            sys.exit()
            
# create manual graph method     
def create_graph():
    create_done = False
    while not create_done:
        edge = input('Enter an edge or return to quit:')
        if edge != '':
            Vertex1 = edge[0]
            Vertex2 = edge[2]
            weight = edge[4:len(edge)]
            weight = int(weight)
            Vertex1 = (Vertex1)
            Vertex2 = (Vertex2)
            weight = (weight)
            mygraph.addEdge(Vertex1,Vertex2,weight)
            mygraph.addEdge(Vertex2,Vertex1,weight)
        if edge == '':
            print ('Graph created successfully')
            create_done = True
    return mygraph
# create manual directed graph
def create_D_graph():
    create_done = False
    while not create_done:
        edge = input('Enter an edge or return to quit:')
        if edge != '':
            Vertex1 = edge[0]
            Vertex2 = edge[2]
            weight = edge[4:len(edge)]
            weight = int(weight)
            Vertex1 = (Vertex1)
            Vertex2 = (Vertex2)
            weight = (weight)
            mygraph.addEdge(Vertex1,Vertex2,weight)
        if edge == '':
            print ('Graph created successfully')
            create_done = True
    return mygraph
# import underected graph
def import_graph(file):
    
        graphFile = open(file,'r')
        for line in graphFile:
            Vertex1 = line[0]
            Vertex2 = line[2]
            weight = line[4:len(line)]
            weight = int(weight)
            Vertex1 = (Vertex1)
            Vertex2 = (Vertex2)
            weight = (weight)
            mygraph.addEdge(Vertex1,Vertex2,weight)
            mygraph.addEdge(Vertex2,Vertex1,weight)
        return mygraph

# import directed graph
def import_D_graph(file):
        graphFile = open(file,'r')
        for line in graphFile:
            Vertex1 = line[0]
            Vertex2 = line[2]
            weight = line[4:len(line)]
            weight = int(weight)
            Vertex1 = (Vertex1)
            Vertex2 = (Vertex2)
            weight = (weight)
            mygraph.addEdge(Vertex1,Vertex2,weight)
        return mygraph

# sortest single path function 
def ssp(graph,start):
    
    for v in graph:
        v.setDistance(10000)
        
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v)for v in graph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist< nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)
                
#prints out graph for option three       
def print_graph(graph):
    for v in graph:
        for n in v.getConnections():
            print('Vertex path\tWeight\n',v.getId(),n.getId(),'\t\t',v.getWeight(n))



Main()
      

