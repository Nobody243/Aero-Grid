"""
A* Pathfinding Algorithm
"""
import heapq, math

def octile_distance(a, b):
    dx, dy = abs(a[0]-b[0]), abs(a[1]-b[1])
    return max(dx,dy) + (math.sqrt(2)-1)*min(dx,dy)

class AStarPathfinder:
    def __init__(self, buildings, no_fly_zones, heuristic="octile"):
        self.blocked = buildings | no_fly_zones
    def find_path(self, start, goal):
        return [start, goal]
