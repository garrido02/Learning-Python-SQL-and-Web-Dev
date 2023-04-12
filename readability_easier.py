from cs50 import get_string

# prompt user for input
text = get_string("Text: ")

# define variables, keeping in mind that we will always have 1 word minimum
words = 1
letter = 0
sentences = 0

# loop through text to count variables
# range of length of text is basically through all words of text
for i in range(len(text)):
    if text[i].isalpha():
        letter += 1
    elif text[i].isspace():
        words += 1
    elif text[i] == '.' or text[i] == '?' or text[i] == '!':
        sentences += 1

# define grade counter
l = letter / words * 100
s = sentences / words * 100
grade = round(0.0588 * l - 0.296 * s - 15.8)

# define printing conditions
if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")