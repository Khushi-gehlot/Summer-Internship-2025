import random
scoreHuman = 0
scoreComp = 0

while True:
    ch = input('''Enter your choice:
    1. Rock
    2. Paper
    3. Scissor
    4. Exit
    ''')
    print("Your choice =",ch)
    ch2 = random.choice(["Rock", "Paper", "Scissor"])
    print("Computer choice =",ch2)
    ch = ch.strip().title()

    if ch not in ["Rock", "Paper", "Scissor", "Exit"]:
        print("Invalid choice")
    else:
        if ch == "Exit" :
            break
        elif ch == ch2:
            print("Draw\n\n")

        elif ch == "Rock" and ch2 == "Scissor" or ch == "Paper" and ch2 == "Rock" or ch== "Scissor" and ch2 == "Paper":
            print("You win\n\n")
            scoreHuman += 1

        else :
            print("You lose\n\n")
            scoreComp += 1

print("\n\nGame Over", "\nYour score is", scoreHuman, "\nComputer's score is", scoreComp, "\n\n")
if scoreHuman > scoreComp:
    print("You win\n\n")
elif scoreHuman < scoreComp:
    print("Computer wins\n\n")
else:
    print("Match Draw!\n\n")


