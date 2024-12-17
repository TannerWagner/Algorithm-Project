#@AUTHOR Tanner Wagner
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return top

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)

    def _bubble_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

    def is_empty(self):
        return len(self.heap) == 0

class AStar:
    def __init__(self, grid, start, items):
        self.grid = grid
        self.start = start
        self.items = items
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.open_list = MinHeap()
        self.closed_set = set()
        self.parents = {}
        self.g_scores = {}
        self.path = []
        self.nodes_explored = 0

    def heuristic(self, current, target):
        return abs(current[0] - target[0]) + abs(current[1] - target[1])

    def neighbors(self, node):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            x, y = node[0] + dx, node[1] + dy
            if 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] != 1:
                neighbors.append((x, y))
        return neighbors

    def reconstruct_path(self, current):
        path = [current]
        while current != self.start:
            current = self.parents[current]
            path.append(current)
        path.reverse()
        return path

    def a_star_search(self, robot=False): #added robot flag
        self.g_scores[self.start] = 0
        self.open_list.push((0, self.start))
        full_path = []

        while not self.open_list.is_empty():
            _, current = self.open_list.pop()
            self.nodes_explored += 1 # Increment nodes explored
            
            if current in self.items:
                self.items.remove(current)

                segment_path = self.reconstruct_path(current)

                overlap_length = 0
                max_overlap = min(len(full_path), len(segment_path))
                for i in range(max_overlap, 0, -1):
                    if full_path[-i:] == segment_path[:i]:
                        overlap_length = i
                        break

                segment_path = segment_path[overlap_length:]
                full_path.extend(segment_path)

                self.start = current
                self.parents = {}
                self.g_scores = {current: 0}
                self.open_list = MinHeap()
                self.open_list.push((0, self.start))
                self.closed_set = set()

                if not self.items:
                    if robot:
                        reverse_path = full_path[::-1]
                        full_path.extend(reverse_path[1:])
                        self.nodes_explored += len(reverse_path)
                    return full_path, len(full_path) - 1, self.nodes_explored

            self.closed_set.add(current)

            for neighbor in self.neighbors(current):
                if neighbor in self.closed_set:
                    continue

                tentative_g_score = self.g_scores.get(current, float('inf')) + 1

                if neighbor not in self.g_scores or tentative_g_score < self.g_scores[neighbor]:
                    self.parents[neighbor] = current
                    self.g_scores[neighbor] = tentative_g_score

                    if self.items:
                        nearest_item = min(self.items, key=lambda item: self.heuristic(neighbor, item))
                        f_score = tentative_g_score + self.heuristic(neighbor, nearest_item)
                    else:
                        f_score = tentative_g_score

                    self.open_list.push((f_score, neighbor))

        print("No path found!")
        return [], float('inf'), self.nodes_explored # Return
