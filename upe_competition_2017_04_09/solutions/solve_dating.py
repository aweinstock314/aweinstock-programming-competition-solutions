#!/usr/bin/env python
import sys

initial = raw_input()

cr_pairs = []
try:
    while True:
        challenge, response = raw_input().rstrip().split(':')
        cr_pairs.append([challenge, response])
except EOFError:
    pass

#print initial
#print cr_pairs

for i, c in enumerate(initial):
    for (challenge, response) in cr_pairs:
        if initial[i:i+len(challenge)] == challenge:
            sys.stdout.write(response)
print
