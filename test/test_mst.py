import pytest
import numpy as np
from mst import Graph
from sklearn.metrics import pairwise_distances



def check_mst(adj_mat: np.ndarray, 
              mst: np.ndarray, 
              expected_weight: int, 
              allowed_error: float = 0.0001):
    """
    
    Helper function to check the correctness of the adjacency matrix encoding an MST.
    Note that because the MST of a graph is not guaranteed to be unique, we cannot 
    simply check for equality against a known MST of a graph. 

    Arguments:
        adj_mat: adjacency matrix of full graph
        mst: adjacency matrix of proposed minimum spanning tree
        expected_weight: weight of the minimum spanning tree of the full graph
        allowed_error: allowed difference between proposed MST weight and `expected_weight`

    TODO: Add additional assertions to ensure the correctness of your MST implementation. For
    example, how many edges should a minimum spanning tree have? Are minimum spanning trees
    always connected? What else can you think of?

    """

    def approx_equal(a, b):
        return abs(a - b) < allowed_error

    total = 0
    for i in range(mst.shape[0]):
        for j in range(i+1):
            total += mst[i, j]
    assert approx_equal(total, expected_weight), 'Proposed MST has incorrect expected weight'
    
    #we check that the MST has n-1 edges
    edge_count = 0 #initialize counter
    #iterating through the lower triangle of the matrix
    for i in range(mst.shape[0]): 
        for j in range(i+1):
            if mst[i,j] != 0: #if the edge exists
                edge_count += 1 #increment the counter
    assert edge_count == mst.shape[0] - 1 #assert that the number of edges is n-1
    
    #check that MST and adjacency matrix have the same dimensions
    assert mst.shape == adj_mat.shape        
    

def test_mst_small():
    """
    
    Unit test for the construction of a minimum spanning tree on a small graph.
    
    """
    file_path = './data/small.csv'
    g = Graph(file_path)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 8)


def test_mst_single_cell_data():
    """
    
    Unit test for the construction of a minimum spanning tree using single cell
    data, taken from the Slingshot R package.

    https://bioconductor.org/packages/release/bioc/html/slingshot.html

    """
    file_path = './data/slingshot_example.txt'
    coords = np.loadtxt(file_path) # load coordinates of single cells in low-dimensional subspace
    dist_mat = pairwise_distances(coords) # compute pairwise distances to form graph
    g = Graph(dist_mat)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 57.263561605571695)


def test_mst_student():
    """
    
    TODO: Write at least one unit test for MST construction.
    
    """
    #we test that an error is raised when a graph is not connected 
    disconnected_graph = './data/disconnected.csv' #to make this, i took the small graph and added a disconnected fifth node
    g = Graph(disconnected_graph) #create instance of graph
    with pytest.raises(ValueError): #assert that an error is raised when the graph is not connected
         g.construct_mst()
         
    #test for an empty graph (i'll note that a warning is raised when the graph is empty due to how the file is loaded, but the function runs)
    empty_graph = './data/empty.csv' #blank csv file 
    empty_g = Graph(empty_graph) #create instance of graph
    with pytest.raises(ValueError): #assert that an error is raised when the graph is empty
        empty_g.construct_mst()
    