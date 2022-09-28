secret_number = 9
i = 0
guess_limit = 3
# or you can rename i as guess_count?
# i represents the number of guesses the user has made
while i < guess_limit:
    guess = int(input("guess: "))
    i += 1
    if guess == secret_number:
        print("you win!!")
        break
else:
    print("sorry game over")