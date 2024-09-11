from hero import Hero, SuperHero
from goblin import Goblin
from menu import Menu 

heroes = []

main_menu_options = [
    "Recruit Hero",
    "Train Heroes",
    "Feed Heroes", 
    "View Heroes' status", 
    "Fight Goblin",
]

recruit_menu_options = [
   "Hero", 
   "Super Hero"
]

def print_menu_error():
    print("Not a valid choice! Shameful!! Try again!")

main_menu = Menu(main_menu_options)
recruit_menu = Menu(recruit_menu_options)

run = True

def main():

    while run == True:
        choice = main_menu.get_choice()

        if choice == 1:
            hero_name = input("What would you like to name your hero?")
            type_choice = recruit_menu.get_choice()
            if type_choice == 1:
                heroes.append(Hero(hero_name))
            elif type_choice == 2:
                heroes.append(SuperHero(hero_name))
            else:
                print_menu_error

        elif choice == 2:
            for hero in heroes:
               hero.hero_train()
            print("Your heroes hit the gym!")
        
        elif choice == 3:
            for hero in heroes:
               hero.hero_eat()
            print("Your heroes ate a feast")
        
        elif choice == 4:
            if not heroes:
               print("No heroes to be found")
            else:
                for hero in heroes:
                   print(f"{hero.hero_name}: Health: {hero.hero_health}, Power: {hero.hero_power}")

        elif choice == 5:
            attack_goblin()

        else:
            print_menu_error()     

def attack_goblin():
    goblin = Goblin("Goblin", goblin_health=1000, goblin_power=8, goblin_damaged=3)
    
    if not heroes:
        print("No heroes to be found! Recruit Immediately!!")
        return
    
    for hero in heroes:
        print(f"{hero.hero_name} is attacking the goblin with {hero.hero_power}")
        goblin_alive = goblin.take_damage(hero.hero_power)

        if not goblin_alive:
            print(f"The goblin has been defeated by {hero.hero_name}! Huzzah!")
            break  

    if goblin.goblin_health > 0:
        print("The goblin survived the attack... for now")    

main()