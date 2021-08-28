class Pokemon:
    def __init__(self, name, level = 5, type ):
        self.name = name
        self.level = level
        self.type = type
        self.is_knocked_out = False
        self.max_health = level
        self.health = self.max_health


    def __repr__(self):
        return "info: {} is in level: {} ,and is type is: {},maximun health: {}, current health: {}.\n".format(self.name, self.level ,self.type, self.max_health, self.health)

    def lose_health(self, dmg):
        pass

    def regaining_health(self, gain):
        pass

    def knock_out(self,knock):
        if self.health <= 0:
           self.is_knocked_out = True
      pass

    def revive_Pokemon(self):
# revive a knocked out Pokémon
      pass

    def attack(self):
        pass