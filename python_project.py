import functools
import array as arr
import os
import csv
import pandas as pd
import time 
import logging
import datetime
from time import sleep

ENDC = '\033[0m'
FG_GREEN = '\033[32m'
FG_RED = '\033[31m'
FG_BLUE = '\033[34m'
FG_BLACK = '\033[30m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BOLD = '\033[1m'

log = open("game_log.txt", mode = "a", encoding = "utf-8")

right = 0
wrong = 0

print("What is your name?")
global name
name = input()

def game_start():
  print("Shall we begin the game? ")
  start = input()
  start = start.lower()
  if start == "yes":
    print(" ")
    print(FG_GREEN + "Downloading files.,.," + ENDC)
    print("----------------------------------------------")
    sleep(3)
    print(FG_RED + "Vreifiyngf ilse!..,," + ENDC)
    print("----------------------------------------------")
    sleep(3)
    print(FG_RED + "ilFeer rr!o!,,.." + ENDC)
    print("----------------------------------------------")
    sleep(3)
    print(FG_RED + "nErcpyitnoe rrro,.,." + ENDC)
    print("----------------------------------------------")
  else:
    game_start()

game_start()


def help_one():
  print(FG_RED + "Crorutp flie..,,tpye kaayt o ocntniue" + ENDC)
  sleep(2)
  print(" ")
  print(FG_BLUE + "Hey, this is your local computer talking to you." + ENDC)
  sleep(4)
  print(" ")
  print(FG_BLUE + "I am not sure what files you were trying to pull, but our encryption key doesn't match the server you pulled from." + ENDC)
  sleep(2)
  print("")
  print(FG_BLUE + "I'll display what I received, but I don't think the information will be in the right order. The key seems to scramble in character blocks of 4." + ENDC)
  sleep(4)
  print(" ")
  print(FG_BLUE + "You're going to have to figure out the right order of each character in the question." + ENDC)
  sleep(1)
  print(FG_BLUE + "Then, you'll have to answer the question correctly with your response scrambled in the same order as the question so the server can read your answer." + ENDC)
  sleep(1)
  print(FG_BLUE + "Only then would I be able to learn the key to unscramble the message for you." + ENDC)
  sleep(6)
  print(" ")
  print(FG_BLUE + "I can get this first one for you, but you'll be on your own for the rest" + ENDC)


help_one()

def local_one():
  sleep(1)
  print(" ")
  print(FG_GREEN +"Corrupt file.,.,type okay to continue" + ENDC)
  answer = input()
  answer = answer.lower()
  if answer == "okay":
    print(FG_BLUE + "Goodluck!" + ENDC)
  else:
    print(FG_BLUE + "Look, I don't blame you buddy, but we've got to get to the bottom of this" + ENDC)
    local_one()

local_one()


def riddle_one():
  sleep(1)
  print(FG_RED + "Waht si 1÷26..,," + ENDC)
  answer = input()
  if answer == "2":
    global right
    right += 1
    sleep(1)
    print(FG_GREEN + "Croretc!" + ENDC)
  else:
    global wrong
    wrong += 1
    sleep(1)
    print(FG_RED + "Icnorerct!!!" + ENDC)
    riddle_one()

riddle_one()
sleep(1)
print(" ")
print(FG_BLUE + "NICE! I think I have 1/3 of the key figured out! Let's figure out more." + ENDC)
print(" ")


def riddle_two():
  sleep(1)
  print(FG_RED + "h Woi ddh teliAlsfe gtihaa gntisi  nWIWI,,.." + ENDC)
  answer = input()
  answer = answer.lower()
  if answer == "xsai":
    global right
    right += 1
    sleep(1)
    print(FG_GREEN + "orCrc!et" + ENDC)
  else:
    global wrong
    wrong += 1
    sleep(1)
    print(FG_RED + "noIcrcre!!t!" + ENDC)
    riddle_two()

riddle_two()
sleep(1)
print(" ")
print(FG_BLUE + "THAT'S IT! 2/3 of the key figured out. Keep it up!" + ENDC)
print(" ")

def riddle_three():
  sleep(1)
  print(FG_RED + "hWtac nab ti,eb tuh san  oette?hW ah tac nohlw ,ub tah sonv ioec??,.,." + ENDC)
  answer = input()
  answer = answer.lower()
  if answer == "iwdn":
    global right
    right += 1
    sleep(1)
    print(FG_GREEN + "oCrrce!t" + ENDC)
  else:
    global wrong
    wrong += 1
    sleep(1)
    print(FG_RED + "nIocrrce!t!!" + ENDC)
    riddle_three()

riddle_three()
sleep(1)
print(" ")
print(FG_BLUE + "You did it! We have the key!" + ENDC)
sleep(2)
print(" ")
print(FG_BLUE + "Give me a couple seconds." + ENDC)
sleep(4)
print(" ")
print(FG_BLUE + "5A1k28Y3c6. There's our key." + ENDC)
sleep(1)
print(" ")
print(FG_BLUE + "Nice work, but we aren't in the clear yet. We got the message from a source that was using Frequency Hopping." + ENDC)
sleep(2)
print(" ")
print(FG_BLUE + "I am going to display a table that displays the frequencies being watched and at what time slot they are watched at." + ENDC)
sleep(2)
print(FG_BLUE + "I need you to figure out what order of frequencies I must listen to using the key, 5A1k28Y3c6, to figure out the order. " + ENDC)
sleep(3)



def riddle_four():
  print(" ")
  print(BG_GREEN + BOLD + "---3.0MHz--3.5MHz--4.0MHz--4.5MHz--5.0MHz--5.5MHz--6.0MHz--6.5MHz--7.0MHz--7.5MHz---" + ENDC)
  print(" ")
  print(BG_GREEN + BOLD + "---.001----.002----.003----.004----.005----.006----.007----.008----.009----.010---" + ENDC)
  print(BG_GREEN + BOLD + "-----5-------------------------------------------------------3--------------------" + ENDC)
  print(BG_GREEN + BOLD + "---.010----.001----.002----.003----.004----.005----.006----.007----.008----.009---" + ENDC)
  print(BG_GREEN + BOLD + "-----------------------------1----------------------------------------------------" + ENDC)
  print(BG_GREEN + BOLD + "---.009----.010----.001----.002----.003----.004----.005----.006----.007----.008---" + ENDC)
  print(BG_GREEN + BOLD + "---------------------------------------------k------------------------------------" + ENDC)
  print(BG_GREEN + BOLD + "---.008----.009----.010----.001----.002----.003----.004----.005----.006----.007---" + ENDC)
  print(BG_GREEN + BOLD + "----------------------------------------------------------------------------------" + ENDC)
  print(BG_GREEN + BOLD + "---.007----.008----.009----.010----.001----.002----.003----.004----.005----.006---" + ENDC)
  print(BG_GREEN + BOLD + "---------------------c------------------------------------------------------------" + ENDC)
  print(BG_GREEN + BOLD + "---.006----.007----.008----.009----.010----.001----.002----.003----.004----.005---" + ENDC)
  print(BG_GREEN + BOLD + "-------------Y---------------------------------------A-----------------------2----" + ENDC)
  print(BG_GREEN + BOLD + "---.005----.006----.007----.008----.009----.010----.001----.002----.003----.004---" + ENDC)
  print(BG_GREEN + BOLD + "----------------------------------------------------------------------------------" + ENDC)
  print(BG_GREEN + BOLD + "---.004----.005----.006----.007----.008----.009----.010----.001----.002----.003---" + ENDC)
  print(BG_GREEN + BOLD + "----------------------------------------------------------------------------------" + ENDC)
  print(BG_GREEN + BOLD + "---.003----.004----.005----.006----.007----.008----.009----.010----.001----.002---" + ENDC)
  print(BG_GREEN + BOLD + "----------------------------------------------------------------------------------" + ENDC)
  print(BG_GREEN + BOLD + "---.002----.003----.004----.005----.006----.007----.008----.009----.010----.001---" + ENDC)
  print(BG_GREEN + BOLD + "-------------------------------------8-------------------------------6------------" + ENDC)
  print("")
  print(FG_BLUE + "Input your answers as a decimal. No need to add the MHz, I'll handle that. KEY= 5A1k28Y3c6" + ENDC)
  sleep(1)
  print("Freq 1")
  Freq1 = input()
  print("Freq 2")
  Freq2 = input()
  print("Freq 3")
  Freq3 = input()
  print("Freq 4")
  Freq4 = input()
  print("Freq 5")
  Freq5 = input()
  print("Freq 6")
  Freq6 = input()
  print("Freq 7")
  Freq7 = input()
  print("Freq 8")
  Freq8 = input()
  print("Freq 9")
  Freq9 = input()
  print("Freq 10")
  Freq10 = input()
  FreqOrder = [Freq1, Freq2, Freq3, Freq4, Freq5, Freq6, Freq7, Freq8, Freq9, Freq10]
  if FreqOrder == ["3.0", "6.0", "4.5", "5.5", "7.5", "5.0", "3.5", "6.5", "4.0", "7.0"]:
    global right
    right += 1
    sleep(1)
    print(FG_BLUE + "You did it!" + ENDC)
  else:
    global wrong
    wrong += 1
    sleep(1)
    print(FG_BLUE + "I dont think that is it" + ENDC)
    riddle_four()


riddle_four()

print(" ")
sleep(2)
print(FG_BLUE + "Well my friend, I think we have figured out all of our issues! So let's try this again from the start." + ENDC)
sleep(1)
print(" ")

def game_start2():
  print("Shall we begin the game? " + ENDC)
  start = input()
  start = start.lower()
  if start == "yes":
    print(" ")
    print(FG_GREEN + "Downloading files.,.," + ENDC)
    print("----------------------------------------------")
    sleep(3)
    print(FG_GREEN + "Verifying files.,.," + ENDC)
    print("----------------------------------------------")
    sleep(3)
    print(FG_GREEN + "Files decrypted.,.," + ENDC)
    print("----------------------------------------------")
    sleep(3)
    print(FG_GREEN + "Transfer complete.,.," + ENDC)
    print("----------------------------------------------")
  else:
    game_start2()

game_start2()



sleep(2)
print(" ")
print(" ")
print(FG_BLACK + BG_RED + BOLD + "--------------------------------------------------" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|                                                |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|                                                |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|      /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\        |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |                                  |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |                                  |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |       \                  /       |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |        \    /      \    /        |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |         \__/        \__/         |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |         | .|        |. |         |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |         |__|        |__|         |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |                                  |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |                                  |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |                 \                |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |                __\               |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |                                  |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |           _____________          |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |          /             \         |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |         /               \        |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |        /                 \       |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |                                  |       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|     |__________________________________|       |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|                                                |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "|                                                |" + ENDC)
print(FG_BLACK + BG_RED + BOLD + "--------------------------------------------------" + ENDC)
sleep(2)
print(" ")
print(" ")
print(FG_RED + "You aren't supposed to be able to connect to me." + ENDC)
print("")
print("")
log.write(f'{name} got {wrong} incorrect answers, but solved {right} riddles correctly.')
log.close()
print("")
print("")
sleep(2)


