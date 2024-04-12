#! python3
# myclip.py - A multi-clipboard program.

text = {
    'agree': """Yes, I agree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week?""",
    'upsell': """Would you consider doing this instead?"""
}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # The first command line arg is the keyphrase

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print('Template text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no rule for ' + keyphrase)
    