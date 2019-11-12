import gym
import numpy as np
env = gym.make('Marvin-v0')


observation_n = env.reset()



actions = np.empty([100, 4])

for i in range(100):
    actions[i] = env.action_space.sample()

print (actions[0])
for action in actions:
    env.step(action) # take a random action
    env.render()
env.close()
