# This program counts the number of occurrences of each letter in a string.

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
	count.setdefault(character, 0) # Ensures that the key is in the count dictionary
	count[character] += 1

pprint.pprint(count) # Print formated dictionary
