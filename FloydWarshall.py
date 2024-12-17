# Floyd-Warshall Algorithm 
# CS 361 project
# Jubilation Megill
#
# Uses an implementation of the Floyd-Warshall algorithm
# to find the shortest path for all pairs
# then does a greedy approach to find an approximate shortest path from start to all items and back
#




#Find the shortest path for every pair of vertices, 
#and then uses that to find the approximate shortest path to get every item
def FloydWarshall(start,V,adj,items,doCycle=False):
    dist = []
    prev = []
    #moved from arguments to simplify calling
    n = length(V)

    nodes_explored = 0 # Counter for number of node updates--Tanner
    
    # initialize dist and prev arrays
    for i in range(0,n):
        dist.append([])
        prev.append([])
        for j in range(0,n):
                if i == j: # dist from i to i is always 0
                     dist[i].append(0)
                     prev[i].append(V[i])
                elif contains(adj[i],V[j]): # if an edge exists the dist is the edge
                     dist[i].append(1)
                     prev[i].append(V[i])
                else:
                     dist[i].append(float('inf')) # Stand in for infinity
                     prev[i].append(None)
    '''
    print("intialized lists")
    for i in range(0,n):
        print(dist[i])
       
    for i in range(0,n):
        print(prev[i])
    '''

       
    for k in range(0,n):   
        for i in range(0,n):   
            for j in range(0,n):

                nodes_explored += 1 # Increment--Tanner
                
                #print(f' {dist[i][j]} > {dist[i][k]} + {dist[k][j]}')
                if dist[i][j] > (dist[i][k] + dist[k][j]) and dist[i][k] != -1 and dist[k][j] != -1:
                    #print("updated")
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = prev[k][j]

    '''
    print("finalized lists")
    for i in range(0,n):
        print(dist[i])
       
    for i in range(0,n):
        print(prev[i])        
    '''

    path, path_weight = connectPath(start,V,dist,prev,items,doCycle) # Included path_weight--Tanner

    return path, path_weight, nodes_explored # Return path_weight and nodes_explored--Tanner

#Uses the shortest pairwise paths to create a single approximate shortest path to each item
#Can also return to start after with a slight adjustment
def connectPath(start,V,dist,prev,items,doCycle):
    path = [start]
    pathWeight = 0;
    src = start
    # this loop create the path from item to item
    while length(path) < (length(items) + 1):
        srcIndex = indexOf(src,V)
        min = None
        minValue = float('inf')

        #Find shortest path to an item we haven't visted yet
        #This is the greedy approach and will NOT always be optimal
        for item in items:
            itemIndex = indexOf(item,V)
            if dist[srcIndex][itemIndex] < minValue and (not contains(path,item)):
                min = item
                minValue = dist[srcIndex][itemIndex]

        pathWeight += minValue
        path.append(min)
        # if min is still None then from our location we cannot go to any other unvisted item
        # But since we're still in the loop that means there is some item that we haven't visited yet
        # That means the item we're at is not connected to the remaining items 
        # which means there is no path from start to all items
        if (min == None):
            print("No valid path found.\nAll items do not exist on the same component")
            return None
        src = min

    if(doCycle):
        path.append(start)
    #This line will make it return to start after collecting all items
        
    # this loop expands the path from item to item into the full path
    totalPath = []
    totalDist = 0;
    for i in range(0,length(path)-1):
        weight = dist[indexOf(path[i],V)][indexOf(path[i+1],V)]
        totalDist += weight
        temp = reconstruct(V,path[i],path[i+1],prev,weight)
        for j in temp:
            totalPath.append(j)

        
    return totalPath, totalDist

#Uses the prev array to reconstruct the exact path between two vertices
def reconstruct(V,src,dest,prev,w):
    path = [None] * w
    index = w-1
    current = dest
    while current != src:
        path[index] = current
        index -= 1
        current = prev[indexOf(src,V)][indexOf(current,V)]

    if index >= 0:
        #actual path length != w
        print("INVALID ARGUMENTS")
    
    #path[0] = src
    return path

def matrixToGraph(matrix):
    vertices = []
    adj = []
    n = length(matrix)
    #theres no point in turning an empty matrix into a graph
    if n == 0 :
        print("Invalid matrix")
        return
    m = length(matrix[0])
    index = 0;
    for i in range(0,n):
        for j in range(0,m):
            if matrix[i][j] != 1:
                #add (i,j) to the list of vertices
                vertices.append((i,j))
                adj.append([])
                #add adjcent tiles to the adjcency list of (i,j) 
                #it may not exist yet, but that doesn't matter
                #Check up
                if i-1 > -1 and matrix[i-1][j] != 1:
                    adj[index].append((i-1,j))
                #Check left
                if j-1 > -1 and matrix[i][j-1] != 1:
                    adj[index].append((i,j-1))
                #Check down
                if i+1 < n and matrix[i+1][j] != 1:
                    adj[index].append((i+1,j))
                #check right
                if j+1 < m and matrix[i][j+1] != 1:
                    adj[index].append((i,j+1))
                index += 1  
                 
    return vertices, adj


def displayPath(path,vertices,n,m):
    if path == None:
        return
    matrix = [[]]
    counter = 1;
    for i in range(0,n):
        matrix.append([])
        for j in range(0,m):
            matrix[i].append(0)

    for v in path:
        index = v-1
        matrix[int(index/n)][index%n] += 1
    for i in range(0,n):
        for j in range(0,m):
            print(matrix[i][j],end=" ")
        print()
    return



# these functions probably exist, but just to be extra sure i'm remaking them
# returns if the value exists in the array
def contains(array,value):
    for i in array:
        if i == value:
            return True
    return False

#returns the index of x in list
def indexOf(x,list):
    for i in range(0,length(list)):
        if list[i] == x:
            return i;
    return -1

#returns the length of list
def length(list):
    count = 0
    for _ in list:
        count += 1
    return count

        
'''
# Old main test code
# matrix test cases
empty = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
warehouse = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],  
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]
impossible = [
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 0, 1, 0],  
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]
minitest = [
    [0, 0],
    [0, 0]  
]

testCase = empty
testItems = [(1,1),(2,2),(3,3)]
testStart = (0,0)

#THIS PART GOES IN MAIN LATER
#Floyd-Warshall
print("\n--- Floyd_Warshall Algorithm ---")
testVertices, testAdj = matrixToGraph(testCase)#Conversion step (Matrix -> Graph)
FWPath, FWLength = FloydWarshall(testStart,testVertices,testAdj,testItems[:]) # Actual algorithm
print("Floyd-Warshall Result:", FWPath)
print("Floyd-Warshall Path Length:", FWLength)
'''
'''
for v in vertices:
    print(v)

for a in adj:
    print(a)
'''
#Direct graph test cases
#items = ['B','C','G']
#items = ['A','B','C','D','E','F','G'] # it currently cannot handle start being an item
#items = ['B','C','D','E','F','G']
#vertices = ['A','B','C','D','E','F','G']
#start = 'A'
#adj = [['B','C'],['D','F'],['D','E'],['E'],['F'],['G'],['A']]
#vertices = ['A','B','C','D']
#adj = [['B'],['C'],['D'],['A']]





