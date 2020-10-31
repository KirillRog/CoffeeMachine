class CoffeeMachine:
    def __init__(self):
        self.state = {"money": 550, "water": 400, "milk": 540, "grams": 120, "cups": 9}

    def take_money(self):
        print(f"I gave you ${self.state['money']}")
        self.state['money'] = 0

    def machine_self(self):
        print("\nThe coffee machine has:")
        print(f"{self.state['water']} of water")
        print(f"{self.state['milk']} of milk")
        print(f"{self.state['grams']} of coffee beans")
        print(f"{self.state['cups']} of disposable cups")
        print(f"${self.state['money']} of money")

    def fill_machine(self):
        water = int(input("Write how many ml of water do you want to add: "))
        milk = int(input("Write how many ml of milk do you want to add: "))
        grams = int(input("Write how many grams of coffee beans do you want to add: "))
        cups = int(input("Write how many disposable cups of coffee do you want to add: "))
        self.state['water'] += water
        self.state['milk'] += milk
        self.state['grams'] += grams
        self.state['cups'] += cups

    def availability(self, water, milk, grams, money, cups):
        if self.state['water'] < water:
            print("Sorry, not enough water!")
            return False
        elif self.state['milk'] < milk:
            print("Sorry, not enough milk!")
            return False
        elif self.state['grams'] < grams:
            print("Sorry, not enough milk!")
            return False
        elif self.state['cups'] < cups:
            print("Sorry, not enough milk!")
            return False
        else:
            print("I have enough resources, making you a coffee!")
            self.state['water'] -= water
            self.state['milk'] -= milk
            self.state['grams'] -= grams
            self.state['money'] += money
            self.state['cups'] -= 1

    def buy_coffee(self, choice):
        if '1' == choice:
            self.availability(250, 0, 16, 4, 1)
        elif "2" == choice:
            self.availability(350, 75, 20, 7, 1)
        elif "3" == choice:
            self.availability(200, 100, 12, 6, 1)
        elif "back" == choice:
            return

    def machine_state(self, action):
        while action != "exit":
            if action == "start":
                answer = input("\nWrite action (buy, fill, take, remaining, exit): ")
                if answer == "exit":
                    return
                elif answer == "buy":
                    answer = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
                    self.buy_coffee(answer)
                elif answer == "fill":
                    self.fill_machine()
                elif answer == "take":
                    self.take_money()
                elif answer == "remaining":
                    self.machine_self()


coffee = CoffeeMachine()
coffee.machine_state('start')
