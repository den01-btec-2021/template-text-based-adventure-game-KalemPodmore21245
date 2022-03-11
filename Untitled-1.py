
def main():
    print('Welcome to the game')
    playername = input('what is your name:   ')
    print('Hi', playername)

    lives = 3
    print(f"you have {lives} lives left") 

    Keys = 0
    print("you have", Keys,"keys. You will need 3 to escape ")

    while True:
        print("you have four directions to choose from. either North,South,East or West")
        direction = input('What direction will you go?:    ')

        if direction == 'North':
            print("You Went North")#Need to stop this if already used
            #im trying to make a puzzle and add a lose life function 
            North_puzzle = input("what is 2+2?")
            if North_puzzle == "4":
                print('You got it right!') #need to connect
                Keys += 1
                print("You have collected a key")
            else:
                lives -= 1
                print("You go the puzzle wrong! You loose a life!") 
                print("You have", lives,"lives left")
        elif direction == 'South':
            print('You went South')
            South_puzzle = input("what is 8*5?")
            if South_puzzle == "40":
                print('You got it right!') 
                Keys += 1
                print("You have collected a key")
            else:
                lives -= 1
                print("You go the puzzle wrong! You loose a life!")
                print("You have", lives,"lives left") 
        elif direction == 'West':
            print('You Went West')
            West_puzzle = input("what is 10-4?")
            if West_puzzle == "6":
                print('You got it right!') 
                Keys += 1
                print("You have collected a key")
            else:
                lives -= 1
                print("You go the puzzle wrong! You loose a life!")
                print("You have", lives,"lives left")
        elif direction == 'East':
            print('You went East')
            East_puzzle = input("what is 3+17?")
            if East_puzzle == "20":
                print('You got it right!') 
                Keys += 1
                print("You have collected a key")
            else:
                lives -= 1
                print("You go the puzzle wrong! You loose a life!")
                print("You have", lives,"lives left")
        else:
            print('that is not a correct direction!')
        
        if lives == 0:
            print("YOU ARE DEAD!")
            exit()

        if Keys == 3:
            print("You Have collected all 3 Keys!")
            print("Well done", playername)
            exit()

main()



