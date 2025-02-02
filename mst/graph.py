import numpy as np
import heapq
from typing import Union

class Graph:

    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """
    
        Unlike the BFS assignment, this Graph class takes an adjacency matrix as input. `adjacency_mat` 
        can either be a 2D numpy array of floats or a path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph.
    
        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')        
        
    def construct_mst(self):
        """
    
        TODO: Given `self.adj_mat`, the adjacency matrix of a connected undirected graph, implement Prim's 
        algorithm to construct an adjacency matrix encoding the minimum spanning tree of `self.adj_mat`. 
            
        `self.adj_mat` is a 2D numpy array of floats. Note that because we assume our input graph is
        undirected, `self.adj_mat` is symmetric. Row i and column j represents the edge weight between
        vertex i and vertex j. An edge weight of zero indicates that no edge exists. 
        
        This function does not return anything. Instead, store the adjacency matrix representation
        of the minimum spanning tree of `self.adj_mat` in `self.mst`. We highly encourage the
        use of priority queues in your implementation. Refer to the heapq module, particularly the 
        `heapify`, `heappop`, and `heappush` functions.

        """
        n = self.adj_mat.shape[0] #the number of nodes in the graph is the number of rows (or columns) in the adjacency matrix
        
        if n == 0: #if the adjacency matrix is empty, raise a ValueError
            raise ValueError()
    
        visited = [] #initialize a list to keep track of which nodes have been visited
        
        mst = np.zeros((n, n)) #create empty nxn matrix to store the MST 
        
        start = np.random.randint(n) #pick a random starting node
        
        visited.append(start) # add the starting node to the visited list

        #initialize a priority queue to store the edges of all the nodes connected to the starting node
        #where each edge is a tuple of the form (weight, start node, end node)
        pq = [(self.adj_mat[start, end], start, end) for end in range(n) if self.adj_mat[start, end] != 0]
        
        heapq.heapify(pq) #this turns the list into a heap, which will allow us to get the edge with the smallest weight
        
        #while the priority queue is not empty
        while len(pq) != 0:
            weight, start, end = heapq.heappop(pq) #getting the edge with the smallest weight
            if end not in visited: #if the end node has not been visited
                mst[start, end] = weight #add the edge to the MST
                mst[end, start] = weight 

                visited.append(end) #add end node to the visited list
                
                #add the end node's connected edges to the priority queue (ensuring that they haven't already been visited)
                for next, weight in enumerate(self.adj_mat[end]): 
                    if weight != 0 and next not in visited: 
                        heapq.heappush(pq, (weight, end, next)) #adding to the heap 
        
        #at the end of prim's algorithm, we should have visited all the nodes in the graph
        if len(visited) != n:
            raise ValueError() #otherwise, raise an error because the graph is not connected
        #add as attribute 
        self.mst = mst
