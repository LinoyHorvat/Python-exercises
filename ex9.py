# Implement all methods of class Creature
class Creature:
    def __init__(self, race, life, weapon_name, weapon_power):
        if not isinstance(race,str):
            raise TypeError
        if not isinstance(life,(int,float)):
            raise TypeError
        if not isinstance(weapon_name,str):
            raise TypeError
        if not isinstance(weapon_power,int):
            raise TypeError
        self.race=race
        self.life=life
        self.weapon_name=weapon_name
        self.weapon_power=weapon_power
        if not self.weapon_power>0:
            raise ValueError
    def hit(self, other):
        if self.is_alive() and other.is_alive():
            self.life=self.life-5.0
            hit_power=self.weapon_power+float(self.life/4)
            other.absorb(hit_power)
    def absorb(self, hit_power):
        self.life=self.life-hit_power
    def is_alive(self):
        if self.life>5.0:
            return True
        else:return False
    def get_life(self):
        return self.life
    def get_race(self):
        return self.race
# Implement class GoodCreature
class GoodCreature(Creature):
    def hit(self, other):
        if self.is_alive() and other.is_alive():
            self.life = self.life - 5.0
            hit_power=self.weapon_power+float(self.life/2)
            other.absorb(hit_power)
    def get_race(self):
        r=Creature.get_race(self)
        return "good " + r
# Implement class BadCreature
class BadCreature(Creature):
    def __init__(self, race, life, weapon_name, weapon_power, shield_power):
        Creature.__init__(self, race, life, weapon_name, weapon_power)
        self.shield_power=shield_power
        if not isinstance(shield_power,int):
            raise TypeError
        if not self.shield_power>0:
            raise ValueError
    def absorb(self, hit_power):
        self.life = self.life - hit_power+self.shield_power
# Implement all methods of class Battle
class Battle:
    def __init__(self, good_army, bad_army):
        self.good_army=good_army
        self.bad_army=bad_army
        for c in good_army:
            if not isinstance(c,(GoodCreature,Creature)):
                raise TypeError
        for c in bad_army:
            if not isinstance(c,(BadCreature,Creature)):
                raise TypeError

    def dual_fight(self, good_index, bad_index):
        good=self.good_army[good_index]
        bad=self.bad_army[bad_index]
        count=0
        while good.is_alive() and bad.is_alive():
            bad.hit(good)
            good.hit(bad)
            count += 1
        return count
# Implement class TotalBattle
class TotalBattle(Battle):
  def fight(self):
      b=0
      g=0
      count=0
      while b<=(len(self.bad_army)-1):
          while g<=(len(self.good_army)-1):
              c=self.dual_fight(g,b)
              count=count+c
              if self.bad_army[b].is_alive() is True:
                  g+=1
              elif self.good_army[g].is_alive() is True:
                  break
          b+=1
      i=0
      j=0
      lg=[]
      lb=[]
      while i <=(len(self.good_army)-1):
          if self.good_army[i].is_alive():
              lg.append(self.good_army[i])
          i+=1
      while j <=(len(self.bad_army)-1):
          if self.bad_army[j].is_alive():
              lb.append(self.bad_army[j])
          j+=1
      if len(lb) == len(lg) == 0:
          print 'Draw'
      else:
          if lg==[]:
              print 'Evil won'
          elif lb==[]:
              print 'Good guys won'
      return count
