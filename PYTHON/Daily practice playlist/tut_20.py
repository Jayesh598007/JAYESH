# Exercise no: 3
# THe Perfect Guess
# user has to input a number until he guess the right number

print("Welcome to the number guessing game")
print("Let's Start!\n")
n = 18
number_of_guesses = 1
print("Number of guesses are limited to 5 times")
while (number_of_guesses <= 5):
    guess_number = int(input("Guess the number: "))
    if guess_number < n:
        print("\nyou entered smaller number, please input larger number.")
    elif guess_number > n:
        print("\nyou entered larger number, please input smaller number. ")
    else:
        print("\n    ******  YOU WON !!  ******  ")
        print(" You took",number_of_guesses, "no.of guesses to finish.")
        break

    print(5-number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses > 5):
    print("\n   ***  Game Over  ***  ")
