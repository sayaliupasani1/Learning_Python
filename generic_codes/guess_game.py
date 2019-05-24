secret_word = "Elephant"
guessed_word = ""
count = 1

while guessed_word != secret_word and count <=3:
    guessed_word = input("Enter your guess: ")
    count+=1
    if guessed_word != secret_word:
        print ("Incorrect guess! Try again!")
    else:
        print ("Correct guess!")
        print ("you win!")

if count >=3:
    print ("You have exceeded the allowed attempts!")