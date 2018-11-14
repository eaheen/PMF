from random import random,randint,choice,choices
from schools import *
import time
class Player(object):
    def __init__(self,myName='Adventurer',level=0,hp=100.0,mhp=10,school=Style,focus=Style,xpos=0,ypos=0,vel=0):
        self.__hp_statii = ('dead','limbo','stasis','invulnerable','critical','severe','damaged','stable','perfect')
        self.name = myName
        self.level = level
        self.hp = hp
        if mhp < 0:
            mhp = 10
        self.mhp = mhp
        self.sghp = 100
        self.fort = 100
        self.school = school
        self.focus = focus
        self.xp = 0
        self.nextLv = 100
        self.accuracy = 0.8
        self.dodge = 0.05
        self.codex = Codex(0,)
        self.inventory = []
        self.hp_status = self.__hp_statii[-1]
    def newPlayer(self):
        Player.__init__(self)
    def levelUp(self):
        self.mhp += randint(7,14)
        self.nextLv *= 1.22
    def checkHP(self):
        self.hpp = 100 * self.hp / self.mhp
        if self.hp <= 0:
            if 'Ankh' in self.inventory:
                self.hp = self.mhp
                self.hp_status = self.__hp_statii[9]
                self.inventory.pop(self.inventory.index('Ankh'))
            else:
                self.hp = 0
                self.hp_status = self.__hp_statii[0]
        elif 0 < self.hpp < 10:
            self.hp_status = self.__hp_statii[4]
        elif 10 <= self.hpp < 25:
            self.hp_status = self.__hp_statii[5]
        elif 25 <= self.hpp < 50:
            self.hp_status = self.__hp_statii[6]
        elif 50 <= self.hpp < 85:
            self.hp_status = self.__hp_statii[7]
        elif 85 <= self.hpp < 100:
            self.hp_status = self.__hp_statii[8]
        elif self.hpp == 100:
            self.hp_status = self.__hp_statii[9]
    def checkSG(self):
        if self.sghp <= 0:
            self.rupture()
    def rupture(self):
        #do stuff with self.school and self.focus
        while self.sghp <= 0:
            self.fort - 0.01
            time.sleep(0.002)