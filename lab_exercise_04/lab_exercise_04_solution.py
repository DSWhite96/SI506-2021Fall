# START LAB EXERCISE 04
print('Lab Exercise 04 \n')

#SETUP
chinese_desserts = [
    ["Wheat Flour Cake", 190],
    ["Egg Yolk", 260],
    ["Green Bean Cake", 100],
    ["Taro Pastry", 227],
    ["Durian Cake", 360],
    ["Flower Pastry", 130],
    ["Sun Cake", 172]
]

# END SETUP

# PROBLEM 1 (3 points)
def get_name(dessert):
    return dessert[0]

name = get_name(chinese_desserts[0])

print(f"\n1. First dessert item: {name}")


# Problem 2 (3 points)
def get_calories(dessert):
    return dessert[1]

calories = get_calories(chinese_desserts[1])

print(f"\n2. Calories of second dessert item: {calories}")


# PROBLEM 3 (5 points)
def remove_dessert(desserts_list, dessert):
    if dessert in desserts_list:
        desserts_list.remove(dessert)

sun_cake = chinese_desserts[-1]
remove_dessert(chinese_desserts, sun_cake)

print(f"\n3. {sun_cake}")
print(f"\n   {chinese_desserts}")


# Problem 4 (6 points)

def add_dessert(desserts, dessert, idx=0):
    desserts.insert(idx, dessert)

sweetheart_cake = ["Sweetheart Cake", 170]
add_dessert(chinese_desserts, sweetheart_cake, 1)

print(f"\n4. {chinese_desserts}")


# Problem 5 (3 points)

egg_tarts = ["Egg Tarts", 376]
add_dessert(idx=2, dessert=egg_tarts, desserts=chinese_desserts)

print(f"\n5. {chinese_desserts}")


# END LAB EXERCISE