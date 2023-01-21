from random import randint 
from termcolor import colored
from colorama import init
import requests
import os
import time
init(autoreset=True)

RED = "\033[1;31;40m"
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m"
black = "\033[0;30m"
black = "\033[0;90m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"

emotionModelID = "de57643d-1deb-47d9-9a27-893ddd9b365c"

baseURL = "https://aicode101.com"
api = {
    "classify": "%s/api/model/%s/classify"%
    (baseURL, emotionModelID)
    }

def classify_text(term):
    httpResponse = requests.get(
        api['classify'],
        json = {'term': term}
        )
    response = httpResponse.json()
    return response['label'], response['confidence']

fortunes = ["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.", "A fresh start will put you on your way.", "A friend asks only for your time not your money."]
facts = ["Superman didn't always fly.", "The first computer was invented in the 1940s.", "Space smells like seared steak.", "The longest wedding veil was the same length as 63.5 football fields.", "The unicorn is the national animal of Scotland.", "Bees sometimes sting other bees."]
emojis = ["( ͡° ͜ʖ ͡°)", "¯\_(ツ)_/¯", "ᕦ(ò_óˇ)ᕤ", "(͡ ͡° ͜ つ ͡͡°)", "ʕ•ᴥ•ʔ", "(◕ᴥ◕)"]
gamesuggestions = ["PUBG MOBILE", "Call of Duty: Mobile", "Game of Thrones: Beyond the Wall.", "Tom Clancy's Elite Squad", "Minecraft: Pocket Edition", "Stranger Things: The Game", " Krunker.io.", "Shell Shockers.", "Slither.io.", "Worms.Zone.", "Wormate.io.", "Zombs Royale (ZombsRoyale.io)", "War Brokers (.io)", "Surviv.io (Survivio)"]
gamesuggestionsmobile = ["PUBG MOBILE", "Call of Duty: Mobile", "Game of Thrones: Beyond the Wall.", "Tom Clancy's Elite Squad", "Minecraft: Pocket Edition", "Stranger Things: The Game"]
gamesuggestionsonline =  [" Krunker.io.", "Shell Shockers.", "Slither.io.", "Worms.Zone.", "Wormate.io.", "Zombs Royale (ZombsRoyale.io)", "War Brokers (.io)", "Surviv.io (Survivio)"]
moviesuggestions = ["The Shawshank Redemption (1994)", " The Godfather (1972)", "The Godfather: Part II (1974)", " The Dark Knight (2008)"]
activities = ["bike ride", "jog", "walk"]
shortactivities = ["a quick walk or jog", "a work/schoolwork session outside", "a stroll in your backyard."]

start = ""


name = input("What is your name?\n")
print("hello " + name.capitalize() + ", I am basic chatbot")
print("Type list to see a complete list of my capabilities.")


while start == "":
 fortune = fortunes[randint(0,4)]
 fact = facts[randint(0,5)]
 emoji = emojis[randint(0,5)]
 gamesuggest = gamesuggestions[randint(0, 13)]
 gamesuggestmobile = gamesuggestionsmobile[randint(0, 5)]
 gamesuggestonline = gamesuggestionsonline[randint(0, 7)]
 moviesuggest = moviesuggestions[randint(0, 3)]
 activity = activities[randint(0, 2)]
 shortactivity = shortactivities[randint(0, 1)]
 blue = colored(' Type a function:', 'green', attrs=['blink'], )
 print(blue) 
 function = input(RED).lower().strip()
 

 if function == "fortune": 
  print(fortune)
  continue
 elif function == "end":
   print("Goodbye, please come back soon!")
   break
 if function == "list":
    print("\n current usable functions:\n \n Fortune \n End \n List \n Hello \n Fact \n Textface \n Birthday \n Game \n Gamemobile \n Gameonline \n Movie \n Help \n Whoareyou \n Luckynumber \n Task \n Calculator \n Destroy \n Moodmeter \n Clear \n dice \n")
    continue
 if function == "hello":
   print("Hello " + name.capitalize() +"!")
   continue
 if function == "fact":
   print(fact)
   continue
 if function == "textface":
   print(emoji)
   continue
 if function == "birthday":
   print("Happy Birthday to You \n Happy Birthday to You \n Happy Birthday Dear " + name.capitalize() + " \n Happy Birthday to You. \n From good friends and true, \n From old friends and new,  \n May good luck go with you, \n And happiness too.")
   continue
 if function == "game":
   print(gamesuggest + " is a good game to play.")
   continue
 if function == "gamemobile":
   print(gamesuggestmobile + " is a good mobile game to play.")
   continue
 if function == "gameonline":
   print(gamesuggestonline + " is a good online game to play.")
   continue
 if function == "movie":
   print(moviesuggest + " has good ratings on ImDB.")
   continue
 if function == "help":
   print("Oh no! what do you need help with? \n Type bug for a error or type sad for a bad experience.")
   helper = input()
   if helper == "bug":
     print("Contact our team @Ace46/.EX.\@gmail.com to report the bug.")
     continue
   elif helper == "sad":
     print("We are sorry for the bad experience, contact us @Ace46/.EX.\@gmail.com.")
     continue
 if function == "whoareyou":
    print("I am ＯＶＥＲＬＯＲＤ, a fun Command Line.")
    continue
 if function == "luckynumber":
    number = str(randint(0,10000000000000001))
    print( number + " is your lucky number!")
    if number > str(10000000000000000):
      print("More like your lucky serial number. *snort*")
      continue
 if function == "task":
      print("You have discoverd the task function!")
      day = input("Is it a weekend? ").strip().lower()
      if day == "yes":
        print("Ok, then maybe you have time for a " + activity + "!")
        continue
      else:
       print("Oh, then maybe you can do " + shortactivity + ".")
       continue
 if function == "calculator":
    types = input("type what method of math you are using: (E.X: add, multiply, e.t.c) ")
    if types == str:
      print("Error 404")
      break
    if types == "add":
     num1 = int(input(" Enter a addend: "))
     num2 = int(input(" Enter another addend: "))
     answer = num1 + num2
     print("Your answer is: ", answer)
     continue
    if types == "multiply":
     num1 = int(input(" Enter a multiplicand: "))
     num2 = int(input(" Enter another multiplicand: "))
     answer = num1 * num2
     print("Your answer is: ", answer)
     continue
    if types == "divide":
     num1 = int(input(" Enter a dividend: "))
     num2 = int(input(" Enter another divisor: "))
     print("Your answer is: ", num1 / num2)
     continue
    if types == "subtract":
     num1 = int(input(" Enter an addend: "))
     num2 = int(input(" Enter another addend: "))
     answer = num1 - num2
     print("Your answer is: ", answer)
     continue
 if function == "destroy":
   print("\n" * 10000000)
   continue 
 if function == "moodmeter":
   print("How are you feeling?")
   x = input()
   label, confidence = classify_text(x)
   print(x + "; classified to: " + label +" with " + str(confidence) + "% confidence.")
   continue
 if function == "clear":
    os.system('clear')
    continue
 if function == "dice":
   os.system("clear")
   input("press enter to roll ").lower().strip()
   c_dice = randint(1,6)
   dice = randint(1,6)
   print(cyan,"you rolled a",dice )
   print(cyan,"the computer rolled a",c_dice )
   if c_dice > dice:
     print(red,"you rolled less than the computer. you lose")
     continue
   if c_dice == dice:
     print(yellow,"you rolled the same than the computer. you tied")
     continue
   if c_dice < dice:
     print(green,"you rolled more than the computer. you win")
     time.sleep(5)
     os.system('clear')
     continue    
 else:
  print("I can't do that yet.")
