# Task 10 Class roll
# Write a program that takes a list of student names and sorts them
# to create a class roll. The list of names will be given on a one line
# separated by a single space.

#The student names could be entered with any combination of capitals or not.
#If they are entered with no capital first letter the list should not append.
#If they are entered with a capital first letter the list should append
#If they are entered with a mix of capitals the name should be converted to capital first letter and
#then added to the list.

def main():
    #Write your code here
    studentsNames = input("Students: ")
    print('Class Roll')
    # Split the input string into a list of names, capitalize each name, sort the list, and print each name
    namesList = studentsNames.split()
    capitalizedNames = [name.capitalize() for name in namesList]
    capitalizedNames.sort()
    for name in capitalizedNames:
        print(name)


    # End of your code here
if __name__ == '__main__':
    main()