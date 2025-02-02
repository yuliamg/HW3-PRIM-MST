# HW 3: Prim's algorithm

![BuildStatus](https://github.com/yuliamg/HW3-PRIM-MST/actions/workflows/test.yml/badge.svg)

In this assignment, you'll implement Prim's algorithm, a non-trivial greedy algorithm used to construct minimum spanning trees. 

## Methods Description 

### Constructing a minimum spanning tree
- The function _**construct_mst**_ implements Prim's algorithm to construct a minimum spanning tree. The function first initializes an empty NxN matrix, as well as a visited list used to keep track of nodes that have been explored. It selects a random starting node and then creates a priority queue containing the nodes connected to the starting node and the weight of the edge. We use a heap to store the connected edges sorted by minimum weight, enabling us to select the minimum weight edge to add to the minimum spanning tree (MST). While the priority queue is not empty, we choose the edge between two nodes with the smallest weight and add it to MST. Then, we find all of the connected nodes of the selected end node, whose neighbors are then added to the heap. The algorithm searches until all of the nodes of the adjacency matrix have been visited, and the MST is complete.

### Unit testing 
- In _**check_mst**_, we ensure that the MST is properly implemented. Besides the tests that were already added which check the MST has the corrected expected weight, we check that the number of edges in the MST equals _n-1_ and that the MST has the same dimensions as the initial adjacency matrix (they should both be NxN matrices).
- In _**test_mst_student**_, we check that the _**contruct_mst**_ properly handles disconnected graphs, as well as empty graphs. We show that errors are raised when the adjacency matrix input is empty and when it contains a disconnected node. 


## Tasks

### Coding

* [x] Complete the `construct_mst` method found in `mst/graph.py`. All necessary modules have already been imported. You should not rely on any other dependencies (e.g. networkx). 

### Development

* [x] Add more assertions to the `check_mst` function in `test/test_mst.py`.
* [x] Write at least one more unit test (in the `test_mst.py` file) for your `construct_mst` implementation. (Two unit tests have already been provided: the first operates on a small graph of four nodes, and the second on a larger graph of 140 single cells, projected onto a lower dimensional subspace.)
* [x] Make your package `pip` installable. (Refer to previous assignments for more in-depth information.)
* [x] Automate testing with `pytest` and GitHub Actions, and add a status badge to this README file. (Refer to previous assignments for more in-depth information.)

## Getting started

Fork this repository to your own GitHub account. Work on the codebase locally and commit changes to your forked repository. 

You will need the following packages:

- [numpy](https://numpy.org/)
- [scikit-learn](https://scikit-learn.org/)
- [pytest](https://docs.pytest.org/en/7.2.x/)

We also strongly recommend you use the built-in [heapq](https://docs.python.org/3/library/heapq.html) module.

## Completing the assignment

Push your code to GitHub with passing unit tests, and submit a link to your repository through this [google form link](https://forms.gle/guyuWE6hsTiz34WTA)

## Grading

### Code (6 points)

* Minimum spanning tree construction works correctly (6)
    * Correct implementation of Prim's algorithm (4)
    * Produces expected output on small graph (1) 
    * Produces expected output on single cell data (1) 

### Unit tests (3 points)

* Complete function "check_mst" (1)
* Write at least two unit tests for MST construction (2)

### Style (1 points)

* Readable code with clear comments and method descriptions (1)

### Extra credit (0.5)

* Github actions/workflow (0.5)
