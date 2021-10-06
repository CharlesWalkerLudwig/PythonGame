from random import randint
score = 0;
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] 

def colorGame():
    index = randint(0,len(rainbow)-1)
    answer = input("Which color do you choose?: ")
    while True:
        if answer != rainbow[index]:
            print("Please try again")
            answer = input("Please choose another color?: ")
            print(["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
        else:
            break
        
    print("The random color was: " + rainbow[index])

encore = 'yes'

while encore == "Yes".lower():
    score += 1;
    colorGame()
    print('Would you want to play again? Please write "Yes" or "No"')
    print("Your score is: " + str(score))
    encore = input()
    
    if encore == "No".lower():
        print("Thank you for playing!")
        print("Your score is: " + str(score))

