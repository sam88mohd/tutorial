#! /usr/bin/python3
# mcb.pyw - Saves and loads pieces of text to clipboard.
# Usage: python mcb.pyw save <keyword> - Save keyword to clipboard.
#		 python mcb.pyw <keyword> - loads keyword to clipboard.
#		 python mcb.pyw list - Loads all keywords to clipboard.
#		 python mcb.pyw delete - delete all keyword in clipboard.
#		 python mcb.pyw delete <keyword> - delete keyword in clip board.


import shelve, pyperclip, sys

mcbshelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() =='save':
	mcbshelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
		del mcbshelf[sys.argv[2]]
elif len(sys.argv) == 2:
	# List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbshelf.keys())))
	elif sys.argv[1] in mcbshelf:
		pyperclip.copy(mcbshelf[sys.argv[1]])
mcbshelf.close()