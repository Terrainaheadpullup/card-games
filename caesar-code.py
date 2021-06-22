# for letter to number conversions
letter_number_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11,
                      "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,
                      "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26, " ": " "}

# for number to letter conversions
number_letter_dict = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K",
                      12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U",
                      22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z", " ": " "}

# enter text in block capitals
Word = input("Enter text in block capitals: ")

# converts letters to numbers adds a number and converts back to letters then writes it to a file
for i in range(26):
    for letters in range(len(Word)):
        letter = Word[letters]
        if letter == " ":
            letter_2 = letter
        else:
            letter_number = letter_number_dict[letter]
            letter_number_2 = letter_number + i
            if letter_number_2 > 26:
                letter_number_2 -= 26
            letter_2 = number_letter_dict[letter_number_2]
        data = open("ROT.txt", "a")
        data.write(letter_2)
    data.write("\n")
