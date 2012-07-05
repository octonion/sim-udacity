#!/usr/bin/python

import random
from math import ceil

trials = 10000

doors = 3

print
print doors,"doors"

win_stand = 0
win_switch = 0

# We always pick Door 1

for i in range(0,trials):
    prize = ceil(doors*(random.random()))
    
    # Stand

    if (prize==1):
        win_stand = win_stand+1

    # Switch

    if not(prize==1):
        win_switch = win_switch+1

print
print "Results:"
print "  stand wins = ",win_stand
print "  switch wins = ",win_switch

doors = 10

print
print doors,"doors"

win_stand = 0
win_switch = 0

# We always pick Door 1

for i in range(1,trials+1):
    prize = ceil(doors*(random.random()))
    
    # Stand

    if (prize==1):
        win_stand = win_stand+1

    # Switch

    if not(prize==1):
        win_switch = win_switch+1

print
print "Results:"
print "  stand wins = ",win_stand
print "  switch wins = ",win_switch
