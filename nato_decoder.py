from nato_tree import NatoTree
from character_tree import CharacterTree
import csv

def getNATOFromUser():
    return input("Please enter a NATO phonetic alphabet code word (All letters must be in "
                 "lower case): ")

def getCharFromUser():
    return input("Please enter an English character (must be upper case):")


def main():
    nato = NatoTree()
    with open(f'nato_message.txt') as natotxtfile:
        for line in natotxtfile:
            if line.strip()[0:1:1] == '\\':
                nato.add(line.strip()[0:2:1], line.strip()[2:])
            else:
                nato.add(line.strip()[0:1:1], line.strip()[1:])

    natotxtfile.close()
    # print(nato.find("victor"))
    # Ask user to input a nato alphabet natoCodeWord, print and save natoCodeWord to txt file

    character = CharacterTree()
    with open(f'nato_message.txt') as chartxtfile:
        for line in chartxtfile:
            if line.strip()[0:1:1] == '\\':
                character.add(line.strip()[2:], line.strip()[0:2:1])
            else:
                character.add(line.strip()[1:], line.strip()[0:1:1])

    chartxtfile.close()
    # print(character.find("A"))

    # This code assumes that the user will input a valid NATO code word
    userNATOInput = getNATOFromUser()
    userCharacter = nato.Decode(userNATOInput)
    print(f"The NATO phonetic alphabet code word {userNATOInput} represents the English character {userCharacter}")

    userCharInput = getCharFromUser()
    userNatoCodeWord = character.Encode(userCharInput)
    print(F"The NATO phonetic alphabet code word for the English character {userCharInput} is {userNatoCodeWord}.")

    with open('saved_nato_translation.csv', 'w') as f:
        writer = csv.writer(f)
        header = ["input", "output"]
        decodeData = [userNATOInput, userCharacter]
        encodeData = [userCharInput, userNatoCodeWord]
        writer.writerow(header)
        writer.writerow(decodeData)
        writer.writerow(encodeData)

if __name__ == "__main__":
    main()





