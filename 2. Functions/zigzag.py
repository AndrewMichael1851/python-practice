import time, sys

# Set globals.
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # Main program loop.
        print(' ' * indent, end='')
        print('**********')
        time.sleep(0.1) # Pause for a moment.

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False # Change direction.
        
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True # Change direction.
except KeyboardInterrupt:
    sys.exit()
    