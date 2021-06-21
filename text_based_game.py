def main():
    print('Welcome to My First Game!')
    start_game()

def start_game():
    health = 10
    name = input('What is your name? ').title() #ask for player's name
    print(f'Welcome {name}!') #print player's name with title case
    age = int(input('What is your age?')) #ask for player's age
    if age >= 18 : #checks if player is old enough to play the game
        print(f'Hey {name}, you are {age} and old enough to play the game!')
        print(f'You are starting with {health} health')
        wants_to_play = input('Do you want to play? ').lower()#ask player if they want to play
        if wants_to_play == 'yes':
            print("Let's play!")
            left_or_right = input('Where do you want to go to? Left or Right? ').lower() #ask player what direction they want to go to
            if left_or_right == 'left': #what happens if player chooses 'left'
                ans = input('Nice, you follow a path and reach a lake... Do you swim across or go around? ').lower() #ask player to make another decision

                if ans == 'around': #what happens if the player chooses 'around'
                    print('You went around reached the other side of the lake.')
                elif ans == 'across':
                    print('You managed to get across but were bit by a fish and lost 5 health')
                    health -= 5
                    print(f'You have {health} health left.')

                ans = input('You notice a house or a river. Which do you go to? ') 
                if ans == 'house': #what happens if player chooses 'house'
                    print('You go to the house and are greeted by the owner. He does not like you and you lose 5 health')
                    health -= 5
                    if health == 0:
                        print('You now have 0 health and you lost the game... ')
                    else:
                        print('You survived...')

                else:
                    print('You fell in the river and lost')

            else:
                 print("You have ended up at a dead end. You lost..!")
        else:
            print('Bye!')
    else:
        print('Ooops! You are not old enough to play...')




if __name__ == '__main__':
    main()