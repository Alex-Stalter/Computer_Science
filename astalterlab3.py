""" This code was written by Alex Stalter
"""
import random


def main():
    # This code asks for the three names of the players of the game
    contestant_one = input("Please enter the name of the first contestant ")
    contestant_two = input("Please enter the name of the second contestant ")
    contestant_three = input("Please enter the name of the third contestant ")
    # This print function informs the user of what is going on in the game
    print("I'm thinking of a number - You guess what it is.")
    # random number uses the random library to generate a pseudo random number form 1-100
    random_number = random.randint(1, 100)
    # The guess variables take in each players guess and convert it to a integer.
    guess_one = int(input("%s what do you think the number is? " % contestant_one))
    guess_two = int(input("%s what do you think the number is? " % contestant_two))
    guess_three = int(input("%s what do you think the number is? " % contestant_three))
    '''The distance variables calculate the distance between the random number and the guess and then find 
    the absolute value of the guess in order to compare the distances.
    '''
    distance_one = abs(guess_one-random_number)
    distance_two = abs(guess_two - random_number)
    distance_three = abs(guess_three - random_number)
    '''These if statements find the lowest number and declare that player the winner but if there is a tie that 
    is closer than the third guess the system will pring out the number and that it is a tie.'''
    if distance_one < distance_two and distance_one < distance_three:
        print("%s was the is the winner the number was %d " % (contestant_one, random_number))
    elif distance_three < distance_two and distance_three < distance_one:
        print("%s was the is the winner the number was %d " % (contestant_three, random_number))
    elif distance_two < distance_one and distance_two < distance_three:
        print("%s was the is the winner the number was %d " % (contestant_two, random_number))
    elif distance_one == distance_two or distance_one == distance_three:
        print("It is a tie there the number was %d" % random_number)


main()
