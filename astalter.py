# Alex Stalter
# Only use 1's and 0's in the answer


def win_percentage():
        games_won = 0
        for games in range(12):
            games_won = games_won + (int(input("If you won the game enter a 1 if you lost enter a 0 ")))
        percent_won = games_won/12 * 100
        print("The win percentage is", percent_won, "%")


win_percentage()

