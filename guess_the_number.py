import random
def number_guessing_game():
    secrete_number=random.randint(1,100)
    guess=None
    print("welcome to the guess the secrete number game!")
    print("please help to to find out the number!")
    print("Now it is your turn to guess the number")
    while guess!=secrete_number:
        guess = int(input("enter a secrete number:"))
        if guess>secrete_number:
            print("too high")
        elif guess<secrete_number:
            print("too low")
        else:
            print("congratulations your guess is correct!")
number_guessing_game()