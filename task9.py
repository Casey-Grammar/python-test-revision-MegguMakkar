# Task 9 Cat problem
# You've collected too many cats. Write a program to count how
# many cats you have by reading in their names. All your cats only
# have first names, with no spaces.

def main():
    #Write your code here
    listOfCatsNames = input("Cats: ")
    # Split the input string into a list of names and print the number of names
    catsNames = listOfCatsNames.split()
    print("You have " + str(len(catsNames)) + " cats.")



    # End of your code here
if __name__ == '__main__':
    main()