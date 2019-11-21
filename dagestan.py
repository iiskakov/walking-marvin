import gym
import math as Math
import numpy as np
import time
import random
from statistics import median
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
                    if np.isnan(np.min(action)) == False:
                        observation_n, reward_n, done_n, info = env.step(action)
                        if life.gen > 800:
                            env.render()
                        self.fitness += reward_n
                        self.done = done_n
                        if self.fitness < -10:
                            self.fitness -= 100
                            self.done = True
                    #if actions > 300 and self.fitness < -20:
                    #    self.fitness = -200
                    #    self.done = True
        ##Normalize??
        self.fitness = ((1000 * (self.fitness - -300) / (600)) ** 1.4)
        

    def display(self):
        print("Display")
        actions = 0
        self.done = False
        while(actions < 5000):
            for action in self.actions:
                if actions > 500:
                    self.done == True
                if self.done == False:
                    actions += 1
                    if np.isnan(np.min(action)) == False:
                        observation_n, reward_n, done_n, info = env.step(action)
                        env.render()
                        self.done = done_n
                actions += 1

        env.reset()




class Population:

    def __init__(self, size, genome_size, mating_pool, population=False):
        if population:
            self.population = population
            print("Population init with copy")
        else:
            self.population = []
            print("Population init from sctratch")
        self.genome_size = genome_size
        self.size = size
        self.next_generation = []
        self.mating_pool = mating_pool

    def create(self):
        for i in range(self.size):
            self.population.append(Marvin(self.genome_size))
        print("New population created", self.size, self.genome_size)

        ##Testing crossover here
        #for i in range(3):
        #    new = self.crossover(self.population[2].actions, self.population[1].actions)
        #    print("Parent 1", self.population[2].actions)
        #    print("Parent 2", self.population[1].actions)
        #    print("Child", new.actions)

    def compete(self):
        self.next_generation = []
        for i in range(self.size):
            self.population[i].walk()
            env.reset()
        print("Before sort")
        sorted_population =  sorted(self.population, key=lambda marvin: marvin.fitness, reverse=True)
        print("Sorted len = ", len(sorted_population))
        chance = 100
        median_fit = median(marvin.fitness for marvin in self.population)
        av_fit = sum(marvin.fitness for marvin in self.population)/float(len(self.population))
        max_fit = sorted_population[0].fitness
        #print("Average:", av_fit)
        #for i in sorted_population:
        #    print(i.actions)
        #print(sorted_population[0].actions)
        print("Median:", median_fit)
        print("Max fit:", max_fit)
        if max_fit > 12000:
            print(sorted_population[0].actions)
            sorted_population[0].display()
            sorted_population[0].display()
            sorted_population[0].display()
        for i in range(len(sorted_population) // 50):
            self.mating_pool.append(sorted_population[i])
            #if sorted_population[i].fitness > median_fit * 2:
            #    for _ in range(10):
            #        self.mating_pool.append(sorted_population[i])
        #for mar in sorted_population:
        #    if mar.fitness > median_fit:
        #        self.mating_pool.append(mar)
        #for mar in sorted_population:
        #    if mar.fitness > median_fit * 2:
        #        for _ in range(10):
        #            self.mating_pool.append(mar)
        #    n = random.randint(0, 100)
        #    if n in range(chance):
        #        self.mating_pool.append(mar)
        #    chance -= (len(sorted_population) // 100) * 2

    def crossover(self, parent_one, parent_two):
        ##ver 0.2



        ##ver 0.1
        rand = random.randint(2,self.genome_size)
        child_genes = np.concatenate((parent_one[:rand],parent_two[rand:]), axis=0)
        child = Marvin(self.genome_size, genes=child_genes)
        return child

    def sex(self):
        p_size = len(self.mating_pool) - 1
        for i in range(self.size):
            dad = random.randint(0, p_size)
            while True:
                #print("mom loop")
                mom = random.randint(0, p_size)
                #print(dad, mom)
                if mom != dad: break
            child = (self.crossover(self.mating_pool[dad].actions, self.mating_pool[mom].actions))
            ##Testing crossover 2
            #print(dad, mom)
            #print("Dad", self.mating_pool[dad].actions)
            #print("Mom", self.mating_pool[mom].actions)
            #print("Child", child.actions)
            self.next_generation.append(child)
        for i in range(self.size - 1):
            number = random.randint(0, 100) 
            if number == 42:
                for _ in range(self.genome_size // 3):
                    self.next_generation[i].actions[random.randint(0, self.genome_size - 1)] = env.action_space.sample()
        print("______________________________")
        self.population = self.next_generation


class Evolution:

    def __init__(self, p_size, g_size, mut_chance=0.1):
        self.population_size = p_size
        self.gen = 0
        self.genome_size = g_size
        self.mutation_chance = mut_chance

    def soup(self):
        mating_pool = []
        self.current_population = Population(self.population_size, self.genome_size, mating_pool) 
        self.current_population.create()
        while(True):
            print("Generation", self.gen)
            self.current_population.compete()
            self.current_population.sex()
            self.gen += 1

      




life = Evolution(1000, 10)        
life.soup()



env.close()
