# SI 506 Problem Set 04

# Part 1
menu = [
    ["name", "categories", "price (HKD)"],
    ["short ribs with xo source", "steamed", 28],
    ["pan-fried turnip cake", "Pan-fried/Baked", 22],
    ["Malay sponge cake", "sweet", 17],
    ["baked egg tart", "sweet", 18],
    ["custard bun", "steamed", 21],
    ["barbecued pork bun", "steamed", 17],
    ["lotus seed bun", "steamed", 18],
    ["shrimp dumpling", "steamed", 29],
    ["shumai", "steamed", 26],
    ["braised chicken feet", "steamed", 19],
    ["pineapple bun", "Pan-fried/Baked", 19],
    ["veggies", "steamed", 17],
    ["lo mai gai", "steamed", 24],
    ["curry beaf strip", "steamed", 26],
    ["honey stewed bbq pork rice roll", "rice roll", 23],
    ["shrimp rice roll", "rice roll", 29],
    ["chrysanthemum", "tea", 8],
    ["longjing", "tea", 20],
    ["tieguanyin", "tea", 12],
    ["dahongpao", "tea", 18],
    ["pu'er", "tea", 10],
]

print("Problem 01\n\n")

# Problem 01: Convert HKD to USD.
menu[0].append("price (USD)")
for item in menu[1:]:
    price_usd = item[2] * 0.128
    item.append(round(price_usd, 2))

print(menu)

print("\n\nProblem 02\n\n")

# Problem 02: Categorize items into superb, top, good, and tea (15 points).
menu[0].append("grade")
for item in menu[1:]:
    if item[1] == "tea":
        item.append("tea")
    elif item[2] > 25:
        item.append("superb")
    elif item[2] > 20:
        item.append("top")
    else:
        item.append("good")

print(menu)

print("\n\nProblem 03\n\n")

# Problem 03: Find the max & min price of dim sums as well as their names (20 points).
max_price = 0
max_names = []
for item in menu[1:]:
    if item[1] == "tea":
        continue
    if item[2] > max_price:
        max_price = item[2]
        max_names.clear() # clear previous elements
        max_names.append(item[0])
    elif item[2] == max_price:
        max_names.append(item[0])

min_price = 100
min_names = []
for item in menu[1:]:
    if item[1] == "tea":
        continue
    if item[2] < min_price:
        min_price = item[2]
        min_names.clear() # clear previous elements
        min_names.append(item[0])
    elif item[2] == min_price:
        min_names.append(item[0])

print(f"max price: {max_price}")
print(f"max names: {max_names}")
print(f"min price: {min_price}")
print(f"min names: {min_names}")

print("\n\nProblem 04\n\n")

# Problem 04: Get the average price of steamed dim sums (10 points).
total_price = 0
total_count = 0
steamed_avg_price = 0
for item in menu[1:]:
    if item[1] == "steamed":
        total_price += item[2]
        total_count += 1
steamed_avg_price = total_price/ total_count

print(f"average price of steamed dim sums: {steamed_avg_price}")


# Part 2

print("\n\nProblem 5.1\n\n")

# Problem 5.1: implement get_category_by_food (15 points).
def get_category_by_food(menu, food_name):
    category = None
    for item in menu:
        if item[0] == food_name:
            category = item[1]
            break
    return category

print(f"E.g. the category of longjing: {get_category_by_food(menu, 'longjing')} (should be tea)")
print(f"E.g. the category of shumai: {get_category_by_food(menu, 'shumai')} (should be steamed)")

print("\n\nProblem 5.2\n\n")

# Problem 5.2: implement is_one_cup_two_pieces (10 points).

def is_one_cup_two_pieces(menu, foods):
    condition1 = (
        get_category_by_food(menu, foods[0]) == "tea" and
        get_category_by_food(menu, foods[1]) != "tea" and
        get_category_by_food(menu, foods[2]) != "tea"
        )
    condition2 = (
        get_category_by_food(menu, foods[1]) == "tea" and
        get_category_by_food(menu, foods[0]) != "tea" and
        get_category_by_food(menu, foods[2]) != "tea"
        )
    condition3 = (
        get_category_by_food(menu, foods[2]) == "tea" and
        get_category_by_food(menu, foods[0]) != "tea" and
        get_category_by_food(menu, foods[1]) != "tea"
        )

    return condition1 or condition2 or condition3

print(f"E.g. Testing with longjing, veggies, and shumai: {is_one_cup_two_pieces(menu, ['longjing', 'veggies', 'shumai'])} (should be True)")
print(f"E.g. Testing with longjing, dahongpao, and shumai: {is_one_cup_two_pieces(menu, ['longjing', 'dahongpao', 'shumai'])} (should be False)")

print("\n\nProblem 6.1\n\n")

# Problem 6.1: implement has_one_cup_two_pieces (15 points)
def has_one_cup_two_pieces(menu, order):
    tea_count = 0
    dim_sum_count = 0
    for name in order:
        if get_category_by_food(menu, name) == "tea":
            tea_count += 1
        else:
            dim_sum_count += 1

    return tea_count >= 1 and dim_sum_count >= 2

print(f"E.g. Testing with ['shumai', 'longjing']: {has_one_cup_two_pieces(menu, ['shumai', 'longjing'])} (should be False)")
print(f"E.g. Testing with ['shumai', 'longjing', 'veggies', 'custard bun']: {has_one_cup_two_pieces(menu, ['shumai', 'longjing', 'veggies', 'custard bun'])} (should be True)")

print("\n\nProblem 6.2\n\n")

# Problem 6.2: implement get_total_price (10 points).
##### Helper function (DO NOT MODIFY) #####
def get_price_by_food(menu, food_name):
    dim_sum_names = [item[0] for item in menu]
    idx = dim_sum_names.index(food_name)
    return menu[idx][2]
##### Helper function (DO NOT MODIFY) #####

def get_total_price(menu, order):
    total_price = 0
    for name in order:
        total_price += get_price_by_food(menu, name)

    if has_one_cup_two_pieces(menu, order):
        total_price *= 0.8

    return round(total_price, 2)

print(f"E.g. Testing with ['shumai', 'longjing']: {get_total_price(menu, ['shumai', 'longjing'])} (should be 46)")
print(f"E.g. Testing with ['shumai', 'longjing', 'veggies']: {get_total_price(menu, ['shumai', 'longjing', 'veggies'])} (should be 50.4)")