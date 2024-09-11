class Menu:
    def __init__(self, options):
        self.options = options

    def get_choice(self):
        while True:

            for i, option in enumerate(self.options, 1):
                print(f"{i}: {option}")
            choice = input("Please choose an option: ")

            try:
                choice = int(choice)
                if 1 <= choice <= len(self.options):
                    return choice
                else:
                    print("Not a valid choice! Shameful!! Try again!")
            except ValueError:
                print("Use a number please. C'mon, this isn't hard.")
                

