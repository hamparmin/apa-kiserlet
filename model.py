import random, numpy
from collections import Counter

"""
Notes:
"""
class Test_Unit:
    def __init__(self,x,y,z,fix_tul):
        self.x=x
        self.y=y
        self.z=z
        self.fix_tul = fix_tul
        self.csoport = self.make_group()
        self.hasonlosag = self.calc_hasonlosag()
        self.sztereo=self.calc_sztereo()

    def create_population(self):
        list_of_lists=[[random.randint(1,self.y) for j in range(self.z)] for i in range(self.x)] #Megcsinálja a populációt, kiosztja a tulajdonságokat. A tulajdonságok duplikáltak is lehetnek
        return list_of_lists

    def most_frequent(self,alist):
        f_list = list(numpy.concatenate(alist).flat) #Kilaposítja a populációs listát.
        counter = 0
        num = f_list[0]
        
        for i in f_list:
            curr_frequency = f_list.count(i)
            if(curr_frequency> counter):
                counter = curr_frequency
                num = i
    
        return num
    
    def make_group(self):
        list_of_lists=self.create_population()
        
        csoport=[]
        nemcsoport=[]
        csoportkepzo = self.most_frequent(list_of_lists)

        i = 0
        for i in range(self.x):
            csoport.append(list_of_lists[i]) if csoportkepzo in list_of_lists[i] else nemcsoport.append(list_of_lists[i])
            i = i + 1 #Létrehozza a Csoport a leggyakoribb tulajdonság alapján.
        return csoport,nemcsoport


    def calc_hasonlosag(self):
        csoport,nemcsoport = self.make_group()

        j = 0
        k = j + 1
        csoporthasonlosagok = []
        while j < len(csoport)-1:
            csoporthasonlosagok.append(set(csoport[j]).intersection(csoport[k])) #Megnézi minden egyes csoporttag minden más csoporttaghoz fűződő hasonlóságát = megnézi, hogy hány közös elem van a két tulajdonsághalmaz között.
            k += 1
            if k == len(csoport):
                j += 1
                k = j+1
                
        csoporthasonlosag_nagysaga = [len(csoporthasonlosagok[l]) for l in range (len(csoporthasonlosagok))] #Megszámolja a közös elemeket.
        csoporthasonlosag = sum(csoporthasonlosag_nagysaga) / len(csoporthasonlosag_nagysaga) #Átlagolja az egyes hasonlóságokat.
        return csoporthasonlosag

    def calc_sztereo(self):
        csoport,nemcsoport = self.make_group()


        sdfix = []

        flattened_csoport = list(numpy.concatenate(csoport).flat) # Kilaposítja a Csoport listát.
        c = Counter(flattened_csoport)


        c.most_common(self.fix_tul)
        sdfix.append(c.most_common(self.fix_tul))
        sdfix_list = list(numpy.concatenate(sdfix).flat) #Megkeresi az n számú leggyakoribb tulajdonságot.
        sdfix_list = sdfix_list[::2] #Mivel itt egy dictionaryt gyártott le, kiszedi a dictionaryből az értékeket.


        sd_aktualizalt = []
        sztereohasonlosagok = []
        sd_iter_n=(self.z-len(sdfix_list))
        nemcsoport_merete = len(nemcsoport) 

        for j in range(nemcsoport_merete):
            sublist=[]
            for element in sdfix_list: 
                sublist.append(element)
            for i in range(sd_iter_n): #add a random number to sublist x-times
                sublist.append(random.randint(1,self.y))
            sd_aktualizalt.append(sublist)
            sztereohasonlosagok.append(set(nemcsoport[j]).intersection(sd_aktualizalt[j]))
     
        sztereohasonlosagok_nagysaga = [len(sztereohasonlosagok[l]) for l in range (len(sztereohasonlosagok))]
        sztereohasonlosag = sum(sztereohasonlosagok_nagysaga) / len(sztereohasonlosagok_nagysaga)

        return sztereohasonlosag
