# --------------------------------------
# CSCI 127, Lab 3
# September 18, 2018
# Michael Heidal
# --------------------------------------

def count_vowels(sentence):
    num = 0;
    num = num + sentence.count("a")
    num = num + sentence.count("e")
    num = num + sentence.count("i")
    num = num + sentence.count("o")
    num = num + sentence.count("u")
    return num


def count_vowels_iterative(sentence):
    num = 0
    vowels = "aeiou"
    for vowel in vowels:
        for letter in sentence:
            if letter == vowel:
                num = num + 1
    return num
    
def remove_iterative(sentence):
    nospace = ""
    for letter in sentence:
        if letter == " ":
            nospace = nospace + ""
        else:
            nospace = nospace + letter
    return nospace


# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence to evaluate: ")
        sentence = sentence.lower()     # convert to lowercase
        print()
        print("Number of vowels using count     =", count_vowels(sentence))
        print("Number of vowels using iteration =", count_vowels_iterative(sentence))
        print("Using iteration = |" + remove_iterative(sentence) + "|")
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
