def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

phrase = input ("Enter your word: ")
print(translator(phrase))
