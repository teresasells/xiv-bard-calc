#! /usr/bin/python2

import numpy
import math
import gearcomparer

#each item has the array associated with it [dex, acc, crit, det, skill speed, vitality]

caps = numpy.array([0, 535, 0, 0, 0, 0])

kirimuhat1 = [24, 25, 25, 18, 9, 28]
kirimuhat2 = [24, 18, 25, 18, 18, 28]
kirimuhat3 = [24, 9, 25, 18, 25, 28]
demonhat = [27, 19, 27, 0, 0, 32] # cannot be bis
aironhat = [31, 29, 0, 14, 0, 36]
dreadhat = [31, 0, 20, 0, 29, 36]

head = [kirimuhat1, kirimuhat2, kirimuhat3, demonhat, aironhat, dreadhat]

kirimuchest = [39, 41, 41, 20, 0, 46]
demonchest = [45, 0, 44, 22, 0, 52] # almost pruned
aironworkschest = [50, 33, 0, 0, 47, 59] # destroyed by kirimu chest
dreadchest = [50, 0, 0, 34, 33, 59]

body = [kirimuchest, demonchest, aironworkschest, dreadchest]

kirimugloves1 = [24, 25, 25, 18, 9, 28]
kirimugloves2 = [24, 18, 25, 18, 18, 28]
kirimugloves3 = [24, 9, 25, 18, 25, 28]
demongloves = [24, 0, 19, 0, 27, 32] #noo no no
airongloves = [31, 0, 20, 21, 0, 36]
dreadgloves = [31, 29, 0, 14, 0, 36]

hands = [kirimugloves1, kirimugloves2, kirimugloves3, demongloves, airongloves, dreadgloves]

arachnesash1 = [18, 19, 18, 13, 13, 21]
arachnesash2 = [18, 18, 18, 13, 19, 21]
arachnesash3 = [18, 18, 19, 13, 13, 21] #loser melds
arachnesash4 = [18, 9, 19, 13, 19, 21]
demonbelt = [21, 14, 0, 0, 20, 24] # yea no
aironbelt = [23, 0, 15, 15, 0, 27]
dreadbelt = [23, 22, 0, 11, 0, 27]

waist = [arachnesash1, arachnesash2, arachnesash3, arachnesash4, demonbelt, aironbelt, dreadbelt]

kirimupants = [39, 41, 41, 20, 0, 46]
demonpants = [45, 0, 0, 22, 44, 52] # loser
aironpants = [50, 47, 0, 0, 33, 59]
dreadpants = [50, 33, 47, 0, 0, 59]

legs = [kirimupants, demonpants, aironpants, dreadpants]

kirimufeet = [24, 25, 25, 18, 0, 28]
demonfeet = [27, 0, 19, 19, 0, 32] # pruned again
aironfeet = [31, 20, 29, 0, 0, 36]
dreadfeet = [31, 29, 0, 0, 20, 36]

feet = [kirimufeet, aironfeet, aironfeet, dreadfeet]

scarf = [18, 19, 18, 12, 9, 0]
aironchoak = [23, 15, 0, 15, 0, 0] # technically pooped on by scarf but who really has time for that?
dreadchoak = [23, 22, 0, 0, 15, 0]

necklace = [scarf, aironchoak, dreadchoak]

aironearings = [23, 22, 0, 0, 15, 0]
platear1 = [18, 18, 19, 12, 9, 0]
platear2 = [18, 9, 19, 12, 18, 0]
platear3 = [18, 0, 19, 13, 18, 0]
dreadear = [23, 15, 0, 15, 0, 0] # pruned


earrings = [dreadear, platear1, platear2, platear3, aironearings]

platwrists1 = [18, 0, 19, 12, 19, 0] # pruned
platwrists2 = [18, 9, 18, 12, 19, 0]
platwrists3 = [18, 18, 18, 6, 19, 0]
platwrists4 = [18, 19, 18, 0, 19, 0]
aironwrists = [23, 22, 0, 0, 15, 0]
dreadwrists = [23, 0, 22, 11, 0, 0]

bracelets = [platwrists1, platwrists2, platwrists3, platwrists4, aironwrists, dreadwrists]

platring1 = [18, 0, 19, 13, 18, 0]
platring2 = [18, 9, 18, 13, 18, 0]
platring3 = [18, 18, 18, 13, 9, 0]
platring4 = [18, 19, 18, 13, 0, 0]
dreadring = [23, 0, 0, 11, 22, 0] # pruned
aironring = [23, 22, 15, 0, 0, 0]
ironring = [21, 20, 14, 0, 0, 0] # wants to prune but thats only because it doesnt understand :(

rings = [platring1, platring2, platring3, platring4, ironring, aironring, dreadring] # accounting for unique rings is gonna be fun ._.

allitems = [head, body, hands, waist, legs, feet, necklace, earrings, bracelets, rings, rings] # weapon
allindex = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def calc_effectivedex(gearset):
    seedweights = [1.0, 0, 0.339, 0.320, 0.161, 0]
    wd = [9.429]
    #note that these weights are from http://www.reddit.com/r/ffxiv/comments/2q2tch/job_statweight_updates/ (22Dec2014)
    return numpy.sum(numpy.array(gearset)*numpy.array(seedweights))+52*wd[0]

def pruneItems(itemset):
    wd = [9.429]
    i = j = 0
    for i in range(len(itemset)):
        myval = calc_effectivedex(itemset[i])
        print myval, i
        mycaps = caps*itemset[i]
        for j in range(len(itemset)):
            newval = calc_effectivedex(itemset[j])
            newcaps = caps*itemset[j]
            comp = mycaps > newcaps
            if newval > myval and not True in comp:
                print "prune item", i, "beat by", j, "dif", newval-myval

def sumset(fullcombo, indexes):
    base = [334, 341, 394, 228, 341, 269]
    for i in range(0, 11):
        base = numpy.add(base, allitems[i][allindex[i]])
    accplus = min(math.floor(base[1]*.03), 16)
    critplus = min(math.floor(base[2]*.05), 33)
    vitplus = min(math.floor(base[5]*.05), 28)
    return numpy.add(base, [0, accplus, critplus, 0, 0, vitplus])

def increment(fullcombo, indexes):
    i = 0
    while i < len(fullcombo):
        if indexes[i]+1 == len(fullcombo[i]):
            indexes[i] = 0
            i = i + 1
        else:
            indexes[i] = indexes[i]+1
            return False
    return True




print "head"
pruneItems(numpy.array(head))
print "body"
pruneItems(body)
print "hands"
pruneItems(numpy.array(hands))
print "waist"
pruneItems(numpy.array(waist))
print "legs"
pruneItems(numpy.array(legs))
print "feet"
pruneItems(numpy.array(feet))
print "necklace"
pruneItems(numpy.array(necklace))
print "earing"
pruneItems(numpy.array(earrings))
print "bracelet"
pruneItems(numpy.array(bracelets))
print "ring"
pruneItems(numpy.array(rings))

sumset(allitems, allindex)

def isValid(itemset):
    comp = itemset > caps
    return not False in comp


def calc_bis(allitems, allindex):
    bestset = sumset(allitems, allindex)
    bestsetval = gearcomparer.calc_dps(bestset[0], bestset[1], bestset[2], bestset[3], bestset[4], [52, 3.2])
    print bestsetval
    while(not increment(allitems, allindex)):
        newset = sumset(allitems, allindex)
        if(isValid(newset)):
            newval = gearcomparer.calc_dps(newset[0], newset[1], newset[2], newset[3], newset[4], [52, 3.2])
            if(newval > bestsetval):
                bestset = newset
                bestsetval = newval
                print bestsetval, bestset, allindex

calc_bis(allitems, allindex)
