# Task 11 Fix the errors in the code
# Fix the errors in this code by running the program with different inputs
# and editing the code until all errors are fixed.

def main():
    #Fix the code starting here
    drink = input("WHAT DRINK DO YOU WANT TO ORDER?")
    if drink.islower():
     print("I DIDN'T HEAR YOUR ORDER!") 
    elif drink.isupper():
      many = input("HOW MANY? ")
      CoffeeScoops = many * 4
    print(f'{many} {drink}S COMING RIGHT UP!')
    print(f'The barrister needs {CoffeeScoops} scoops of coffee in the coffee making machine')
    

# End of code to be fixed





if __name__ == '__main__':
    main()