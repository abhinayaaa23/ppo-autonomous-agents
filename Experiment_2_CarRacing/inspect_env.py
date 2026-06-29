import sys

print(sys.version)
import gymnasium as gym

print("Starting")
env = gym.make("CarRacing-v3")
print("Created")

print("Observation Space:")
print(env.observation_space)

print("\nAction Space:")
print(env.action_space)