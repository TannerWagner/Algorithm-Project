import time
import matplotlib.pyplot as plt
import numpy as np
from dfs import DFS
from bfs import BFS
from FloydWarshall import FloydWarshall, matrixToGraph
from Astar import MinHeap
from Astar import AStar
from Dijkstras import dijkstras

class Main:
    def __init__(self):
        pass

    def plot_theoretical_complexities(self):
        n = np.linspace(1, 100, 500)
        bfs_dfs = n
        floyd_warshall = n ** 3
        astar_typical = n
        astar_worst = np.power(2, n / 10)
        dijkstra_sparse = n * np.log(n)
        dijkstra_dense = n ** 2

        plt.figure(figsize=(10, 6))
        plt.loglog(n, bfs_dfs, label="BFS/DFS: O(n)", color="blue", linewidth=2, marker="o", markersize=4)
        plt.loglog(n, floyd_warshall, label="Floyd-Warshall: O(n^3)", color="red", linewidth=2, linestyle="-.")
        plt.loglog(n, astar_typical, label="A*: O(n) (Typical Case)", color="green", linewidth=2, linestyle=":")
        plt.loglog(n, astar_worst, label="A*: O(b^d) (Worst Case)", color="purple", linewidth=2, linestyle="--")
        plt.loglog(n, dijkstra_sparse, label="Dijkstra (Sparse Graph): O(V log V)", color="orange", linewidth=2, linestyle=":")
        plt.loglog(n, dijkstra_dense, label="Dijkstra (Dense Graph): O(V²)", color="brown", linewidth=2, linestyle="--")

        plt.title("Theoretical Time Complexity of Algorithms")
        plt.xlabel("Input Size (n)")
        plt.ylabel("Time Complexity (Arbitrary Units)")
        plt.legend()
        plt.grid(True, which="both", linestyle="--", linewidth=0.5)
        plt.savefig("theoretical_complexities.png")
        plt.show()
        
    def execute(self):
        test_cases = [
            {
                "description": "Case with no obstacles and several items",
                "grid": [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                ],
                "start": (0, 0),
                "items": [(4, 4), (2, 2), (3, 3)],
            },
            {
                "description": "Case with multiple obstacles and fewer items",
                "grid": [
                    [0, 1, 0, 0, 0],
                    [0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0],
                    [1, 1, 0, 0, 0],
                ],
                "start": (0, 0),
                "items": [(4, 4)],
            },
            {
                "description": "Case with a complex grid layout requiring different paths to optimize",
                "grid": [
                    [0, 0, 1, 1, 1],
                    [1, 0, 1, 0, 0],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 0, 1],
                    [0, 0, 0, 0, 0],
                ],
                "start": (0, 0),
                "items": [(4, 4), (2, 3)],
            },
            {
                "description": "Case with only one item in a corner of the grid",
                "grid": [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0],
                    [0, 0, 0, 0, 0],
                ],
                "start": (0, 0),
                "items": [(4, 4)],
            },
        ]

        # Comparative Analysis:
        bfs_times, dfs_times, fw_times, astar_times, d_times = [], [], [], [], []
        bfs_memory, dfs_memory, fw_memory, astar_memory, d_memory = [], [], [], [], [] 

        for case in test_cases:
            print(f"\n--- Test Case: {case['description']} ---")
            grid = case["grid"]
            start = case["start"]
            items = case["items"]
            
            # BFS Algorithm--Jennifer Diaz
            '''
            print("\n--- BFS Algorithm ---")
            bfs_solver = BFS(grid, start, items[:])
            bfs_path, bfs_length = bfs_solver.find_path(robot=False)
            print("BFS Path:", bfs_path)
            print("BFS Path Length:", bfs_length)
            '''
            print("\n--- BFS Algorithm ---")
            start_time = time.time()
            bfs_path, bfs_length, bfs_nodes = BFS(grid, start, items[:]).find_path(robot=False)
            end_time = time.time()
            bfs_times.append(end_time - start_time)
            bfs_memory.append(bfs_nodes)
            print("BFS Path:", bfs_path)
            print("BFS Path Length:", bfs_length)
            print("BFS Nodes Explored:", bfs_nodes)

            '''
            print("\n--- BFS Algorithm: Robot Return to Start ---")
            bfs_solver = BFS(grid, start, items[:])
            bfs_path, bfs_length = bfs_solver.find_path(robot=True)
            print("BFS Path:", bfs_path)
            print("BFS Path Length:", bfs_length)
            '''

            print("\n--- BFS Algorithm: Robot Return to Start ---")
            start_time = time.time()
            bfs_path, bfs_length, bfs_nodes = BFS(grid, start, items[:]).find_path(robot=True)
            end_time = time.time()
            bfs_times.append(end_time - start_time)
            bfs_memory.append(bfs_nodes)
            print("BFS Path:", bfs_path)
            print("BFS Path Length:", bfs_length)
            print("BFS Nodes Explored:", bfs_nodes)

            # DFS Algorithm--Jennifer Diaz
            '''
            print("\n--- DFS Algorithm ---")
            dfs_solver = DFS(grid, start, items[:])
            dfs_path, dfs_length = dfs_solver.find_path(robot=False)
            print("DFS Path:", dfs_path)
            print("DFS Path Length:", dfs_length)
            '''
            print("\n--- DFS Algorithm ---")
            start_time = time.time()
            dfs_path, dfs_length, dfs_nodes = DFS(grid, start, items[:]).find_path(robot=False)
            end_time = time.time()
            dfs_times.append(end_time - start_time)
            dfs_memory.append(dfs_nodes)
            print("DFS Path:", dfs_path)
            print("DFS Path Length:", dfs_length)
            print("DFS Nodes Explored:", dfs_nodes)

            '''
            print("\n--- DFS Algorithm: Robot Return to Start ---")
            dfs_solver = DFS(grid, start, items[:])
            dfs_path, dfs_length = dfs_solver.find_path(robot=True)
            print("DFS Path:", dfs_path)
            print("DFS Path Length:", dfs_length)
            '''
            print("\n--- DFS Algorithm: Robot Return to Start ---")
            start_time = time.time()
            dfs_path, dfs_length, dfs_nodes = DFS(grid, start, items[:]).find_path(robot=True)
            end_time = time.time()
            dfs_times.append(end_time - start_time)
            dfs_memory.append(dfs_nodes)
            print("DFS Path:", dfs_path)
            print("DFS Path Length:", dfs_length)
            print("DFS Nodes Explored:", dfs_nodes)
            
            # Floyd-Warshall Algorithm--Jubilation Megill
            '''
            print("\n--- Floyd_Warshall Algorithm ---")
            vertices, adj = matrixToGraph(grid)#Conversion step (Matrix -> Graph)
            FWPath, FWLength = FloydWarshall(start,vertices,adj,items[:]) # Actual algorithm
            print("Floyd-Warshall Result:", FWPath)
            print("Floyd-Warshall Path Length:", FWLength)
            '''
            print("\n--- Floyd_Warshall Algorithm ---")
            vertices, adj = matrixToGraph(grid) # convert matrix to graph
            start_time = time.time()
            FWPath, FWLength, FWNodes = FloydWarshall(start, vertices, adj, items[:])
            end_time = time.time()
            fw_times.append(end_time - start_time)
            fw_memory.append(FWNodes)
            print("Floyd-Warshall Result:", FWPath)
            print("Floyd-Warshall Path Length:", FWLength)
            print("Floyd-Warshall Nodes Explored:", FWNodes)

            print("\n--- Floyd_Warshall Algorithm (Returning to start)---")
            vertices, adj = matrixToGraph(grid) # convert matrix to graph
            start_time = time.time()
            FWPath, FWLength, FWNodes = FloydWarshall(start, vertices, adj, items[:],True)
            end_time = time.time()
            fw_times.append(end_time - start_time)
            fw_memory.append(FWNodes)
            print("Floyd-Warshall Result:", FWPath)
            print("Floyd-Warshall Path Length:", FWLength)
            print("Floyd-Warshall Nodes Explored:", FWNodes)

            # Astar Algorithm--Tanner Wagner
            '''
            print("\n--- Astar Algorithm ---")
            astar_solver = AStar(grid, start, items[:])
            astar_path = astar_solver.a_star_search(robot=False)
            astar_length = len(astar_path) - 1
            print("Astar Path:", astar_path)
            print("Astar Path Length:", astar_length)
            '''
            print("\n--- Astar Algorithm ---")
            start_time = time.time()
            astar_path, astar_length, astar_nodes = AStar(grid, start, items[:]).a_star_search(robot=False)
            end_time = time.time()
            astar_times.append(end_time - start_time)
            astar_memory.append(astar_nodes)
            print("Astar Path:", astar_path)
            print("Astar Path Length:", astar_length)
            print("Astar Nodes Explored:", astar_nodes)

            '''
            print("\n--- Astar Algorithm:Robot Return to Start ---")
            astar_solver = AStar(grid, start, items[:])
            astar_path = astar_solver.a_star_search(robot=True)
            astar_length = len(astar_path) - 1
            print("Astar Path:", astar_path)
            print("Astar Path Length:", astar_length)
            '''
            print("\n--- Astar Algorithm: Robot Return to Start ---")
            start_time = time.time()
            astar_path, astar_length, astar_nodes = AStar(grid, start, items[:]).a_star_search(robot=True)
            end_time = time.time()
            astar_times.append(end_time - start_time)
            astar_memory.append(astar_nodes)
            print("Astar Path:", astar_path)
            print("Astar Path Length:", astar_length)
            print("Astar Nodes Explored:", astar_nodes)

            # Dijkstra's Algorithm--Odysseus Valdez
            print("\n--- Dijkstra's Algorithm ---")
            start_time = time.time()
            d_path, d_length, d_nodes = dijkstras(grid, start, items[:]).dijkstras_search(False)
            end_time = time.time()
            d_times.append(end_time - start_time)
            d_memory.append(d_nodes)
            print("Dijkstra's Path:", d_path)
            print("Dijkstra's Path Length:", d_length)
            print("Dijkstra's Nodes Explored:", d_nodes)

            print("\n--- Dijkstra's Algorithm: Robot Return to Start ---")
            start_time = time.time()
            d_path, d_length, d_nodes = dijkstras(grid, start, items[:]).dijkstras_search(True)
            end_time = time.time()
            d_times.append(end_time - start_time)
            d_memory.append(d_nodes)
            print("Dijkstra's Path:", d_path)
            print("Dijkstra's Path Length:", d_length)
            print("Dijkstra's Nodes Explored:", d_nodes)
            

        # Convert lists to numpy arrays:
        bfs_times = np.array(bfs_times)
        dfs_times = np.array(dfs_times)
        fw_times = np.array(fw_times)
        astar_times = np.array(astar_times)
        d_times = np.array(d_times)

        bfs_memory = np.array(bfs_memory)
        dfs_memory = np.array(dfs_memory)
        fw_memory = np.array(fw_memory)
        astar_memory = np.array(astar_memory)
        d_memory = np.array(d_memory)

        # Averages:
        algorithms = ["BFS", "DFS", "FloydWarshall", "AStar", "Dijkstra"]
        avg_times = [bfs_times.mean(), dfs_times.mean(), fw_times.mean(), astar_times.mean(), d_times.mean()]
        avg_memory = [bfs_memory.mean(), dfs_memory.mean(), fw_memory.mean(), astar_memory.mean(), d_memory.mean()]

        # Averages in terminal:
        print("\n--- Comparative Analysis Results ---")
        for i, alg in enumerate(algorithms):
            print(f"{alg}: Average Execution Time = {avg_times[i]:.4f}s, Average Nodes Explored = {avg_memory[i]:.2f}")

        # Plot execution time:
        plt.figure()
        plt.bar(algorithms, avg_times, color=["blue", "green", "red", "purple", "pink"])
        plt.title("Average Execution Time Across All Test Cases")
        plt.xlabel("Algorithm")
        plt.ylabel("Time (seconds)")
        plt.savefig("average_execution_time.png")
        plt.show()

        # Plot memory usage (nodes explored) with a logarithmic scale
        plt.figure()
        plt.bar(algorithms, avg_memory, color=["blue", "green", "red", "purple", "pink"])
        plt.title("Average Nodes Explored Across All Test Cases (Log Scale)")
        plt.xlabel("Algorithm")
        plt.ylabel("Nodes Explored (Log Scale)")
        plt.yscale("log")
        plt.savefig("average_nodes_explored_log.png")
        plt.show()

        

        self.plot_theoretical_complexities()

if __name__ == "__main__":
    main = Main()
    main.execute()
