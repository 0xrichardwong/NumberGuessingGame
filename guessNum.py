

import sys
import random

# prompt function
def prompt_user(message):
    sys.stdout.buffer.write(message.encode())
    sys.stdout.flush()
    return int(sys.stdin.buffer.readline())

# prompt input
min_val = prompt_user('This is a Number Guessing Game. Pick a minimum number.\n')
max_val = prompt_user('Nextly, pick a maximum number.\n')
guessed_num = prompt_user('Thank you for the inputs. Now please guess the number.\n')

# random number generator
def guess_the_number(min_val, max_val):
    return random.randint(min_val, max_val)

num = guess_the_number(min_val, max_val)

# output
while num != guessed_num:
    guessed_num = prompt_user('Wrong! Input a new number.\n')

print("Congratulations!! The number was " + str(guessed_num) + "!!")
