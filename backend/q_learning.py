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
