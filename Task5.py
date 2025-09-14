# Task 5 FIFA World Cup
# With 9 FIFA World Cup wins between them, Brazil and Italy two of
# the most successful soccer countries in the world. Write a program
# that works out who won their latest soccer match, given the scores
# of both teams.

def main():
    #Write your code here
     italyscore = int(input('Italy: '))
    brazilscore = int(input('Brazil: '))
    if italyscore > brazilscore:
        print('Italy won the match.')
    elif brazilscore > italyscore:
        print('Brazil won the match.')
    else:
        print('The match was a draw.')


    # End of your code here





if __name__ == '__main__':
    main()