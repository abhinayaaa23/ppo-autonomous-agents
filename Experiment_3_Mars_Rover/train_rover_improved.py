from stable_baselines3 import PPO
from mars_rover_improved import MarsRoverEnv

env = MarsRoverEnv()

model = PPO(
    "MlpPolicy",
    env,
    verbose=1
)

model.learn(
    total_timesteps=10000
)

model.save(
    "models/ppo_rover_improved"
)

print("Improved Reward Training Complete!")