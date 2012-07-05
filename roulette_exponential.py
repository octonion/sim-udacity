#!/usr/bin/python

from numpy import random,average,std,sqrt

# trials is the number of simulations

trials = 10000

# We'll spin until our total equals or exceeds target

target = 10.0

# Parameter for the exponential distribution

lam = 1.0

mean = 1/lam

# Arrays to store simulation results

samples = [0.0]*trials
totals = [0.0]*trials
remainders = [0.0]*trials

# Run simulations

for i in range(0,trials):
    sample = 0.0
    total = 0.0
    while (total <= target):
        total = total+random.exponential(1.0)
        sample = sample+1
    samples[i] = sample
    totals[i] = total
    remainders[i] = total-target

print
print "Predictions:"
print "   Mean number of spins = ",target/mean+1.0
print "   Mean total sum = ",target+mean
print "   Mean remainder = ",mean
print "   SD of remainder = ",mean
print
print "Simulation results:"
print "   Mean number of spins = ",average(samples)
print "   Mean total sum = ",average(totals)
print "   Mean remainder = ",average(remainders)
print "   SD of remainder = ",std(remainders)
