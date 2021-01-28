#!/usr/bin/python3

# Mincraft composting simulation to find the best farm for creating bonemeal

import random as rand
import functools

random_tick_speed = 3 # Java Edition, 1 for Bedrock Edition

cactus_ticks = 0 # number of random ticks cactus has had
wheat_growth_stage = 0 # growth stage of wheat
beetroot_growth_stage = 0 # growth stage of beetroot
melon_slices = 0 # number of melon slices built up

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
    if unit == "kelp":
        if rand.random() <= 0.14:
            add_unit(unit)
    elif unit == "cactus":
        global cactus_ticks
        cactus_ticks += 1
        if cactus_ticks >= 16:
            add_unit(unit)
            cactus_ticks = 0
    elif unit == "wheat":
        global wheat_growth_stage
        if rand.random() <= (1/3):
            wheat_growth_stage += 1
        if wheat_growth_stage >= 7:
            add_unit(unit)
            wheat_growth_stage = 0
    elif unit == "beetroot":
        global beetroot_growth_stage
        if rand.random() <= (1/3):
            if rand.random() <= (2/3):
                beetroot_growth_stage += 1
        if beetroot_growth_stage >= 3:
            add_unit(unit)
            beetroot_growth_stage = 0
    elif unit == "melon slice":
        if rand.random() <= (1/3):
            for i in range(rand.randint(3,7)):
                add_unit(unit)
    elif unit == "pumpkin":
        if rand.random() <= (1/3):
            add_unit(unit)
    elif unit == "melon":
        global melon_slices
        if rand.random() <= (1/3):
            melon_slices += rand.randint(3,7)
            while melon_slices >= 9:
                add_unit(unit)
                melon_slices -= 9

def add_unit(unit):
    global compost_level
    if rand.random() <= composting_prob(unit):
        compost_level += 1

reps = 1000

def per_hour_test(unit):
    global compost_level
    compost_level = 0 # reset level of composter
    total = 0
    for i in range(reps):
        for j in range(60*60*20): # total number of game ticks per hour
            random_tick(unit)
            if compost_level >= 7:
                total += 1
                compost_level = 0
    print(unit, ": ", total/reps)

units = ["kelp", "cactus", "wheat", "beetroot", "pumpkin", "melon slice", "melon"]

for unit in units:
    per_hour_test(unit)
