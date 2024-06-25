word = input("Type a word: ")

intertwined = "".join(reversed(word))

if word.lower().replace(" ", "") == intertwined.lower().replace(" ", ""):
    print(f"{word} is a palindrome word.")
else:
    print(f"{word} is not a palindrome word.")
