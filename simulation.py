from model import Test_Unit
from matplotlib import pyplot as plt
import numpy as np

class Simulation():
    def __init__(self,n_fut,x,y,z,fix_tul):
        self.n_fut=n_fut
        self.x=x
        self.y=y
        self.z=z
        self.fix_tul=fix_tul

        self.run()

    def make_unit(self):
        csoport= Test_Unit(self.x,self.y,self.z,self.fix_tul)
        return csoport

    def run(self):
        #run Simulation n-times
        hasonlosagok=[]
        sztereok=[]
        for _ in range(self.n_fut):
            csoport=self.make_unit()
            hasonlosagok.append(csoport.hasonlosag)
            sztereok.append(csoport.sztereo)

        self.hasonlosagok=hasonlosagok
        self.sztereo=sztereok

    def display(self):
        x=list(range(1,self.n_fut+1))

        plt.scatter(x,self.hasonlosagok, c='b', marker='x', label='hasonlosagok')
        plt.scatter(x, self.sztereo, c='r', marker='s', label='sztereohasonlosagok')
        plt.legend(loc='bottom right')
        plt.xlabel="number of simulations"
        plt.ylabel="mean hasonlosag"
        plt.show()
    