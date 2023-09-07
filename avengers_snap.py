##############################################
#Choose your own adventure story
#Created by: 
#Maysen Wakerley, Garrett Nutting, Tae Lee, and Nick Hoekwater

import random

characters = [
    "Okoye",
    "Iron Man",
    "Captain America",
    "Thor",
    "The Hulk",
    "Black Widow",
    "Spider-Man",
    "Dr. Strange",
    "Black Panther",
    "Peter Quill",
    "Luke Skywalker",
    "Drax",
    "Rocket Racoon",
    "Groot",
    "Mantis",
    "Scarlet Witch",
    "Tony Soprano",
    "Falcon",
    "War Machine",
    "Bucky Barnes"
]
alive_characters = []

# Loop 10 times to get 10 random people
for i in range(0,10):
    character_that_lives = random.choice(characters)
    alive_characters.append(character_that_lives)
    characters.remove(character_that_lives)
    i += 1
    
print("\n\n")
#print("These characters have survived the Infinity War snap", alive_characters)
print("\n\n")


#Introduction to the setting.
print("The Avengers take on Thanos in an epic final battle in Wakanda as a last defense against the Mad Titan")
print("The Avengers cannot keep up with Thanos who now has the power of six infinity stones")

#Script directly pulled from movie describing the last attempt from the Avengers.
print("[The wind picks up. It feels... strange. Eerie.]")
print("\n")
print("Steve Rogers: Everyone, on my position. We have incoming. \n[he is joined by the Black Widow, Falcon, Okoye and the Black Panther in short order.]")
print("\n")
print("Natasha Romanoff: What the hell?")
print("Bruce Banner: [Bruce sees the blue-black clouds of a Space Stone relocation just before Thanos steps forward, and confirms this isn't just another member of the Black Order]\n Cap. That's him.")
print("\n")
print("Steve Rogers: Eyes up. Stay sharp.")
print("\n")
print("Bruce reaches Thanos first, lunging forward fist-first - but Thanos uses the Space Stone on him, renders him immaterial until the Hulkbuster is half-buried in the stone of the cliff behind him, and freezes Bruce in place.]")
print("Captain America is sent flying by purple energy before he even gets to strike a single blow]")
print("The Black Panther, armor fully charged kinetically, leaps high and with claws extended, but is easily grabbed by the throat and punched to the ground, his armor discharging violently]")
print("Falcon stoops, strafing with both Steyr pistols, but is felled when his wings become rubbery and unable to sustain flight.]")
print("\n")
print("[Thanos picks up Vision by the throat, lifting him to eye-level, and digs the fingers of his right hand into Vision's forehead, digging out the Mind Stone. He pulls it loose, and Vision goes limp and colorless; he tosses the lifeless android aside like trash. Bringing his gauntleted hand up, he slowly moves the Mind Stone over the last empty setting, and drops it in. The energy surge is much more than any previous - his torso is wreathed with iridescent static and he bellows from the sensations.]")
print("[As Thanos studies the completed gauntlet, a massive bolt of lighting strikes him, digging him into the ground and grinding him back for meters. Thor has arrived, eyes glowing with power, stooping down from the sky like a bird of prey. The God of Thunder pauses his attack, reverses his position, raises Stormbreaker above his head and hurls it -- Thanos fires the whole might of the gauntlet against it, but it only creates a rainbow-like bowshock, not slowing the axe as it slams right into Thanos' chest. ]")
print("\n")
print("Thor: [lands in front of Thanos, who is down on one knee; hatefully.]\n I told you. You'd die for that!")
print("\n")
print("[He takes hold of the back of Thanos's head and forces Stormbreaker deeper into his chest, staring angrily into his eyes while Thanos cries out in pain]")
print("Thanos: [weakly]\n You should have... \nYou... \n[suddenly stronger] \n\nYou should have gone for the head! \n[He raises his gauntlet and snaps his fingers.]")
print("\n")
print("Thor: NO!")
print("\n")
print("[Now out of the Soul World, Thanos is snapped back to normal reality, and notices the damage inflicted on the gauntlet - the metal scorched and distorted from heat, the stones no longer glowing]")
print("Thor: What'd you do? [angrily] WHAT'D YOU DO?!")
print("\n")
print("\n")

#Run randomizer, see who dies. if statements for dialog for each character who dies.
#Have user input names to see if they died


character = input("Name a character to see if they made it: ")

    #figure out what they say about the ones that died
if character.lower() == "iron man" or character.lower() == "tony":
    
    if "Iron Man" in alive_characters:
        print("He lived!")
        
    else:
        print("Iron Man died!")
        print("final line")
        
elif character.lower() == "thor":
    if "Thor" in alive_characters:
        print("He lived!\n")
        print("Thor: I have failed, what have I done")
    else:
        print("He died!")
        print("See you soon, brother")

elif character.lower() == "captain america" or character.lower() == "cap":
    
    if "Captain America" in alive_characters:
        print("He lived!")
        
    else:
        print("Captain America died!")
        print("final line")
        
elif character.lower() == "hulk" or "bruce": 
    if "Hulk" in alive_characters:
        print("It's over... we lost.")
    else:
        print("What's happpening to me?")

elif character.lower() == "black widow" or "natasha":
    if "Black Widow" in alive_characters:
        print("I can't believe this.")
    else:
        print("This doesn't feel ok.")

elif character.lower() == "spider-man":
    if "Spider-Man" in alive_characters:
        print("I don't think that this is supposed to be happening!")
    else:
        print("Mr. Stark, I don't feel so good.")

elif character.lower() == "dr.strange":
    if "Dr. Strange" in alive_characters:
        print("This is the only way")
    else:
        print("This isn't supposed to happen like this")

elif character.lower() == "black panther":
    if "Black Panther" in alive_characters:
        print("What has this monster done")
    else:
        print("I have failed my people")

elif character.lower() == "peter quill" or character.lower() == "star lord":
    if "Peter Quill" in alive_characters:
        print("Did we win guys?")
    else:
        print("This feels totally uncool!")

elif character.lower() == "drax":
    if "Drax" in alive_characters:
        print("This is so cool.")
    else:
        print("Why am I turning into dust?")

elif character.lower() == "rocket raccoon":
    if "Rocket Raccoon" in alive_characters:
        print("Ok guys, what are we gonna do now?")
    else:
        print("Oh shit")

elif character.lower() == "groot":
    if "Groot" in alive_characters:
        print("I am groot.")
    else:
        print("I am groot.")


############
#   This code below is nonfunctioning. Make sure to check the alive list (just copy the format above)
############

# elif character.lower() == "mantis":
#     print("This is not ok.")
# else:
#     print("I feel so tingly.")

# elif character.lower() == "scarlet witch":
#     print("He took everything from me")
# else:
#     print("How could this happen?")

# elif character.lower() == "falcon":
#     print("Now what?")
# else:
#     print("This is not good.")

# elif character.lower() == "war machine":
#     print("The suit wasn't enough.")
# else:
#     print("Something's happening to me.")

# elif character.lower() == "bucky barnes" or character.lower() == "bucky":
#     print("We failed.")
# else:
#     print("Steve?")
