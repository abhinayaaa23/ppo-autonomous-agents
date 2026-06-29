# PPO Autonomous Agents

This repository contains a few reinforcement learning experiments that I worked on to understand how agents learn through interaction with an environment using rewards and penalties.

The project was implemented using Gymnasium and Stable-Baselines3 with the PPO (Proximal Policy Optimisation) algorithm.

## Experiments

### 1. CartPole

The goal of the agent is to keep a pole balanced on a moving cart for as long as possible.

**State Space**

* Cart Position
* Cart Velocity
* Pole Angle
* Pole Angular Velocity

**Actions**

* Move Left
* Move Right

**Reward**

* +1 for every timestep the pole remains balanced



### 2. Car Racing

In this environment, the agent learns to drive a car around a race track using image observations.

**State Space**

* 96 × 96 RGB image

**Actions**

* Steering
* Acceleration
* Brake

**Reward**

* Based on progress around the track

Due to limited training time, the agent was able to learn some movement patterns but still struggled with staying on the track consistently.



### 3. Mars Rover Navigation

A simple custom grid-world environment was created to study the effect of reward design on agent behaviour.

The rover must reach a target position while avoiding obstacles.

**Actions**

* Up
* Down
* Left
* Right

#### Initial Reward Design

* Step penalty: -1
* Goal reward: +100
* Obstacle penalty: -20

The rover often repeated actions and got stuck near boundaries.

#### Improved Reward Design

A distance-to-goal reward was added so that the rover receives positive feedback when moving closer to the destination.

This resulted in noticeably different behaviour and highlighted the importance of reward shaping in reinforcement learning.



## Tools Used

* Python
* Gymnasium
* Stable-Baselines3
* PPO
* NumPy
* PyTorch


## Learning Outcomes

Through these experiments, I gained hands-on experience with:

* State and action spaces
* Reward functions
* PPO training
* Policy learning
* Environment design
* Reward engineering

The Mars Rover experiment was particularly useful in understanding how small changes in the reward function can significantly influence an agent's behaviour.
