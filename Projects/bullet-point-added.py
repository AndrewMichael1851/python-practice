#! python3
# bullet-point-added.py - Adds bullet points to the start of text in the clipboard.

# Example lines to copy:
'''
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
'''

# Import pyperclip and get the current clipboard
import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

# Join it back together
text = '\n'.join(lines)

# Add the returned result to a new clipboard
pyperclip.copy(text)

