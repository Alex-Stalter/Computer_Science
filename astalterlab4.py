""" Written by Alex Stalter
"""


def main():
    # The following inputs take in the users inputs for the situation that they desire to find the probability of
    activity = input("Please enter the activity you would like to test the probability of: ")
    probability = float(input("Please enter the probability of one event(Enter a Decimal) : "))
    # For desired win the loss probability that the user wants must be entered
    desired_win = float(input("Please enter the minimum threshold for one favorable event happening"
                              " (Enter a whole Number) : "))/100
    '''The Losing probability variable changes the imputed probability of winning into the chance of the user losing in
    order to multiply the probability by itself and find the desired win rate 
    '''
    losing_prob = 1-probability
    times_played = 0
    # This while loop calculates the probability of winning after a certain amount of events.
    while losing_prob > desired_win:
        losing_prob = 1 - probability
        times_played = times_played + 1
        losing_prob = losing_prob ** times_played
        '''This print function utilizes the f string characteristic in order to make the code more readable and easier
        to work with'''
    print(f"For your activity of {activity} with a probability of success of {probability} for each event")
    print(f"you will have to have {times_played} events to have a {desired_win * 100}% ")
    print(f"chance of winning in one of the {times_played} events ")


main()
