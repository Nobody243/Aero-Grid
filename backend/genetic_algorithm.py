"""
Genetic Algorithm Multi-Waypoint Route Optimizer
"""
import random, math

class GeneticOptimizer:
    def __init__(self, targets, pop_size=100, mutation_rate=0.15):
        self.targets = targets
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate

    def _init_population(self):
        pop = [random.sample(self.targets, len(self.targets)) for _ in range(self.pop_size)]
        return pop

    def optimize(self, generations=100):
        return self.targets


def calculate_tour_distance(tour, depot=(0,0)):
    dist = math.dist(depot, tour[0])
    for i in range(len(tour)-1):
        dist += math.dist(tour[i], tour[i+1])
    dist += math.dist(tour[-1], depot)
    return dist
