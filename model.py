"""
Sutton and Barto from Scratch 1: Bandits and Dynamic Programming

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - create_bandit_testbed (not yet solved)
# TODO: implement

# Step 2 - pull_arm (not yet solved)
# TODO: implement

# Step 3 - sample_average_update (not yet solved)
# TODO: implement

# Step 4 - epsilon_greedy_action (not yet solved)
# TODO: implement

# Step 5 - run_bandit_episode (not yet solved)
# TODO: implement

# Step 6 - track_rewards_and_optimal_actions (not yet solved)
# TODO: implement

# Step 7 - average_bandit_curves (not yet solved)
# TODO: implement

# Step 8 - apply_random_walk_drift (not yet solved)
# TODO: implement

# Step 9 - constant_step_size_update (not yet solved)
# TODO: implement

# Step 10 - optimistic_initialization (not yet solved)
# TODO: implement

# Step 11 - ucb_action_select (not yet solved)
# TODO: implement

# Step 12 - gradient_bandit_update (not yet solved)
# TODO: implement

# Step 13 - bandit_parameter_study (not yet solved)
# TODO: implement

# Step 14 - build_gridworld_mdp
from typing import Dict, List, Tuple, Any
def build_gridworld_mdp() -> Dict[str, Any]:
    # TODO: Build the book's small gridworld MDP as a dynamics table...
    n_states : int = 16
    grid_shape : Tuple[int,int]= (4,4)
    n_actions : int = 4
    P: List[List[List[Tuple[float, int, float]]]] = [
        [[] for _ in range(n_actions)] for _ in range(n_states)
    ]

    def next_state(row: int, col: int, shape: tuple[int, int], action: int) -> tuple[int, int]:
        if action == 0:
            return max(0, row - 1), col
        if action == 1:
            return row, min(shape[1] -1, col + 1)
        if action == 2:
            return min(shape[0] - 1, row + 1), col
        if action == 3:
            return row, max(0, col - 1)
        raise ValueError("Wrong action")

    for s in range(n_states):
        for a in range(n_actions):
            if s == 0 or s == 15:
                P[s][a] = [(1.0, s, 0.0)]
            else:
                row, col = divmod(s, grid_shape[0])
                row, col = next_state(row, col, grid_shape, a)
                next_s = row * grid_shape[0] + col
                P[s][a] = [(1.0, next_s, -1.0)]

    return {'n_states': n_states, 'n_actions': n_actions, 'P': P}

# Step 15 - iterative_policy_evaluation (not yet solved)
# TODO: implement

# Step 16 - greedy_policy_improvement (not yet solved)
# TODO: implement

# Step 17 - policy_iteration (not yet solved)
# TODO: implement

# Step 18 - value_iteration (not yet solved)
# TODO: implement

# Step 19 - build_gambler_mdp (not yet solved)
# TODO: implement

# Step 20 - gambler_value_iteration (not yet solved)
# TODO: implement

# Step 21 - extract_optimal_stakes (not yet solved)
# TODO: implement

