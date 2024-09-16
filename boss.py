
import time as t


class Boss:

    def __init__(self, name, health, time, lore, intro, pronoun, price):
        self.name = name
        self.health = health
        self.time = time
        self.lore = lore
        self.intro = intro
        self.pronoun = pronoun
        self.price = price
    
    def bossFight(self, damage, gemMultiplier, inventory, fightType, points, weapon=None):

        if fightType == 'clicker': # Spam click fights
            bossHP = self.health
            HParray = []
            for i in range(0, bossHP, 10):
                HParray.append('█')
            print(self.intro)
            t.sleep(0.5)
            choice = input(f'Do you wish to face {self.pronoun}? Y/n')
            if choice == 'Y':
                points -= self.price
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
                    return points
                else:
                    print('☠️')
                    print('BOSS SLAIN')
                    print(f'{(5* gemMultiplier)}+ gems 💎')
                    inventory['Gems 💎'] += (5* gemMultiplier) 
                    return points
            elif choice.lower() == 'n':
                return points
            else:
                print('Choose a valid option: ')
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
     'him',
     100)

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
                'him',
                100)

medusa = Boss('Medusa', 
              100,
              10,
              ("In Greek mythology, Medusa is one of the Gorgons, once a beautiful maiden who was cursed by Athena" 
               "to have snakes for hair and a gaze that turns anyone who looks at her into stone. Medusa is often" 
               "depicted as a monstrous figure, and her severed head was used by Perseus as a powerful weapon."),
               "The gorgon, the snake-haired monster, the stone maiden, the serpent queen, MEDUSA!",
               "her",
               100
               )

banshee = Boss('Banshee',
               100,
               10,
               ("In Irish folklore, a Banshee is a wailing spirit that foretells the death of a family member."
                "Often depicted as a mournful woman with long, flowing hair, her cry is a chilling omen of tragedy" 
                "and is deeply rooted in Irish cultural traditions."),
                "The wailing woman, the death messanger, the bean sidhe, the fairie of the mourning cry, BANSHEE!",
                "her",
                100
                )

jörmungandr = Boss("Jörmungandr",
                   100,
                   10,
                   ("Jörmungandr, known as the Midgard Serpent, is a primordial creature born from the chaos of" 
                    " the ancient oceans and the blood of the first gods. According to the ancient texts lost to"
                    " time, Jörmungandr was forged by the primordial frost and fire at the dawn of the world, a "
                    "being so immense that it encircles the entire Earth, grasping its own tail. Legends speak"
                    " of Jörmungandr being the offspring of Loki and the giantess Angerboda, its body stretching"
                    " across the cosmos, its presence a dark reminder of the world’s primordial chaos. As it slumbers"
                    " beneath the ocean, its restless movements are said to cause tremors and upheavals. The"
                    " serpent's very existence is tied to the fate of the world; its emergence will signal the onset"
                    " of Ragnarök, the apocalypse, where it will rise from the depths to flood the Earth and battle Thor"
                    " in a cataclysmic clash. Jörmungandr’s gaze, if one could ever meet it, is said to invoke profound despair,"
                    " reflecting the end times and the inescapable fate of all things."),
                    "The world serpent, the serpent of midgard, the serpent of the deep JÖRMUNGANDR!",
                   "it",
                   100
                   )

chronos = Boss("Chronos",
               1000,
               10,
               ("Cronus, also known as Chronos, is a primordial deity in Greek mythology, embodying the relentless passage of "
                "time and the inevitable decay that accompanies it. As the leader of the Titans, he overthrew his father Uranus"
                " to establish his own reign. However, his rule was marked by paranoia and tyranny, driven by a prophecy that he"
                " would be overthrown by one of his own children. To prevent this, Cronus devoured each of his offspring at birth"
                ". His cruel acts of consuming his children symbolized his attempt to control and contain the inexorable flow of "
                "time and fate. In a dark twist of myth, Cronus was eventually tricked by his wife, Rhea, who saved their youngest"
                " son, Zeus, and allowed him to grow up in secret. Zeus would later lead a rebellion against Cronus, culminating in"
                " a catastrophic battle that ended Cronus’s reign and cast him into the depths of Tartarus. Despite his defeat,"
                " Cronus’s influence endures as the embodiment of time’s dark, consuming nature, and his name is often invoked"
                " as a symbol of unyielding fate and the inevitability of decline."),
                "The titan king, the devourer of time, the time eater CHRONOS!",
                "him",
                100) 


bossArray = [dracula, cthulhu, medusa, banshee, jörmungandr, chronos]

# The goal is to eventually have a roster of bosses from which the user can pick to fight
# with different bosses having different playstyles.

# Only Cthulhu is in use at the moment as there doesnt exist an option for multiple bosses in the main
# file as of yet
