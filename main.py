print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
user_name=input("Please Enter Your Full Name:")
print(user_name)
print(f"Welcome {user_name} to treasure island.")
print("Your mission is to find the treasure.")
choice1=input("Please enter your direction where you want to go either 'left' or 'right' : ").lower()
if choice1  == "left" :
    #continue
    choice2=input("What you want to do with it 'swim' or'wait': ").lower() 
    if choice2 == "wait":
       choice3=input("You arrive at the island unharmed .There is a house with 3 door (One red),(One Yellow),(One blue) which colour do you choice?").lower()
       if choice3 =="red":
          print("It's a room full of fire.game over.")
       elif choice3 == "yellow":
          print("You found the treasure!.You Win🏆💰💰")
       elif choice3 == "blue" :
          print("You enter a room of beasts.Game Over.")
       else :   
           print("You choice a door that do not exist.Game Over")
    #continue
    else :
      print("You got attacked by an angry .Game Over")

else :
   print("You fell into a hole .Game Over")