#! /usr/bin/python3

# madlib.py - fun word game

import re

# Open the madlib.txt file.
file = open('madlib.txt')
text = file.read()
file.close()

# Print the content of the file
print(text)

#use regex to search the part to replace.
regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')
for i in regex.findall(text):
	for j in i:
		if j != '':
			reg = re.compile(r'{}'.format(j))
			inp = input('Enter a {}:\n'.format(j))
			text = reg.sub(inp.lower(), text, 1)
print(text)
# Write the input words to new file and close the file.
file = open('madlib_ans.txt', 'w')
file.write(text)
file.close()