import random 
def words():
    l=["Rock","Paper","Seasor"]
    word=''.join(random.choice(l))
    return word
def users(user):
    if user=="s":
        return 'Seasor'
    elif user=="p":
        return "Paper"
    elif user=="r":
        return "Rock"
def decisions(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "Draw",0,0
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!",1,0
    else:
        return "Computer wins!",0,1
user_points=0
computer_points=0
while True:
    user=input("Enter your choice (s for scissors, p for paper, r for rock): ").lower()
    user_choice=users(user)
    if user_choice is None:
        print("Invalid input. Please enter 's', 'p', or 'r'.")
        continue
    print("your choice is: ",user_choice)
    computer_choice=words()
    print("Computer choice is: ",computer_choice)
    result,user_point, computer_point=decisions(user_choice,computer_choice)
    print(result)
    user_points += user_point
    computer_points += computer_point
    
    print("Points Table:")
    print("You:", user_points)
    print("Computer:", computer_points)
    quit=input("any key for Continue or q for Quit the game: ")
    if quit=="q":
        print('Final point table: ')
        print("You:", user_points)
        print("Computer:", computer_points)
        if user_points>computer_points:
            print("YOU WON THE GAME !!")
        else:
            print("COMPUTER WON THE GAME :(")
        break
    else:
        continue   
