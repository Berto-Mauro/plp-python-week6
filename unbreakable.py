def get_number():
    while True:
        try:
            number = int(input("Enter a whole number: "))
            return number
        except ValueError:
            print("That is not a number. Please try again.")


number = get_number()
print("You entered:", number)

