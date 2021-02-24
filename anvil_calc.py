#!/usr/bin/python3

# Perhaps I am biting off more than I can chew with this project. My hope is to create program that allows you to input what you have and what you want and it computes the way to combine them that uses the least number of levels. Anvil costs, especially with enchantments are complex though, so who knows if I can make it work?


# format for stuff:
# dictionary with the following fields:
# type: what is it? Sword, book, etc (only really matters for checking if certain enchantments are possible)
# uses: how many times has anvil been used on it?
# enchantments: dictionary with enchantments as keys and levels as values (enchantments that aren't on it will either not be there or have a level of 0)

enchantment_data = {
        "Protection": {
            "max_lvl": 4,
            "item_mult": 1,
            "book_mult": 1,
            "type_apply": ["helmet", "chestplate", "leggings", "boots"]
        },
        "Fire Protection": {
            "max_lvl": 4,
            "item_mult": 2,
            "book_mult": 1,
            "type_apply": ["helmet", "chestplate", "leggings", "boots"]
        },
        "Feather Falling": {
            "max_lvl": 4,
            "item_mult": 2,
            "book_mult": 1,
            "type_apply": ["boots"]
        },
        "Blast Protection": {
            "max_lvl": 4,
            "item_mult": 4,
            "book_mult": 2,
            "type_apply": ["helmet", "chestplate", "leggings", "boots"]
        },
        "Projectile Protection": {
            "max_lvl": 4,
            "item_mult": 2,
            "book_mult": 1,
            "type_apply": ["helmet", "chestplate", "leggings", "boots"]
        },
        "Thorns": {
            "max_lvl": 3,
            "item_mult": 8,
            "book_mult": 4,
            "type_apply": ["helmet", "chestplate", "leggings", "boots"]
        },
        "Respiration": {
            "max_lvl": 3,
            "item_mult": 4,
            "book_mult": 2,
            "type_apply": ["helmet"]
        },
        "Depth Strider": {
            "max_lvl": 3,
            "item_mult": 4,
            "book_mult": 2,
            "type_apply": ["boots"]
        },
        "Aqua Affinity": {
            "max_lvl": 1,
            "item_mult": 4,
            "book_mult": 2,
            "type_apply": ["helmet"]
        },
        "Sharpness": {
            "max_lvl": 5,
            "item_mult": 1,
            "book_mult": 1,
            "type_apply": ["sword", "ax"]
        },
        "Smite": {
            "max_lvl": 5,
            "item_mult": 2,
            "book_mult": 1,
            "type_apply": ["sword", "ax"]
        },
        "Bane of Arthropods": {
            "max_lvl": 5,
            "item_mult": 2,
            "book_mult": 1,
            "type_apply": ["sword", "ax"]
        },
        "Knockback": {
            "max_lvl": 2,
            "item_mult": 2,
            "book_mult": 1,
            "type_apply": ["sword"]
        },
        "Fire Aspect": {
            "max_lvl": 2,
            "item_mult": 4,
            "book_mult": 2,
            "type_apply": ["sword"]
        },
        "Looting": {
            "max_lvl": 3,
            "item_mult": 4,
            "book_mult": 2,
            "type_apply": ["sword"]
        },
        "Efficiency": {
            "max_lvl": 5,
            "item_mult": 1,
            "book_mult": 1,
            "type_apply": ["pickaxe", "shovel", "ax", "hoe", "shears"]
        },
        "Silk Touch": {
            "max_lvl": 1,
            "item_mult": 8,
            "book_mult": 4,
            "type_apply": ["pickaxe", "shovel", "ax", "hoe"]
        },
        "Unbreaking": {
            "max_lvl": 3,
            "item_mult": 2,
            "book_mult": 1,
            "type_apply": ["pickaxe", "shovel", "ax", "fishing rod", "helmet", "chestplate", "leggings", "boots", "sword", "bow", "hoe", "shears", "flint and steel", "shield", "elytra", "trident", "crossbow"]
        },
        "Fortune": {
            "max_lvl": 3,
            "item_mult": 4,
            "book_mult": 2,
            "type_apply": ["pickaxe", "shovel", "ax", "hoe"]
        },
        "Power": {
            "max_lvl": 5,
            "item_mult": 1,
            "book_mult": 1,
            "type_apply": ["bow"]
        },
        "Mending": {
            "max_lvl": 1,
            "item_mult": 4,
            "book_mult": 2,
            "type_apply": ["pickaxe", "shovel", "ax", "fishing rod", "helmet", "chestplate", "leggings", "boots", "sword", "bow", "hoe", "shears", "flint and steel", "shield", "elytra", "trident", "crossbow"]
        }
}

incompitible_enchantments_data = [
        ["Sharpness", "Smite", "Bane of Arthropods"],
        ["Fortune", "Silk Touch"],
        ["Protection", "Fire Protection", "Blast Protection", "Projectile Protection"],
        ["Depth Strider", "Frost Walker"],
        ["Infinity", "Mending"],
        ["Multishot", "Piercing"],
        ["Loyalty", "Riptide"],
        ["Channeling", "Riptide"],
        ["Silk Touch", "Looting"],
        ["Silk Touch", "Luck of the Sea"]
]

def prior_work_penalty(thing):
    return 2**(thing["uses"]) - 1

def rename_cost(thing):
    return 1 + prior_work_penalty(thing)

def combining_cost(target, sacrifice):
    return prior_work_penalty(target) + prior_work_penalty(sacrifice) + enchantment_cost(target, sacrifice)

def combine(target, sacrifice):
    result = {"type": target["type"]}
    result["uses"] = max(target["uses"], sacrifice["uses"]) + 1
    result["enchantments"] = combine_enchantments(target, sacrifice)
    return result

def enchant_mult(enchant, sacrifice_type):
    if sacrifice_type == "book":
        return enchantment_data[enchant]["book_mult"]
    else:
        return enchantment_data[enchant]["item_mult"]

def max_lvl(enchant):
    return enchantment_data[enchant]["max_lvl"]

def compatible(target_type, enchant):
    return target_type in enchantment_data[enchant]["type_apply"]

def incompatible_enchants(enchant1, enchant2):
    incompatible = False
    for category in incompatible_enchantments_data:
        if enchant1 in category and enchant2 in category:
            incompatible = True
    return incompatible

def enchantment_cost(target, sacrifice):
    cost = 0
    for enchant, lvl in sacrifice["enchantments"].items():
        if compatible(target["type"], enchant):
            for enchant_target in target["enchantments"]:
                incompatible = False
                if incompatible_enchants(enchant_target, enchant):
                    incompatible = True
                    cost += 1
            if incompatible:
                break
            if enchant in target["enchantments"]:
                # combining enchantments
                target_lvl = target["enchantments"]["enchant"]
                if lvl > target_lvl:
                    final_lvl = lvl
                elif lvl == target_lvl:
                    if lvl < max_lvl(enchant):
                        final_lvl = lvl+1
                    else:
                        final_lvl = lvl
                else: # lvl < target_lvl
                    final_lvl = target_lvl
            else: # enchantment not on target
                final_lvl = lvl
            cost += final_lvl*enchant_mult(enchant, sacrifice["type"])

def combine_enchantments(target, sacrifice):
    res_enchants = copy(target["enchantments"])
    for enchant, lvl in sacrifice["enchantments"]:
        if compatitible(target["type"], enchant):
            for enchant_target in target["enchantments"]:
                incompatible = False
                if incompatible_enchants(enchant_target, enchant):
                    incompatible = True
            if incompatible:
                break
            if enchant in target["enchantments"]:
                # combining enchantments
                target_lvl = target["enchantments"][enchant]
                if lvl > target_lvl:
                    final_lvl = lvl
                elif lvl == target_lvl:
                    if lvl < max_lvl(enchant):
                        final_lvl = lvl + 1
                    else:
                        final_lvl = lvl
                else: # lvl < target_lvl
                    final_lvl = target_lvl
            else: # enchantment not on target
                final_lvl = lvl
            res_enchants[enchant] = final_lvl
    return res_enchants
