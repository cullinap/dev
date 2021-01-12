#Space Discover: Genetic Algorithms - Training File 

#Importing the libraries
import numpy as np
from environment import Environment

# Creating the bots
# dna = 3,2,1,0
# fitness = total distance travelled
class Route():

    def __init__(self, dnaLength):
        self.dnaLength = dnaLength
        self.dna = list()
        self.distance = 0

        # initalize the random DNA
        for i in range(self.dnaLength - 1):
            # dna = 3,1,2
            rnd = np.random.randint(1, self.dnaLength)
            while rnd in self.dna:
                rnd = np.random.randomint(1, self.dnaLength)
            self.dna.append(rnd)
        self.dna.append(0)
        # dna = 3,1,2,0

    # Building the Crossover method
    def mix(self, dna1, dna2):
        # dna1 = 1,2,3,4,0
        # dna2 = 4,3,2,1,0

        # dna = dna1.copy()

        # i = 1, dna[i] = 2, dna2[i] = 3
        # previous = dna[i] = 2
        # inx3 = 2
        # dna[inx3] = previous
        # dna = 1,2,3,4,0
        # dna[i] = dna[2]
        self.dna = dna1.copy()
        
        for i in range(self.dnaLength - 1):
            if np.random.rand() <= 0.5:
                previous = self.dna[i]
                inx = self.dna.index(dna2[i])
                self.dna[inx] = previous
                self.dna[i] = dna2[i]
        
        # random partial mutations

                





