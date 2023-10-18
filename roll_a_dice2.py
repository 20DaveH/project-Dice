import random

#response = input("Would you like to roll the dice, please answer yes/no: ")

response = "yes"
  
while response == "yes":
    no = random.randint(1,6)

   
    if no == "1":
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
            print("")
            print("Do you want to roll the dice again?")

    if no == "2":
            print("[-----]")
            print("[  0  ]")
            print("[     ]")
            print("[  0  ]")
            print("[-----]")
            print("")
            print("Do you want to roll the dice again?")

    if no == "3":
            print("[-----]")
            print("[ 0   ]")
            print("[  0  ]")
            print("[   0 ]")
            print("[-----]")
            print("")
            print("Do you want to roll the dice again?")

    if no == "4":
            print("[-----]")
            print("[ 0 0 ]")
            print("[     ]")
            print("[ 0 0 ]")
            print("[-----]")
            print("")
            print("Do you want to roll the dice again?")

    if no == "5":
            print("[-----]")
            print("[ 0 0 ]")
            print("[  0  ]")
            print("[ 0 0 ]")
            print("[-----]")
            print("")
            print("Do you want to roll the dice again?")

    if no == "6":
            print("[-----]")
            print("[ 0 0 ]")
            print("[ 0 0 ]")
            print("[ 0 0 ]")
            print("[-----]")
            print("")
            print("Do you want to roll the dice again?")