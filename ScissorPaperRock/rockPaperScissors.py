
import os 
import random

os.system("cls")

def play_rps():
    userInput = input("""Enter 'r' for Rock, 'p' for Paper and 's' for scissor: """)
    userInput.lower()
    computer_choice = random.choice(["p", "r", "s"])
    
    # this dictionary is used in the code to get full name instead of getting " 'r', 'p' or 's' " while printing the result
    rps_dict = {"p": "paper",
                "r": "rock",
                "s" : "scissor" }
    
    
    while userInput != computer_choice:        
        
        
        if userInput == "r" and computer_choice == "p":
            print(f"computer chose {rps_dict.get(computer_choice)} you lost! ")
            break
            
        elif userInput == "s" and computer_choice == "r":
            print(f"computer chose {rps_dict.get(computer_choice)} you lost! ")
            break
            
        elif userInput == "p" and computer_choice == "s":
            print(f"computer chose {rps_dict.get(computer_choice)} you lost! ")
            break        
                    
        else:
            print(f"computer chose {rps_dict.get(computer_choice)} you won! ")
            break  

# if the choice of user and the computer is the same than it will print result as draw
    if computer_choice == userInput:
        print(f"computer chose {rps_dict.get(computer_choice)} its A Draw. ")
        

play_rps()
    
