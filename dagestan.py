import gym
import math as Math
import numpy as np
import time
env = gym.make('Marvin-v0')

fittest = 0
fittest_actions = np.empty([420, 4])
population = []



class Marvin:
    
    def __init__(self, population_size, genome_size, mut_chance=0.1):
        self.actions = np.empty([genome_size, 4])
        self.fitness = 0
        self.done = False
        self.population_size = population_size
        self.mut_chance = mut_chance
        self.fill_random_actions()


    def fill_random_actions(self):
        for i in range(self.population_size):
            self.actions[i] = env.action_space.sample()

    def walk(self):
        while(True and self.done == False):
            for action in self.actions:
                if self.done == False:
                    observation_n, reward_n, done_n, info = env.step(action)
                    env.render()
                    self.fitness += reward_n
                    self.done = done_n
                    if self.fitness < -10:
                        self.done = True
        self.fitness = (self.fitness - -120) / (300 - -120)


class Population:

    def __init__(self, size, genome_size, population=False):
        if population:
            self.population = population
        else:
            self.population = []
        self.fittest = 0
        self.genome_size = genome_size
        self.size = size
        print("New population created", self.size, self.genome_size)

    def create(self):
        for i in range(self.size):
            population.append(Marvin(self.size, self.genome_size))

    def compete(self):
        for i in range(self.size):
            env.reset()
            (population[i]).walk()
            print(population[i].fitness)
        if (population[i].fitness > fittest):
            self.fittest = population[i].fitness
            fittest_actions = population[i].actions
        print("I was the fittest, my fitness is ", self.fittest)

class Evolution:

    def __init__(self, p_size, g_size, mut_chance=0.1):
        self.population_size = p_size
        #self.current_population = Population
        self.genome_size = g_size
        self.mutation_chance = mut_chance

    def soup(self):
        self.current_population = Population(self.population_size, self.genome_size) 
        self.current_population.create()
        self.current_population.compete()


life = Evolution(100, 400)        
life.soup()





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
