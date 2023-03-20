# 1. über die console eine eingabe zu definieren (S,T,P)
# 2. zufällige computer auswahl, und dann sehen wer gewinnt.
import random

userInput = input("Schere (SC), Stein (ST), Papier (P)")
computerRandom = random.randint(1,3)

if computerRandom == 1:
    computerInput = "SC" # Schere

if computerRandom == 2:
    computerInput = "ST" # Stein

if computerRandom == 3:
    computerInput = "P"  # Papier

#########################################################
### Computer nimmt SCHERE ###
if computerInput == "SC" and userInput == "SC":
    print("Unentschieden!")

if computerInput == "SC" and userInput == "ST":
    print("User gewinnt!")

if computerInput == "SC" and userInput == "P":
    print("Computer gewinnt!")

#########################################################
### Computer nimmt STEIN ###
if computerInput == "ST" and userInput == "SC":
    print("Computer gewinnt!")

if computerInput == "ST" and userInput == "ST":
    print("Unentschieden!")

if computerInput == "ST" and userInput == "P":
    print("User gewinnt!")

#########################################################
### Computer nimmt PAPIER ###
if computerInput == "P" and userInput == "SC":
    print("User gewinnt!")

if computerInput == "P" and userInput == "ST":
    print("Computer gewinnt!")

if computerInput == "P" and userInput == "P":
    print("Unentschieden")

print("Computer hat gewählt", computerInput)
