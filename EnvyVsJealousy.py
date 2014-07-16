#!/usr/bin/python
#-*- coding: utf-8 -*-

#www.facebook.com/bash3ba
#https://github.com/basheba

from termcolor import colored #learn to add colored text
from datetime import datetime

class color:
   GREEN = '\033[92m'
   BOLD = '\033[1m'
   CYAN = '\033[96m'
   END = '\033[0m'
   MAGNETTA = '\033[95m'
   YELLOW = '\033[93m'

print "\n" * 2
print color.BOLD + color.MAGNETTA +"▁ ▂ ▄ ▅ ▆ ▇ █ BASHEBA █ ▇ ▆ ▅ ▄ ▂ ▁" + color.END
now = datetime.now()
print color.BOLD + color.MAGNETTA + "\nWelcome today is: %s/%s/%s %s:%s:%s " % (now.month, now.day, now.year, now.hour, now.minute, now.second) + color.END

print color.BOLD + color.CYAN + ("JEALOUSY VS ENVY\n").center(100)+ color.END

print """Jealousy is a Satanic ACTION spirit.  Jealousy sets out on a mission to rob one of their joy and 
destroy what makes someone feel happy, or makes them look good, in order to feel good about ONES SELF.\n"""  

print """Envy is a layed back PASSIVE spirit that sprinkles the euphoria of wish.\n"""

print """Below are six scenarios.  Pick the letter [e] for envy or [j] for jealousy.\n"""

print color.BOLD + color.CYAN + "SCENARIO ONE\n" + color.END

print """Tony has a 2016 Lamborgini.  Walter HATES to walk.  Tony rode up to 
Walter and honked the horn toot, toot, and said, 'Hey man, you want a ride'?  Walter 
exclaimed 'WOW DUDE.  I'D KILL FOR A RIDE LIKE THIS, YEAH SURE!\n"""

print ("Type the correct letter 'e' or 'j' to the appropriate response: "), 

input = raw_input()
#also use "if input not in {'e', 'j'}" if the user picks other than e or j is another way instead of a switch

def switch(input):
    return {
        'e': color.BOLD + color.GREEN +"Correct! He wished he had a car like Tony's." + color.END,
        'j': color.BOLD + color.MAGNETTA + "Incorrect.  Walter never set out to hurt Tony." + color.END,
        }.get(input, color.BOLD + color.YELLOW + "That letter was not a valid option.") + color.END

print(switch(input))
print "\nOpen for discussion:\n"

print color.BOLD + color.CYAN + "SCENARIO TWO\n" + color.END

print """Pamela went on a diet and lost 50 pounds.  All the guys wanted to date Pamela and Katie
was worried that she was about to lose her man.  Even though Katie applauded Pamela's new look,
Katie invited Pamela over for some friendly chit chat with cake and coffee.\n"""

print ("Type the correct letter 'e' or 'j' for the appropriate response: "),

input = raw_input()
def switch(input):
    return {
        'e': color.BOLD + color.MAGNETTA + "Incorrect!  Katie had no desire to be like Pamela she just wants to keep her man." + color.END,
        'j': color.BOLD + color.GREEN + "Correct!  Katie wanted to destroy Pamela's looks by offering her cake because Pamela intimidated Katie." + color.END,
        }.get(input, color.BOLD + color.YELLOW + "That letter was not a valid option.") + color.END

print(switch(input))

print "\nOpen for discussion:\n"

print color.BOLD + color.CYAN + "SCENARIO THREE\n" + color.END

print """Sam was assumed to be the richest man in town - a big contributor.  Calvin bought 
a new house and a new truck and increased his business all in the same week.  Calvin was now the
talk of the town.  Sam put flyers all over town disparaging Calvin, so that he would lose his 
business, his money, his car and his new house.\n"""

print ("Type the correct letter 'e' or 'j' for the appropriate response: "),

input = raw_input()
def switch(input):
    return {
        'e': color.BOLD + color.MAGNETTA + "Incorrect!  Sam was assumed to have money." + color.END,
        'j': color.BOLD + color.GREEN +"""Correct! Sam didn't like watching Calvin enjoy his good fortune so he set out
to destroy Calvin.""" + color.END,
        }.get(input, color.BOLD + color.YELLOW + "That letter was not a valid option.") + color.END

print(switch(input))

print "\nOpen for discussion:\n"

print color.BOLD + color.CYAN + "SCENARIO FOUR\n" + color.END

print """Marsha was a secretary at the White House. She received roses every day from
her boe.  Helen was her boss and didn't like watching Marsha, smiling, and smelling and  
dancing with her roses, so she fired Marsha out of her sight.\n"""

print ("Type the correct letter 'e' or 'j' for the appropriate response: "),

input = raw_input()
def switch(input):
    return {
        'e': color.BOLD + color.MAGNETTA + "Incorrect!  Helen was jealous of how the flowers made Martha feel." + color.END,
        'j': color.BOLD + color.GREEN +"""Correct! Helen was jealous of Marsha's glee and went after her job.""" + color.END, 
        }.get(input, color.BOLD + color.YELLOW + "That letter was not a valid option.") + color.END

print(switch(input))

print "\nOpen for discussion:\n"

print color.BOLD + color.CYAN + "SCENARIO FIVE\n" + color.END

print """Joel was a straight A student, and with one more exam to go for the record, the class cheered Joel on.  Stan hacked into the school's computer and changed Joel's grade to a 'D'.\n"""

print ("Type the correct letter 'e' or 'j' for the appropriate response: "),

input = raw_input()
def switch(input):
    return {
        'e': color.BOLD + color.MAGNETTA + "Incorrect!  Stan was a pot head, and didn't care to make the same grade as Joel." + color.END,
        'j': color.BOLD + color.GREEN +"Correct! Stan felt jealous of Joel's victory and attention." + color.END,
        }.get(input, color.BOLD + color.YELLOW + "That letter was not a valid option.") + color.END

print(switch(input))

print "\nOpen for discussion:\n"

print color.BOLD + color.CYAN + "SCENARIO SIX\n" + color.END

print """Jackie thought Sheila was the most beautiful girl she had ever seen and couldn't stop 
staring at her.  Jackie went home and fixed her hair the way Sheila had hers, and patterened 
her lifestyle after the manner of Sheila.\n"""

print ("Type the correct letter 'e' or 'j' for the appropriate response: "),

input = raw_input()
def switch(input):
    return {
        'e': color.BOLD + color.GREEN + "Correct!  Jackie wanted to be just like Shiela." + color.END,
        'j': color.BOLD + color.MAGNETTA +"Incorrect!  Jackie never set out to hurt Shiela." + color.END,
        }.get(input, color.BOLD + color.YELLOW + "That letter was not a valid option.") + color.END

print(switch(input))