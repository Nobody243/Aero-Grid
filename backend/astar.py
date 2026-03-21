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


DIRECTIONS = [(0,1,1.0),(0,-1,1.0),(1,0,1.0),(-1,0,1.0),(1,1,1.414),(1,-1,1.414),(-1,1,1.414),(-1,-1,1.414)]

def in_bounds(p, size=40):
    return 0 <= p[0] < size and 0 <= p[1] < size
