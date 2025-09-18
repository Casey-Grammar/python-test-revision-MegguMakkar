# Task 5 FIFA World Cup
# With 9 FIFA World Cup wins between them, Brazil and Italy two of
# the most successful soccer countries in the world. Write a program
# that works out who won their latest soccer match, given the scores
# of both teams.

def main():
    #Write your code here
    italyScore = int(input("Italy: "))
    brazilScore = int(input("Brazil: "))
    if italyScore > brazilScore:
        print("Italy won the match.")
    elif brazilScore > italyScore:
        print("Brazil won the match.")
    else:
        print("The match was a draw.")


    # End of your code here





if __name__ == '__main__':
    main()