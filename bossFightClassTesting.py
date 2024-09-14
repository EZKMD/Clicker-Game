
import time as t

#from main import inventory, damage, gemMultiplier

class Boss:

    def __init__(self, name, health, time, lore, intro, pronoun):
        self.name = name
        self.health = health
        self.time = time
        self.lore = lore
        self.intro = intro
        self.pronoun = pronoun
    
    def bossFight(self, damage, gemMultiplier, inventory):
        bossHP = self.health
        HParray = []
        for i in range(0, bossHP, 10):
            HParray.append('█')
        #HParray = ['█','█','█','█','█','█','█','█','█','█']
        print(self.intro)
        t.sleep(0.5)
        choice = input(f'Do you wish to face {self.pronoun}? Y/n')
        if choice == 'Y':
            print("      O                                     O      \n"
                  "{o)xxx|===============-  *  -===============|xxx(o}\n"
                  "      O                                     O      \n")
            print(f'Defeat {self.pronoun} within {self.time} seconds')
            t.sleep(1)
            print(f'Boss: {bossHP}hp {''.join(HParray)}')
            print(f'Dmg: {damage}dmg/click')

            x = t.time()

            while t.time() < x+self.time and bossHP > 0:
                option = input("")
                if option == '' and len(HParray) > 0:
                    bossHP -= damage
                else:
                    pass
                if bossHP%10 == 0 and len(HParray) > 0 :
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

    def showStats(self):
        print(f"""
- Name: {self.name}
- Health ({self.health}hp)
- Time to Kill ({self.time}s)
- Lore:
{self.lore}""")
        


dracula = Boss('Vlad III Drăcula Țepeș', 
               10000, 
               10, 
               ("Vlad III Drăcula Țepeș, the immortal Prince of Darkness, was once a noble warrior and brilliant tactician, "
     "feared on the battlefield for his unmatched cunning and ruthless command. Betrayed by humanity, his heart turned cold, "
     "and he embraced the ancient powers of the night, becoming a lord of vampires. His dominion stretches beyond the mortal realm, "
     "commanding legions of night creatures and wielding dark magic that warps reality itself. Dracula’s presence is an oppressive shadow "
     "that suffocates hope, his voice commanding the very elements, and his wrath manifesting in storms and hellfire. Immortal and untouchable, "
     "he embodies a dark vengeance, ruling over a cursed empire from his towering, ever-shifting castle, waiting for the day when the world "
     "will once again tremble under his iron fist.\n"),
     "A shrouded dark mass swoops onto the ground, and standing before you is the immortal prince of darkness "
     "DRACULA! ",
     'him')

#print(dracula.lore)

#dracula.bossFight()

#dracula.showStats()
