
import time as t


class Boss:

    def __init__(self, name, health, time, lore, intro, pronoun):
        self.name = name
        self.health = health
        self.time = time
        self.lore = lore
        self.intro = intro
        self.pronoun = pronoun
    
    def bossFight(self, damage, gemMultiplier, inventory, fightType, weapon=None):

        if fightType == 'clicker': # Spam click fights
            bossHP = self.health
            HParray = []
            for i in range(0, bossHP, 10):
                HParray.append('█')
            print(self.intro)
            t.sleep(0.5)
            choice = input(f'Do you wish to face {self.pronoun}? Y/n')
            if choice == 'Y':
                t.sleep(0.5)
                print("      O                                     O      \n"
                    "{o)xxx|===============-  *  -===============|xxx(o}\n"
                    "      O                                     O      \n")
                t.sleep(1)
                print(f'Defeat {self.pronoun} within {self.time} seconds')
                t.sleep(2)
                print(f'Boss: {bossHP}hp {''.join(HParray)}')
                print(f'Dmg: {damage}dmg/click')
                t.sleep(2)
                print("FIGHT!")
                
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
        elif fightType == 'complex': # Used for more active boss
            pass


    def showStats(self):
        print(f"""
- Name: {self.name}
- Health ({self.health}hp)
- Time to Kill ({self.time}s)
- Lore:
{self.lore}""")
        


dracula = Boss('Vlad III Drăcula Țepeș', 
               100, 
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

cthulhu = Boss('Cthulhu Macula', 
               500, 
               5,
               ("In the shadowed recesses of forgotten lore, the Cthulhu Macula is a malevolent artifact,"
                " a dark remnant of the cosmic horrors that predate even the oldest of Earth’s civilizations."
                " Forged in the unfathomable void between stars, it is said to be a fragment of the primordial "
                "darkness that once coalesced into the dread entity known as Cthulhu. The Macula manifests as a"
                " pulsating, iridescent sigil, its surface shifting with an unsettling rhythm that mirrors the"
                " heartbeat of the cosmos. Legends whisper that it was once an instrument of unimaginable power," 
                "capable of bending reality itself to the will of its bearer. Those who seek it out are driven by"
                "a fatal curiosity, drawn to the Macula’s promise of forbidden knowledge. Yet, the price is steep:" 
                " madness and despair lurk in its wake, as the Macula’s ancient energies seep into the minds of those"
                "who dare to harness its dark potential, forever binding them to the will of the eldritch horrors from which it originated."),
                "High priestess of the great old ones, the sleeper of R'iyeh, the great Dreamer, the slumbering one, CTHULHU!",
                'him')

# ghostFace = Boss() #Not yet created

bossArray = [dracula, cthulhu]

# The goal is to eventually have a roster of bosses from which the user can pick to fight
# with different bosses having different playstyles.

# Only Cthulhu is in use at the moment as there doesnt exist an option for multiple bosses in the main
# file as of yet
