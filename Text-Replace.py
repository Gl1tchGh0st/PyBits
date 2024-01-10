# A program that replaces given charcters within a string of text. 

# Function to loop back when invalid input is occoured
def run():
    # User selecting which option to run
    print("""Please select an option:
    1. Replace characters in a string
    2. Remove characters from a string""")
    option = input("Enter your choice here: ")
    print("\n")
    # Initiate the removing option
    if option == "1":
        text = input("Enter your string here: ")
        replacing_digit = input("Enter the character you wish to replace: ")
        new_digit = input("Enter the character you wish to change to: ")
        new_text = text.replace(replacing_digit, new_digit)
        print("\n")
        print("Your old text was:")
        print(text + "\n")
        print("Your new text is:")
        print(new_text)
        print("\n")
    # Initiate the removing option
    elif option == "2":
        text = input("Enter your string here: ")
        removing_digit = input("Enter the charcter you wish to remove: ")
        new_text = text.replace(removing_digit, "")
        print("\n")
        print("Your old text was:")
        print(text + "\n")
        print("Your new text is:")
        print(new_text)
        print("\n")
    # If option is invalid, print an error
    else:
        print("Your option is incorrect. Please try again.")
        print("\n")
        run()
    again = input("Run again? ")
    # If statement to run again
    if again == "Yes" or again == "yes":
        run()
    #Exits the program
    else:
        print("Exiting now...")
        input("Press any key to continues")
# Initiate the program
run()
