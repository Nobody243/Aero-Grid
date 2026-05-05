"""
Reinforcement Learning Q-Learning Drone Navigation Agent
"""
import numpy as np
import random

ACTIONS = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

class QLearningAgent:
    def __init__(self, grid_size=40, alpha=0.1, gamma=0.95, epsilon=0.2):
        self.grid_size = grid_size
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}


    def get_state_key(self, pos, target):
        return (pos[0], pos[1], target[0], target[1])

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, len(ACTIONS)-1)
        q_vals = [self.q_table.get((state, a), 0.0) for a in range(len(ACTIONS))]
        return int(np.argmax(q_vals))
