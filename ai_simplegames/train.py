#Space Discover: Genetic Algorithms - Training File 

#Importing the libraries
import numpy as np
from environment import Environment

# Creating the bots
# dna = 3,2,1,0
# fitness = total distance travelled
class Route():

    def __init__(self, dnaLength):
        self.dnaLength = dnaLength # set dna length
        self.dna = list() # set dna a list
        self.distance = 0 # distance 

        # initalize the random DNA
        for i in range(self.dnaLength - 1):
            # gen rand num, append to list, if it appears
            # chk if it appears in list and if so make a new
            # rnadom numb 
            rnd = np.random.randint(1, self.dnaLength) # random value
            while rnd in self.dna: # 
                rnd = np.random.randomint(1, self.dnaLength)
            self.dna.append(rnd)
        self.dna.append(0) # drop a 0 at the end
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
        self.dna = dna1.copy() # copy dna1
        
        for i in range(self.dnaLength - 1): 
            # switch DNA sequences randomly
            if np.random.rand() <= 0.5: # select index randomly
                previous = self.dna[i] # 
                inx = self.dna.index(dna2[i])
                self.dna[inx] = previous # 
                self.dna[i] = dna2[i]
        
        # random partial mutations
        
                





