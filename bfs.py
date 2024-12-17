#@AUTHOR Jennifer Nevares-Diaz
class BFS:
    def __init__(self, grid, start, items):
        self.grid = grid
        self.start = start
        self.items = items
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.full_path = []
        self.debug = False

    def log_debug(self,message):
        if self.debug:
            print("[Debug: BFS] ", message)

    def neighbors(self, node):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            x, y = node[0] + dx, node[1] + dy
            if 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] != 1:
                neighbors.append((x, y))
        return neighbors

    def shortest_path(self, start, target):
        queue = [(start, [])]
        front = 0
        visited = set()
        visited.add(start)

        nodes_explored = 0 # Count how many nodes are processed--Tanner

        while front  < len(queue):
            current, path = queue[front]
            front +=1
            nodes_explored += 1 # Increment each time we pop from the queue--Tanner

            path = path + [current]

            if current == target:
                return path, nodes_explored # Return path and nodes explored--Tanner

            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor,path))
        return [], nodes_explored # Return empty if no path found along with nodes explored--Tanner

    def find_path(self, robot=False):
        current_position = self.start
        self.log_debug(f"Starting BFS from {self.start} to collect items: {self.items}")

        total_nodes_explored = 0 # Track total nodes across all calls--Tanner

        while self.items:
            closest_item = self.items.pop(0)
            self.log_debug(f"Finding path to item at {closest_item}")
            path_to_item, item_nodes  = self.shortest_path(current_position, closest_item) # Added item_nodes -- Tanner
            total_nodes_explored += item_nodes # Increment--Tanner

            if not path_to_item:
                self.log_debug(f"No path to item at {closest_item}")
                return "No path found", float('inf'), total_nodes_explored # Return--Tanner

            self.log_debug(f"Path to {closest_item}: {path_to_item}")
            self.full_path.extend(path_to_item)
            current_position = closest_item

        if not robot:
            return_path = self.full_path[::-1]
            ret_nodes = len(return_path)  # Added ret_nodes--Tanner
        else:
            return_path, ret_nodes = self.shortest_path(current_position, self.start) # Added ret_nodes--Tanner
            self.log_debug("Returning to starting position")
            total_nodes_explored += ret_nodes # Return--Tanner
        
            if return_path and robot:
                self.full_path.extend(return_path[1:])
                ret_nodes = len(return_path)

        self.log_debug(f"Final path: {self.full_path}")
        
        return self.full_path, len(self.full_path)-1, total_nodes_explored


