import time as t
import random as r
from bossFightClassTesting import dracula 




    
clickMultiplier = 1  
gemMultiplier = 1
damage = 1

# Functions and classes

def paddingCalculation(points, key):
    padding = []
    lengthOfPoints = len(str(points))
    if key == 'adult':
        paddingValue = 29 - lengthOfPoints
        for i in range(0, paddingValue):
            padding.append(" ")
    elif key == 'child':
        paddingValue = 12 - lengthOfPoints
        for i in range(0, paddingValue):
            padding.append(" ")
    else:
        paddingValue = 18 - lengthOfPoints
        for i in range(0, paddingValue):
            padding.append("‾")
    padding = ''.join(padding)
    return padding

def diceRoll(points):
    print("You roll two 6 sided dice if they are the same value, you win 1000 points!! \n")
    t.sleep(1)
    x = r.randint(1,6)
    y = r.randint(1,6)
    if x == y:
        print(f'You got {x} and {y} so you WIN')
        points += 1000
    else:
        print(f'You got {x} and {y} so you lose :(')
    return points

def numberGuess(points): 
    min = int(input('Enter minimum: '))
    max = int(input('Enter maximum: '))
    x = r.randint(min, max)
    guess = int(input('Guess number: '))
    amountGained = 100 * (max-min)
    if guess == x:
        points += amountGained
        print(f'CORRECT +{amountGained} points')
    else:
        print(f'WRONG: It was {x}')
    
    return points


def storyShop(points):
    hasFightOccurred = False
    while True:
        padding = paddingCalculation(points, 'adult')
        print(f"""
                   ___________________________________________
                  ////////////////////////////////////////////|
                 /////////////////////////////////////////////|
                |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾SHOP‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|//|
                |==== [1] Boss Fight: 100              ====|//|
                |==== [2] Roll the Dice: 10            ====|//|
                |==== [3] Guess Number: 10             ====|//|
                |==== [4] Riddle: 50                   ====|//|
                |==== [5] General Knowledge: 50        ====|//|     
                |__________________________________________|//|
                |                                          |//|
                |     Points: {points}{padding}|//
                |__________________________________________|/
    """)
        option = input("")
        if option == '1':
            dracula.bossFight(damage, gemMultiplier, inventory)
            hasFightOccurred = True
            break
        elif option == '2':
            points -= 10
            points = diceRoll(points)
        elif option == '3':
            points -= 10
            points = numberGuess(points)
        elif option.lower() == 'b':
            break
    return points, hasFightOccurred

def damageShop(points, damage):
    stockArray = [[1, 100], [10, 200], [25, 300], [50, 400], [100, 500]]
    while True:
        padding = paddingCalculation(points, 'adult')
        print(f"""
                   ___________________________________________
                  ////////////////////////////////////////////|
                 /////////////////////////////////////////////|
                |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾SHOP‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|//|
                |==== [1] Damage +1: 100               ====|//|
                |==== [2] Damage +10: 200              ====|//|
                |==== [3] Damage +25: 300              ====|//|
                |==== [4] Damage +50: 400              ====|//|
                |==== [5] Damage +100: 500             ====|//|     
                |__________________________________________|//|
                |                                          |//|
                |     Points: {points}{padding}|//
                |                                          |/
                 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    """)
        option = input("")
        if option in ['1', '2', '3', '4', '5']:
            if points >= stockArray[int(option)-1][1]:
                damage += stockArray[int(option)-1][0]
                points -= stockArray[int(option)-1][1]
            else:
                print('Not enough points broke ahh')
        elif option.lower() =='b':
            break
        else:
            pass

    return damage, points
    


def checkStats():
    print(f"""
    Point Multiplier (x{clickMultiplier})
    Gem Multiplier (x{gemMultiplier})
    Damage ({damage})
""")

inventory = {
    'Cookies 🍪':0,
    'Gems 💎':500,
}

def showInventory():
    print("Inventory: ")
    for item, amount in inventory.items():
        print(f"- {item} ({amount})")


class Shop:
    def __init__(self, name, price, level, rate):
        self.name = name
        self.price = price
        self.level = level
        self.rate = rate

    def clickerEnabled(self, points):
        while True:
            t.sleep(5)
            points += self.rate

# Declaring objects that will be used as shop options

pssveClkr1 = Shop('Lvl 1', 100, 1, 0.5)
pssveClkr2 = Shop('Lvl 2', 300, 2, 1)
pssveClkr3 = Shop('Lvl 3', 500, 3, 2)
pssveClkr4 = Shop('Lvl 4', 1000, 4, 4)
pssveClkr5 = Shop('Lvl 5', 2000, 5, 10)

GemMult1 = Shop('Lvl 1', 10, 1, 0.5)
GemMult2 = Shop('Lvl 2', 30, 2, 1)
GemMult3 = Shop('Lvl 3', 50, 3, 2)
GemMult4 = Shop('Lvl 4', 100, 4, 4)
GemMult5 = Shop('Lvl 5', 200, 5, 10)

# Array to use as object seection later on 

ClkrArray = [pssveClkr1,pssveClkr2, pssveClkr3, pssveClkr4, pssveClkr5 ]
GemArray = [GemMult1, GemMult2, GemMult3, GemMult4, GemMult5]

def gemShop(inventory, gemMultiplier):
    while True:
        adultPadding = paddingCalculation(inventory['Gems 💎'], 'adult')
        print(f"""
                   ___________________________________________
                  ////////////////////////////////////////////|
                 /////////////////////////////////////////////|
                |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾SHOP‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|//|
                |==== [1] Gem Multiplier Lvl 1         ====|//|
                |==== [2] Gem Multiplier Lvl 2         ====|//|
                |==== [3] Gem Multiplier Lvl 3         ====|//|
                |==== [4] Gem Multiplier Lvl 4         ====|//|
                |==== [5] Gem Multiplier Lvl 5         ====|//|     
                |__________________________________________|//|
                |                                          |//|
                |     Gems ⟡: {inventory['Gems 💎']}{adultPadding}|//
                |                                          |/
                 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    """)
        option = input("")
        if option in ['1', '2', '3', '4', '5']:
            childPadding = paddingCalculation(points, 'child')
            x = GemArray[int(option)-1]
            ratePadding = paddingCalculation(x.rate, 'adult')
            pricePadding = paddingCalculation(x.price, 'adult')
            dashing = paddingCalculation(inventory['Gems 💎'], 'misc')
            
            print(f''' 
              ______________________________________________
             ///////////////////////////////////////////////|     
            |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾{x.name}‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|/|
            |==== Rate: x{1+(x.rate)}{ratePadding}====|/|
            |==== Price: {x.price}{pricePadding}====|/|
            |_____________________________________________|/
                 |Gems ⟡: {inventory['Gems 💎']}{childPadding}|/
                  ‾‾‾‾‾‾‾‾{dashing}
                    ''')
            print(f"Dashes: {len(dashing)}")
            print(f"Padding: {len(childPadding)}")
            choice = input('Would you like to purchase? Y/n')
            if choice == 'Y' and inventory['Gems 💎'] >= x.price:
                inventory['Gems 💎'] -= x.price
                gemMultiplier += (x.rate) # Here if the operation between multiplier and the brackets is changed to a multiply (*)
                                                # the amount of gems drastically increases instead of if an addition is used.
            elif choice == 'Y' and inventory['Gems 💎'] < x.price:
                print("Not enough gems \n")

            else:
                pass
        elif option.lower() == 'b':
            break
        else:
            print('Please select a valid option, or "b" to go back \n')
    return gemMultiplier



def pssveClkrMenu(clickMultiplier, points): # Still need to implement passive clicking; make sure to use threading
    while True:            # or async processes
        adultPadding = paddingCalculation(points, 'adult')
        print(f"""
                   ___________________________________________
                  ////////////////////////////////////////////|
                 /////////////////////////////////////////////|
                |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾SHOP‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|//|
                |==== [1] Clicker Multiplier Lvl 1     ====|//|
                |==== [2] Clicker Multiplier Lvl 2     ====|//|
                |==== [3] Clicker Multiplier Lvl 3     ====|//|
                |==== [4] Clicker Multiplier Lvl 4     ====|//|
                |==== [5] Clicker Multiplier Lvl 5     ====|//|     
                |__________________________________________|//|
                |                                          |//|
                |     Points: {points}{adultPadding}|//
                |                                          |/
                 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    """)
        option = input("")
        if option in ['1', '2', '3', '4', '5']:
            childPadding = paddingCalculation(points, 'child')
            x = ClkrArray[int(option)-1]
            ratePadding = paddingCalculation(x.rate, 'adult')
            pricePadding = paddingCalculation(x.price, 'adult')
            dashing = paddingCalculation(points, 'misc')
            print(f''' 
              ______________________________________________
             ///////////////////////////////////////////////|     
            |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾{x.name}‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|/|
            |==== Rate: x{1+(x.rate)}{ratePadding}====|/|
            |==== Price: {x.price}{pricePadding}====|/|
            |_____________________________________________|/
                 |Points: {points}{childPadding}|/
                  ‾‾‾‾‾‾‾‾{dashing}
                    ''')
            print(f"Dashes: {len(dashing)}")
            print(f"Padding: {len(childPadding)}")
            choice = input('Would you like to purchase? Y/n')
            if choice == 'Y' and points >= x.price:
                points -= x.price
                clickMultiplier += (1+x.rate)       # Here if the operation between multiplier and the brackets is changed to a multiply (*)
                                                  # the amount of gems drastically increases instead of if an addition is used.
            elif choice == 'Y' and points < x.price:
                print("Not enough points \n")

            else:
                pass
        elif option.lower() == 'b':
            break
        else:
            print('Please select a valid option, or "b" to go back \n')
    return clickMultiplier, points





def cookie():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠚⣉⡙⠲⠦⠤⠤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⠛⠉⠉⠀⣾⣷⣿⡆⠀⠀⠀⠐⠛⠿⢟⡲⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⢞⣭⠎⠀⠀⠀⠀⠘⠛⠛⠀⠀⢀⡀⠀⠀⠀⠀⠈⠓⠿⣄⠀⠀⠀
⠀⠀⠀⡜⣱⠋⠀⠀⣠⣤⢄⠀⠀⠀⠀⠀⠀⣿⡟⣆⠀⠀⠀⠀⠀⠀⠻⢷⡄⠀
⠀⢀⣜⠜⠁⠀⠀⠀⢿⣿⣷⣵⠀⠀⠀⠀⠀⠿⠿⠿⠀⠀⣴⣶⣦⡀⠀⠰⣹⡆
⢀⡞⠆⠀⣀⡀⠀⠀⠘⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣶⠇⠀⢠⢻⡇
⢸⠃⠘⣾⣏⡇⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⣠⣤⣤⡉⠁⠀⠀⠈⠫⣧
⡸⡄⠀⠘⠟⠀⠀⠀⠀⠀⠀⣰⣿⣟⢧⠀⠀⠀⠀⠰⡿⣿⣿⢿⠀⠀⣰⣷⢡⢸
⣿⡇⠀⠀⠀⣰⣿⡻⡆⠀⠀⠻⣿⣿⣟⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠘⢿⡿⣸⡞
⠹⣽⣤⣤⣤⣹⣿⡿⠇⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⣽⠀
⠀⠙⢻⡙⠟⣹⠟⢷⣶⣄⢀⣴⣶⣄⠀⠀⠀⠀⠀⢀⣤⡦⣄⠀⠀⢠⣾⢸⠏⠀
⠀⠀⠘⠀⠀⠀⠀⠀⠈⢷⢼⣿⡿⡽⠀⠀⠀⠀⠀⠸⣿⣿⣾⠀⣼⡿⣣⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⣆⠑⠋⠀⢀⣀⠀⠀⠀⠀⠈⠈⢁⣴⢫⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣧⣄⡄⠴⣿⣶⣿⢀⣤⠶⣞⣋⣩⣵⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⢯⣭⣭⣯⣯⣥⡵⠿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀""")
    inventory['Cookies 🍪'] += 1

print('Welcome to the CLICKER GAME!')

t.sleep(1)

def help():
    print('- Press ENTER to gain points')
    t.sleep(0.5)
    print('- Q to check points')
    t.sleep(0.5)
    print('- Ctrl-C to stop')
    t.sleep(0.5)
    print('- S for shop')
    t.sleep(0.5)
    print('- B to go back')
    t.sleep(0.5)
    print('- I for inventory')
    t.sleep(0.5)
    print('- M for stats')
    t.sleep(0.5)
    print('- ? for help')


#help()

t.sleep(1)

print("CLICK!")

points = 10000

      
try:
    while True:
        padding = paddingCalculation(points, 'adult')        
        option = input("")
        if option == "":
            points += (1*(clickMultiplier))
        elif option.lower() == 'q':
            print(f'Point total: {points}')
        elif option.lower() == '?':
            help()
        elif option.lower() == 'm':
            checkStats()
        elif option.lower() == 'i':
            showInventory()
        elif option.lower() == 's':
            while True:
                print(f'''
            ===================SHOP===================
            ==== [1] Clicker Shop                 ====
            ==== [2] Cookie: 100                  ====
            ==== [3] Gem Shop                     ====
            ==== [4] Damage Shop                  ====
            ==== [5] Story Shop                   ====
            ==========================================
                Points: {points}                     
            ==========================================
                    ''')
                
                option = input("")
                if option == "1":
                    clickMultiplier, points = pssveClkrMenu(clickMultiplier, points)
                    
                    if option.lower == 'b':
                        break
                elif option == "2":
                    if points > 100:
                        cookie()
                        points = points - 100
                        break
                    else:
                        print('Not enough points')
                        break
                elif option == '3':
                    gemMultiplier = gemShop(inventory, gemMultiplier)
                elif option == '4':
                    damage, points = damageShop(points, damage)
                elif option == '5':
                    points, hasFightOccurred = storyShop(points)
                    if hasFightOccurred:
                        break
                    else:
                        pass
                elif option.lower() == "b":
                    break

            


except KeyboardInterrupt:
    print("Game Ended")
    print(f"Points earned: {points}")


