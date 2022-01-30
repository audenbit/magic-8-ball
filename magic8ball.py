## By Fiad Muntakim ##
# Magic 8 Ball Game #

import random
import sys
import time

answers = [
    "It is certain",
    "Don't count on it.",
    "Signs point to yes.",
    "Very doubtful.",
    "Reply hazy, try again.",
    "Concentrate and ask again.",
    "My reply is no.",
    "My sources say no.",
    "Outlook good.",
    "Outlook not so good.",
    "The future tells me no.",
    "I cannot answer, you are on your own.",
]

game_title = """
 d8~~\       888                 888 888 
C88b  |      888-~88e    /~~~8e  888 888 
 Y88b/  ____ 888  888b       88b 888 888 
 /Y88b       888  8888  e88~-888 888 888 
|  Y88D      888  888P C888  888 888 888 
 \__8P       888-_88"   "88_-888 888 888 

   __          ____         __
  / /  __ __  / _(_)__ ____/ /
 / _ \/ // / / _/ / _ `/ _  / 
/_.__/\_, / /_//_/\_,_/\_,_/  
     /___/                                                                          
"""
print(game_title)


time.sleep(2)

name = input(
    "\nWelcome to the magical 8-ball game... First of all, what is your name? "
)


def question_ask():
    print("\nOk " + name + ", what is the question you want to ask?\n")


question_ask()


def question_input():
    input(": ")


def replay():
    replay_question = input("Do you wish to play again? [Y/n] ")

    if replay_question == "Y":
        question_ask()
        question_answer()

    if replay_question == "y":
        question_ask()
        question_answer()

    elif replay_question == "n":
        print("Have a nice day!")
        sys.exit()

    elif replay_question == "N":
        print("Thanks for playing, Have a nice day!")
        sys.exit()


def question_answer():
    while True:

        question_input()

        holy_grail = random.choice(answers)  # chooses random answer from answers dict.

        print(holy_grail)  # prints the all mighty holy grail!! (the answer)

        # redo the question input if the holy grail decides that they do not understand
        if holy_grail == "Concentrate and ask again.":
            print("try again")
            continue

        if holy_grail == "Reply hazy, try again.":
            continue

        if holy_grail == "Very doubtful.":
            print("try again")
            continue

        replay()  # brings up prompt to replay the game


question_answer()  # gives the prompt and gives the holy answer

# hope you enjoyed my first non hello world program
