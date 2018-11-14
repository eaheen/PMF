from random import random

class Codex(object):
    def __init__(self,abilityIndex={}):
        self.numAbilities = len(abilityIndex)
        self.abilityIndex = {'fireball':Ability()}

class Ability:
    def __init__(self,name='noneAbility',intent=-1,weight=0,cost=0,scalar=1,difficulty=1,bloodCost=0):
        self.name = name
        self.intent = fixIntent(intent)
        self.setIntentStr()
        self.weight = weight
        self.cost = cost
        self.scalar = scalar
        self.difficulty = difficulty
        self.bloodCost = bloodCost
    def fixIntent(self,intent):
        if intent < -1:
            return -1
        elif intent > 1:
            return 1
        elif (-1 < intent < 1) and (intent != 0):
            return 0
        else:
            return intent
    def setIntentStr(self):
        if not self.intent:
            self.intentStr = 'Neutral'
        elif self.intent == -1:
            self.intentStr = 'Destructive'
        elif self.intent == 1:
            self.intentStr = 'Constructive'
    def setName(self,newName):
        self.name = newName
    def setIntent(self,newIntent):
        self.intent = newIntent
    def setWeight(self,newWeight):
        self.weight = newWeight
    def setCost(self,newCost):
        self.cost = newCost
    def setScalar(self,newScalar):
        self.scalar = newScalar
    def cast(self,caster,target):
        if (caster.accuracy - self.difficulty/10) > target.dodge:
            target.hp += self.weight * self.intent * self.scalar * caster.scalar
            caster.sghp -= self.cost
        caster.hp -= self.bloodCost * (self.difficulty/2)
        caster.checkSG()
        caster.checkHP()
        target.checkHP()
    def __repr__(self):
        return 'Ability {0}, {1} intent, weight {2}, current scalar {3}'.format(self.name,self.intentStr,self.weight,self.scalar)


class Style:
    def __init__(self,abilities=Codex(0,{}),power=0,school='none',focus='none'):
        self.power = power
        self.codex = abilities
        self.school = school
        self.focus = focus
    def __repr__(self):
        if not self.power:
            return 'nonePower and noneStyle'
        else:
            return

class Blank(Style):
    def __init__(self):
        Style.__init__(self)
    def __repr__(self):
        return 'noneStyle'
