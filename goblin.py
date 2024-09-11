class Goblin:
    def __init__(self, goblin_name, goblin_health=1000, goblin_power=8, goblin_damaged=3):
        self.goblin_name = goblin_name
        self.goblin_health = goblin_health
        self.goblin_power = goblin_power
        self.goblin_damaged = goblin_damaged

    def take_damage(self, damage):
        self.goblin_health -= damage
        print(f"{self.goblin_name} took {damage} damage! Health is now {self.goblin_health}")
        
        if self.goblin_health <= 0:
            print(f"{self.goblin_name} has been defeated!")
            return False
        return True
