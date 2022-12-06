import random
your_score=0
computer_score=0
while True:
    possible=["rock","paper","scissor"]
    user=input("Enter your choise: (rock, paper, scissor): ")
    computer=random.choice(possible)
    print("user:",user)
    print("computer:",computer)
    if user == computer:
        print(f"you and computer have selected {user}, it's tie!")
    elif user == "rock":
        if computer == "scissor":
            print("you win! rock smashes scissor")
            your_score+=1
        else:
            print("you lose! paper covers rock")
            computer_score+=1

    elif user == "paper":
        if computer == "rock":
            print("you win! paper covers rock")
            your_score+=1
        else:
            print("you lose! scissor cuts paper")
            computer_score+=1

    elif user == "scissor":
        if computer == "paper":
            print("you win! scissor cuts paper")
            your_score+=1
        else:
            print("you lose! rock smashes scissor")
            computer_score+=1
        
    play_again=input("play again(y/n): ")
    if play_again.lower()!="y":
        break
if your_score==computer_score:
    print("it's tie!")
    print("user",your_score)
    print("computer",computer_score)

if your_score<computer_score:
    print("you lose!")
    print("user",your_score)
    print("computer",computer_score)
    
if your_score>computer_score:
    print("you win!")
    print("user",your_score)
    print("computer",computer_score)