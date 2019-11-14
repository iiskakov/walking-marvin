import gym
import math as Math
import numpy as np
import time
import random
env = gym.make('Marvin-v0')



class Marvin:
    
    def __init__(self, genome_size, mut_chance=0.1, genes = None):
        self.actions = np.empty([genome_size, 4])
        self.fitness = 0
        self.done = False
        self.genome_size = genome_size
        self.mut_chance = mut_chance
        if genes is None:
            self.fill_random_actions()
        else:
            self.actions = genes


    def fill_random_actions(self):
        for i in range(self.genome_size):
            self.actions[i] = env.action_space.sample()

    def walk(self):
        self.fitness = 0
        actions = 0
        while(True and self.done == False):
            for action in self.actions:
                if self.done == False:
                    actions += 1
                    observation_n, reward_n, done_n, info = env.step(action)
                    env.render()
                    #time.sleep(0.01)
                    self.fitness += reward_n
                    self.done = done_n
                    if actions > 1200 and self.fitness < -5:
                    #if self.fitness < -10:
                        self.fitness = -200
                        self.done = True
        ##Normalize??
        self.fitness = 1000 * (self.fitness - -200) / (300 - -200)


class Population:

    def __init__(self, size, genome_size, population=False):
        if population:
            self.population = population
        else:
            self.population = []
        self.genome_size = genome_size
        self.size = size
        self.next_generation = []
        self.mating_pool = [] 
        print("New population created", self.size, self.genome_size)

    def create(self):
        for i in range(self.size):
            self.population.append(Marvin(self.genome_size))
        ##Testing crossover here
        #self.crossover(self.population[2].actions, self.population[1].actions)

    def compete(self):
        self.next_generation = []
        for i in range(self.size):
            self.population[i].walk()
            env.reset()
            if (round(self.population[i].fitness) in range(random.randint(0, 400))):
                    print("I might have sex tonight!")
                    self.mating_pool.append(self.population[i])
            print(self.population[i].fitness)

    def crossover(self, parent_one, parent_two):
        middle = self.genome_size // 2
        child_genes = np.empty([self.genome_size, 4])  
        child_genes[0:middle] = parent_one[0:middle] 
        child_genes[middle:-1] = parent_two[middle:-1] 
        if random.randint(0, 100) == 42:
            print("X-RAY JUST HIT ME, MUTATION IS HAPPENING")
            for i in range(random.randint(0, self.genome_size//8)):
                child_genes[random.randint(0, self.genome_size - 1)] = env.action_space.sample()
        child = Marvin(self.genome_size, genes=child_genes)
        return child

    def sex(self):
        for i in range(self.size):
            self.next_generation.append(self.crossover(self.mating_pool[random.randint(0, len(self.mating_pool) - 1)].actions, self.mating_pool[random.randint(0, len(self.mating_pool) - 1)].actions))

        self.population = self.next_generation


class Evolution:

    def __init__(self, p_size, g_size, mut_chance=0.1):
        self.population_size = p_size
        self.genome_size = g_size
        self.mutation_chance = mut_chance

    def soup(self):
        gen = 0
        self.current_population = Population(self.population_size, self.genome_size) 
        self.current_population.create()
        while(True):
            print("Generation", gen)
            self.current_population.compete()
            self.current_population.sex()
            gen += 1

      



life = Evolution(10, 400)        
life.soup()



env.close()
