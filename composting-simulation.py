#!/usr/bin/python3

# Mincraft composting simulation to find the best farm for creating bonemeal

import random as rand
import functools

random_tick_speed = 3 # Java Edition, 1 for Bedrock Edition

cactus_ticks = 0 # number of random ticks cactus has had

compost_level = 0 # level of composter

@functools.lru_cache(maxsize=None)
def composting_prob(unit):
    if unit == "kelp":
        return 0.30
    elif unit == "beetroot":
        return 0.65
    elif unit == "apple": # growth mechanics complicated
        return 0.65
    elif unit == "melon":
        return 0.65
    elif unit == "pumpkin":
        return 0.65
    elif unit == "sea pickle":
        return 0.65
    elif unit == "wheat":
        return 0.65
    elif unit == "sugar cane":
        return 0.50
    elif unit == "melon slice":
        return 0.50
    elif unit == "cactus":
        return 0.50

def random_tick(unit):
    if rand.random() <= random_tick_speed/4096:
        growth_tick(unit)

def growth_tick(unit):
    global cactus_ticks
    if unit == "kelp":
        if rand.random() <= 0.14:
            add_unit(unit)
    elif unit == "cactus":
        cactus_ticks += 1
        if cactus_ticks >= 16:
            add_unit(unit)
            cactus_ticks = 0

def add_unit(unit):
    global compost_level
    if rand.random() <= composting_prob(unit):
        compost_level += 1

reps = 1000

total = 0
for i in range(reps):
    for j in range(60*60*20): # total number of game ticks per hour
        random_tick("kelp")
        if compost_level >= 7:
            total += 1

print("kelp: ", total/reps) # should output average amount of bonemeal per hour

total = 0
for i in range(reps):
    for j in range(60*60*20): # total number of game ticks per hour
        random_tick("cactus")
        if compost_level >= 7:
            total += 1

print("cactus: ", total/reps) # should output average amount of bonemeal per hour

