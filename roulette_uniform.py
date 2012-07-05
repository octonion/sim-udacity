#!/usr/bin/python

from numpy import random,average,std,sqrt,exp

# trials is the number of simulations

trials = 10000

# Range for the uniform distribution

low = 0.0
high = 1.0

mean = (low+high)/2

# Arrays to store simulation results

samples = [0.0]*trials
totals = [0.0]*trials
remainders = [0.0]*trials

# Run simulation with target = 1.0

# We'll spin until our total equals or exceeds target

target = 1.0

print
print "Target total = ",target

for i in range(0,trials):
    sample = 0.0
    total = 0.0
    while (total <= target):
        total = total+random.uniform(0.0,1.0)
        sample = sample+1
    samples[i] = sample
    totals[i] = total
    remainders[i] = total-target

print
print "Predictions:"
print "   Mean number of spins = ",exp(target)
print
print "Simulation results:"
print "   Mean number of spins = ",average(samples)

# Run simulation with target = 10.0

# We'll spin until our total equals or exceeds target

target = 10.0

print
print "Target total = ",target

for i in range(0,trials):
    sample = 0.0
    total = 0.0
    while (total <= target):
        total = total+random.uniform(0.0,1.0)
        sample = sample+1
    samples[i] = sample
    totals[i] = total
    remainders[i] = total-target

print
print "Predictions:"
print "   Mean number of spins = ",target/mean+2/3.0
print "   Mean total sum = ",target+1/3.0
print "   Mean remainder = ",1/3.0
print "   SD of remainder = ",sqrt(1/18.0)
print
print "Simulation results:"
print "   Mean number of spins = ",average(samples)
print "   Mean total sum = ",average(totals)
print "   Mean remainder = ",average(remainders)
print "   SD of remainder = ",std(remainders)
