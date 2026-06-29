import gymnasium as gym
from gymnasium import spaces
import numpy as np

class MarsRoverEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.grid_size = 4

        self.action_space = spaces.Discrete(4)

        self.observation_space = spaces.Box(
            low=0,
            high=self.grid_size - 1,
            shape=(2,),
            dtype=np.int32
        )

        self.start = (0, 0)
        self.goal = (3, 3)

        self.obstacles = [
            (1, 1),
            (2, 2)
        ]

        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.position = list(self.start)

        observation = np.array(
            self.position,
            dtype=np.int32
        )

        return observation, {}

    def step(self, action):

        old_row, old_col = self.position

        row, col = self.position

        if action == 0:
            row -= 1

        elif action == 1:
            row += 1

        elif action == 2:
            col -= 1

        elif action == 3:
            col += 1

        row = np.clip(row, 0, self.grid_size - 1)
        col = np.clip(col, 0, self.grid_size - 1)

        self.position = [row, col]

        new_row, new_col = self.position

        old_distance = abs(old_row - 3) + abs(old_col - 3)
        new_distance = abs(new_row - 3) + abs(new_col - 3)

        reward = old_distance - new_distance

        terminated = False

        if (row, col) in self.obstacles:
            reward = -20
            terminated = True

        elif (row, col) == self.goal:
            reward = 100
            terminated = True

        observation = np.array(
            self.position,
            dtype=np.int32
        )

        return observation, reward, terminated, False, {}

    def render(self):

        grid = np.full(
            (self.grid_size, self.grid_size),
            ".",
            dtype=str
        )

        for r, c in self.obstacles:
            grid[r, c] = "X"

        grid[self.goal] = "G"

        r, c = self.position
        grid[r, c] = "R"

        print("\n")
        print(grid)