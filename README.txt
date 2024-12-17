# Implementation and Comparative Analysis of Pathfinding Algorithms

## Overview
This script provides a framework to evaluate and compare the performance of various pathfinding algorithms on a grid-based environment with obstacles and items.

- **Pathfinding Algorithms**:
  - **A\***
  - **BFS (Breadth-First Search)**
  - **DFS (Depth-First Search)**
  - **Dijkstra**
  - **Floyd-Warshall**
- **Test Cases**
- **Comparison Graphs**

## Requirements
### Prerequisites
- Python 3.8+
- Required Libraries:
  - `matplotlib`:
    - Run the script: `pip install matplotlib`
  - `numpy`:
    - Run the script: `pip install numpy`
- Required algorithm modules:
  - `dfs.py`
  - `bfs.py`
  - `FloydWarshall.py`
  - `Astar.py`
  - `Dijkstras.py`

### Installation & Usage 
1. Option 1 Clone the repository: `https://lobogit.unm.edu/twagner1003/cs-361-final-project.git`
2. Option 2 Download all the required algorithm modules plus `main.py`
   - Make sure all required algorithm modules are in the same directory as the `main.py` class.
3. Run the script: `python main.py`

### Code Structure 
- Main Class:
  - Initializes and executes the test cases.
  - Calls each pathfinding algorithm and displays results for each test case.
- Test Cases:
  - Case with no obstacles and several items. 
  - Case with multiple obstacles and fewer items. 
  - Case with a complex grid layout requiring different paths to optimize. 
  - Case with only one item in a corner of the grid.

## Authors
Tanner Wagner, Jennifer Diaz, Odysseus Valdez, and Jubilation Megill.


