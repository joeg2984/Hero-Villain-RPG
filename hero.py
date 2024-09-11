class Hero:
    def __init__(self, hero_name, hero_health=10, hero_power=5, hero_damaged=2):
        self.hero_name = hero_name
        self.hero_health = hero_health
        self.hero_power = hero_power
        self.hero_damaged = hero_damaged

    def take_damage(self, damage):
        self.hero_health -= damage
        print(f"{self.hero_name} took {damage} damage! Health is now {self.hero_health}.")
        if self.hero_health <= 0:
            print(f"{self.hero_name} has died!")
            return False
        return True

    def attack(self, other):
        print(f"{self.hero_name} attacks {other.hero_name} with power {self.hero_power}")
        return other.take_damage(self.hero_power)
    
    def hero_eat(self):
        self.hero_health += 10

    def hero_train(self):
        self.hero_power +=20

class SuperHero(Hero):
    def __init__(self, hero_name, hero_health=50, hero_power=10):
        super().__init__(hero_name, hero_health, hero_power)