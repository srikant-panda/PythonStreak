class Character:
    @classmethod
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
    
    def attack_enemy(self):
        print(f'{self.name} attack with power {self.attack} with {self.health} health.')


warriror = Character('Sudhansu',100,34)

mage = Character("Srikant",80,54)

warriror.attack_enemy()
mage.attack_enemy()


"""
1 - classes
2-  objects
3-  inheritance
4-  encapsulation
5-  polymorphism

"""