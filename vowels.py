string=input("Enter the string:")
for letter in string:
    if(letter in "aeiou"):
        print(letter)
        if(letter not in "aeiou"):
            print("No vowels")
