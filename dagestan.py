import gym
import math as Math
import numpy as np
import time
env = gym.make('Marvin-v0')

fittest = 0
fittest_actions = np.empty([420, 4])
population = []


class Marvin:
    
    def __init__(self):
        self.actions = np.empty([420, 4])
        self.fitness = 0
        self.done = False


    def random_actions(self):
        for i in range(420):
            self.actions[i] = env.action_space.sample()

    def walk(self):
        observation_n = env.reset()
        for action in self.actions:
            if self.done == False:
                observation_n, reward_n, done_n, info = env.step(action)
                env.render()
                self.fitness += reward_n
                self.done = done_n
                if self.fitness < -10:
                    self.done = True
        self.fitness = (self.fitness - -120) / (300 - -120)
        print(self.fitness)

class Population:

    def __init__(self, population=False):
        if population:
            self.population = population
        else:
            self.population = []
        fittest = 0

    def create(self):
        for i in range(100):
            population.append(Marvin())

    def compete(self):
        for i in range(100):
            (population[i]).random_actions()
            (population[i]).walk()
        print(population[i].fitness)
        if (population[i].fitness > fittest):
            self.fittest = population[i].fitness
            fittest_actions = population[i].actions
        print("I was the fittest, my fitness is ", self.fittest)

        
first = Population()

first.create()
first.compete()




print("And here are my moves")
while(True):
    observation_n = env.reset()
    done_n = False
    while (True):
        for action in fittest_actions:
            if done_n == False:
                observation_n, reward_n, done_n, info = env.step(action) # take a random action
                env.render()
            #time.sleep(0.01)
#print(fittest_actions)
env.close()
