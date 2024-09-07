import time as t
import random as r



    
clickMultiplier = 1  
gemMultiplier = 1

# Functions and classes

def checkMultipliers():
    print(f"""
    Point Multiplier ({clickMultiplier})
    Gem Multiplier ({gemMultiplier})
""")

inventory = {
    'Cookies 🍪':0,
    'Gems 💎':0,
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

def gemShop(inventory):
    while True:
        print(f"""
                ===================SHOP===================
                ==== [1] Gem Muliplier Lvl 1          ====
                ==== [2] Gem Muliplier Lvl 2          ====
                ==== [3] Gem Muliplier Lvl 3          ====
                ==== [4] Gem Muliplier Lvl 4          ====
                ==== [5] Gem Muliplier Lvl 5          ====
                ==========================================
                    Gems 💎: {inventory['Gems 💎']}                     
                ==========================================
    """)
        option = input("")
        if option in ['1', '2', '3', '4', '5']:
            x = GemArray[int(option)-1]
            print(f'''
            ==============={x.name}==================
            ==== Rate: x{1+(x.rate)}                ====
            ==== Price: {x.price} 💎              ====
            ======================================
                    
                    ''')
            choice = input('Would you like to purchase? Y/n')
            if choice == 'Y' and inventory['Gems 💎'] >= x.price:
                inventory['Gems 💎'] -= x.price
                return gemMultiplier+(1+x.rate) # Here if the operation between multiplier and the brackets is changed to a multiply (*)
                                                # the amount of gems drastically increases instead of if an addition is used.
            elif choice == 'Y' and inventory['Gems 💎'] < x.price:
                print("Not enough gems \n")


            elif choice.lower() == 'n':
                break
            else:
                pass
        elif option.lower() == 'b':
            break
        else:
            print('Please select a valid option, or "b" to go back \n')





def bossFight():
    
    bossHP = 100
    HParray = ['█','█','█','█','█','█','█','█','█','█']
    print('A WILD MONSTER HAD APPEARED!!!')
    t.sleep(0.5)
    choice = input('Do you wish to face it? Y/n')
    if choice == 'Y':
        print("""
              __.......__
            .-:::::::::::::-.
          .:::''':::::::''':::.
        .:::'     `:::'     `:::. 
   .'\\  ::'   ^^^  `:'  ^^^   '::  /`.
  :   \\ ::   _.__       __._   :: /   ;
 :     \\`: .' ___\\     /___ `. :'/     ; 
:       /\\   (_|_)\\   /(_|_)   /\\       ;
:      / .\\   __.' ) ( `.__   /. \\      ;
:      \\ (        {   }        ) /      ; 
 :      `-(     .  ^"^  .     )-'      ;
  `.       \\  .'<`-._.-'>'.  /       .'
    `.      \\    \\;`.';/    /      .'
      `._    `-._       _.-'    _.'
       .'`-.__ .'`-._.-'`. __.-'`.
     .'       `.         .'       `.
   .'           `-.   .-'           `.
""")
        print('Defeat it within 10 seconds')
        t.sleep(1)
        print(f'Boss: {bossHP}hp ██████████ ')
        print('Dmg: 1dmg/click')

        x = t.time()

        while t.time() < x+10 and bossHP > 0:
            option = input("")
            if option == '':
                bossHP -= 1
            else:
                pass
            if bossHP%10 == 0:
                HParray.pop()
                print(f'{bossHP}: {''.join(HParray)}')
            else:
                pass

        if bossHP > 0:
            print('Boss fight failed')
        else:
            print('☠️')
            print('BOSS SLAIN')
            print(f'{(5* gemMultiplier)}+ gems 💎')
            inventory['Gems 💎'] += (5* gemMultiplier) 
    else:
        pass
    


        





def specialEvent(x):
    if x < 10:
        bossFight()
    else:
        pass

def pssveClkrMenu(points): # Still need to implement passive clicking; make sure to use threading
    while True:            # or async processes
        print(f"""
            ===================SHOP===================
            ==== [1] Passive Clicker Lvl 1        ====
            ==== [2] Passive Clicker Lvl 2        ====
            ==== [3] Passive Clicker Lvl 3        ====
            ==== [4] Passive Clicker Lvl 4        ====
            ==== [5] Passive Clicker Lvl 5        ====
            ==========================================
                Points: {points}                     
            ==========================================
                            """)
        option = input("")
        if option in ['1', '2', '3', '4', '5']:
            x = ClkrArray[int(option)-1]
            print(f'''
            ==============={x.name}==================
            ==== Rate: x{1+(x.rate)}                  ====
            ==== Price: {x.price} points          ====
            ======================================
                    
                    ''')
            choice = input('Would you like to purchase? Y/n')
            if choice == 'Y' and points >= x.price:
                points -= x.price
                return clickMultiplier+(1+x.rate), points # Here if the operation between multiplier and the brackets is changed to a multiply (*)
                                                  # the amount of gems drastically increases instead of if an addition is used.
            elif choice == 'Y' and points < x.price:
                print("Not enough points \n")


            elif choice.lower() == 'n':
                return clickMultiplier, points
            else:
                pass
        elif option.lower() == 'b':
            return clickMultiplier, points
        else:
            print('Please select a valid option, or "b" to go back \n')





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
    print('- m for multipliers')
    t.sleep(0.5)
    print('- ? for help')


help()

t.sleep(1)

print("CLICK!")

points = 0
      
try:
    while True:
        chance1 = r.randint(0,100)
        chance2 = r.randint(0,100)
        if chance1 == chance2:
            print("Success")
            specialEvent(chance1)
        option = input("")
        if option == "":
            points += (1*clickMultiplier)
        elif option.lower() == 'q':
            print(f'Point total: {points}')
        elif option.lower() == '?':
            help()
        elif option.lower() == 'm':
            checkMultipliers()
        elif option.lower() == 'i':
            showInventory()
        elif option.lower() == 's':
            while True:
                print(f'''
            ===================SHOP===================
            ==== [1] Passive Clickers             ====
            ==== [2] Cookie: 100                  ====
            ==== [3] Gem Shop                     ====
            ==========================================
                Points: {points}                     
            ==========================================
                    ''')
                
                option = input("")
                if option == "1":
                    clickMultiplier, points = pssveClkrMenu(points)
                    
                    if option.lower == 'b':
                        break
                elif option == "2":
                    if points > 100:
                        cookie()
                        points = points - 100
                        break
                elif option == '3':
                    gemMultiplier = gemShop(inventory)
                elif option.lower() == "b":
                    break

            


except KeyboardInterrupt:
    print("Game Ended")
    print(f"Points earned: {points}")


