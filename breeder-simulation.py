#!/usr/bin/python3

# Mincraft villager breeder simulation to find the best farm for creating villagers

import random as rand
import functools

random_tick_speed = 3 # Java Edition, 1 for Bedrock Edition

field_size = 48 # size of field in breeder

growth_prob = 1/6 # probability of growth succeeding, based on conditions
# farmer villagers do not plant in rows, so most this can be is 1/6.

beetroot_growth_stages = [0] * field_size # growth stage of beetroot
potato_growth_stages = [0] * field_size # growth stage of potato
carrot_growth_stages = [0] * field_size # growth stage of carrot

food_in_inventory = 0 # amount of food in inventory of villagers 
# can share, so assume sharing happens instantly

def random_tick(unit):
    for i in range(field_size):
        if rand.random() <= random_tick_speed/4096:
            growth_tick(unit, i)

def growth_tick(unit, i):
    if unit == "beetroot":
        global beetroot_growth_stages
        if rand.random() <= growth_prob:
            if rand.random() <= (2/3): # beetroot is weird
                beetroot_growth_stages[i] += 1
        if beetroot_growth_stages[i] >= 3:
            add_unit(unit)
            beetroot_growth_stages[i] = 0 # unit is replanted immediately
    elif unit == "potato":
        global potato_growth_stages
        if rand.random() <= growth_prob:
            potato_growth_stages[i] += 1
        if potato_growth_stages[i] >= 7:
            add_unit(unit)
            potato_growth_stages[i] = 0 # unit is replanted immediately
    elif unit == "carrot":
        global carrot_growth_stages
        if rand.random() <= growth_prob:
            carrot_growth_stages[i] += 1
        if carrot_growth_stages[i] >= 7:
            add_unit(unit)
            carrot_growth_stages[i] = 0 # unit is replanted immediately

def add_unit(unit):
    global food_in_inventory
    if unit == "beetroot":
        food_in_inventory += 1
    elif unit == "potato":
        food_in_inventory += rand.randint(0,4) # 1-5 potatoes dropped, one used to replant
    elif unit == "carrot":
        food_in_inventory += rand.randint(1,4) # 2-5 carrots dropped, one used to replant

reps = 50

def per_hour_test(unit):
    global food_in_inventory
    food_in_inventory = 0 # reset level of food_in_inventory
    total = 0
    for i in range(reps):
        for j in range(60*60*20): # total number of game ticks per hour
            random_tick(unit)
            while food_in_inventory >= 24:
                total += 1
                food_in_inventory -= 24
    print(unit, ": ", total/reps)

units = ["beetroot", "potato", "carrot"]

for unit in units:
    per_hour_test(unit)
