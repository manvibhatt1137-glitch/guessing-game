import random


def main():
    print("let's start the game")
    attempts =10
    num = random.randint(1,99)
    score = 10
    while attempts!= 0:     
        input = input('guess the number')
        
        print(attempts)
        if num>input:
            print('too low')
            attempts-=1
        elif num<input :
            print('too high')
            attempts-=1
        else :
            break


        

    

    # TODO: Features 
    # use loop
    # take input for finishing the game
    # take input for hint question 
    # add scoring mechanism 

    # TODO: Refactor
    # extract classes
    # use separate files



