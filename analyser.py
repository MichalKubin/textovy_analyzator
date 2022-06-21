# odstraní tečky, čárky a pomlčky

for forbidden_character in analyzed_text:
    if forbidden_character == "." or forbidden_character == ",":
        analyzed_text = str(analyzed_text).replace(
            forbidden_character, "")
    elif forbidden_character == "-" or forbidden_character == "\n":
        analyzed_text = str(analyzed_text).replace(
            forbidden_character, " ")

analyzed_text = analyzed_text.rsplit(" ")

# odstraní uvozovky na začátku a na konci textu, které po
# rozdělení vytvoří samostatné znaky

for forbidden_space in analyzed_text:
    if forbidden_space == '':
        analyzed_text.remove('')

# počet slov,

word_count = len(analyzed_text)

if word_count == 1:
    print("There is 1 word in the selected text.")
else:
    print(f"There are {word_count} words in the selected text.")

# počet slov začínajících velkým písmenem,

words_with_capitals = 0

for words in analyzed_text:
    if words[0].isupper():
        words_with_capitals += 1

if words_with_capitals == 1:
    print("There is 1 titlecase word.")
else:
    print(f"There are {words_with_capitals} titlecase words.")
# print(analyzed_text)

# počet slov psaných velkými písmeny,

words_uppercase = 0

for words in analyzed_text:
    if words.isupper() and words.isalpha():
        words_uppercase += 1
    elif words.isupper() and words.isalpha() is False:
        words_uppercase += 0

if words_uppercase == 1:
    print("There is 1 uppercase word.")
else:
    print(f"There are {words_uppercase} uppercase words.")

# počet slov psaných malými písmeny,

words_lowercase = 0

for words in analyzed_text:
    if words.islower():
        words_lowercase += 1

if words_lowercase == 1:
    print("There is 1 lowercase word.")
else:
    print(f"There are {words_lowercase} lowercase words.")

# počet čísel (ne cifer),

numbers_count = 0

for words in analyzed_text:
    if words.isnumeric():
        numbers_count += 1

if numbers_count == 1:
    print("There is 1 numeric string.")
else:
    print(f"There are {numbers_count} numeric strings.")

# sumu všech čísel (ne cifer) v textu.

numbers_sum = 0
numbers_sum = int(numbers_sum)

for words in analyzed_text:
    if words.isnumeric():
        numbers_sum += int(words)

print(f"The sum of all the numbers: {numbers_sum}")

# Program zobrazí jednoduchý sloupcový graf, který bude
# reprezentovat četnost různých délek slov v textu.

print(separator)
print(" LEN |       OCCURENCES       | NR. ")
print(separator)

word_length = []

for words in analyzed_text:
    word_length.append(len(words))

word_length.sort()
# print(word_length)

count_length = 1

while count_length <= word_length[-1]:
    print(str(count_length).rjust(4) +
          str("") * (4 - len(str(count_length))) +
          " |" +
          "*" * (word_length.count(count_length)) +
          " " * (24 - word_length.count(count_length)) +
          "|" +
          str(word_length.count(count_length)).rjust(4))
    count_length += 1