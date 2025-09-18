# Task 8 Call signs
# A portmanteau is a word made by combining parts of two other
# words. This could be used to create call signs for an online
# group.

#For example, david and jones would make daones.

#Let's make some call signs!

#Write a program that asks a user for their first name and last
#name and then takes the first two letters of the first name and
#the last four letters of the last name and combines them to make
#a new call sign. (N.B. we won't test your program with any input
#that's too short!)

def main():
    #Write your code here
    namesForCallSigns = input("First and Last Name? ")
    
    #Print the first two letters of the first word entered and the last four letters of the second word entered
    firstName = namesForCallSigns.split()[0]
    lastName = namesForCallSigns.split()[1]
    callSign = firstName[:2] + lastName[-4:]
    print("Your call sign is: " + callSign)
    


    # End of your code here





if __name__ == '__main__':
    main()