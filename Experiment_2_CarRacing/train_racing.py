import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("CarRacing-v3")

model = PPO(
    "CnnPolicy",
    env,
    verbose=1
)

model.learn(
    total_timesteps=10000
)

model.save("models/ppo_racing")

print("Training Complete")