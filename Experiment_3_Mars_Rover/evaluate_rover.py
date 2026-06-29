from stable_baselines3 import PPO
from mars_rover_improved import MarsRoverEnv
import time

env = MarsRoverEnv()

model = PPO.load(
    "models/ppo_rover_improved"
)

obs, info = env.reset()

for step in range(20):

    action, _ = model.predict(
        obs,
        deterministic=True
    )

    obs, reward, terminated, truncated, info = env.step(action)

    print("\n-------------------------")
    print(f"Step: {step + 1}")
    print(f"Action: {action}")
    print(f"Reward: {reward}")

    env.render()

    time.sleep(1)

    if terminated or truncated:

        print("\nEpisode Finished!")

        if reward == 100:
            print("Goal Reached! 🚀")

        elif reward == -20:
            print("Hit Obstacle! 💥")

        break

env.close()