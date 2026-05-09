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


    def update_q(self, state, action, reward, next_state):
        current_q = self.q_table.get((state, action), 0.0)
        max_next_q = max([self.q_table.get((next_state, a), 0.0) for a in range(len(ACTIONS))])
        td_target = reward + self.gamma * max_next_q
        self.q_table[(state, action)] = current_q + self.alpha * (td_target - current_q)


# Rebalanced reward shaping: step -0.5, obstacle -150.0, goal +300.0, progress reward +2.0


# Boundary bounce and strict out-of-bounds wall penalty


    def save(self, filepath):
        import pickle
        with open(filepath, "wb") as f:
            pickle.dump(self.q_table, f)

    def load(self, filepath):
        import pickle
        with open(filepath, "rb") as f:
            self.q_table = pickle.load(f)
