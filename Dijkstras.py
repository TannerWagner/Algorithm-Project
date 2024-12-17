# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 13:27:53 2024

@author: odysseus.valdez
"""
from Astar import MinHeap

class dijkstras:
    
    def __init__(self, grid, start, items):
        self.grid = grid
        self.start = start
        self.items = items
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.open_nodes = MinHeap()
        self.closed_set = set()
        self.parents = {}
        self.shortest_distance = {}
        self.path = []

    def neighbors(self, node):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            x, y = node[0] + dx, node[1] + dy
            if 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] != 1:
                neighbors.append((x, y))
        return neighbors

    def reconstruct_path(self, node):
        path = [node]
        while node != self.start:
            node = self.parents[node]
            path.append(node)
        path.reverse()
        return path
    
    #Change to robot=True to return to start
    def dijkstras_search(self, robot):
        self.open_nodes.push((0, self.start))
        self.shortest_distance[self.start] = 0

        nodes_explored = 0 # Track nodes explored--Tanner
        
        while not self.open_nodes.is_empty():
            _, node = self.open_nodes.pop()
            nodes_explored += 1 # Increment--Tanner
            
            if node in self.items:
                self.items.remove(node)
                segment = self.reconstruct_path(node)
                self.path.extend(segment)
                
                if not self.items:
                    if robot:
                        return_to_start = self.reconstruct_path(self.start)
                        self.path.extend(return_to_start)
                    return self.path, len(self.path) - 1, nodes_explored  # Return Path, length, and nodes explored--Tanner
               

                self.start = node 
                self.parents = {}
                self.shortest_distance = {node: 0} 
                self.open_nodes = MinHeap()
                self.open_nodes.push((0, self.start)) 
                self.closed_set = set()

            
            self.closed_set.add(node)

            
            for neighbor in self.neighbors(node):
                if neighbor in self.closed_set:
                    continue
                temp_shortest_distance = self.shortest_distance.get(node, float('inf')) + 1 
                
                if temp_shortest_distance < self.shortest_distance.get(neighbor, float('inf')):
                    self.parents[neighbor] = node
                    self.shortest_distance[neighbor] = temp_shortest_distance
                    self.open_nodes.push((temp_shortest_distance, neighbor))

        return self.path, float('inf'), nodes_explored # Return--Tanner

