#Madlibs is a word game where one player prompts another for a list of words to substitute for blanks in a story.

def madlibs():
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adjective1 = input("Enter an adjective: ")
    adverb1 = input("Enter an adverb: ")
    noun2 = input("Enter another noun: ")

    print("The " + adjective1 + " " + noun1 + " " + verb1 + " " + adverb1 + " to the " + noun2 + ".")

madlibs()

