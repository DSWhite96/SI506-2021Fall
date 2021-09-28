# SI 506: Problem Set 04

## This week's Problem Set

This week's problem set focuses on the `list` type, the accumulation pattern, and functions.

## Background

*Yum cha (飲茶)* is the Cantonese tradition of brunch involving Chinese tea and dim sum.
The practice is popular in Cantonese-speaking regions, such as Guangdong province, Hong Kong, and
Macau. Yum cha generally involves small portions of steamed, pan-fried/baked, or sweet dim sum
dishes. People often go to yum cha in large groups for family gatherings and celebrations (from
[Wikipedia](https://en.wikipedia.org/wiki/Yum_cha)).

## Part 1

In this part, you will help with designing and analyzing a Cantonese restaurant menu.
The `menu` list below contains the names of dim sums and Chinese teas, their categories, and their
prices in HKD (Hong Kong Dollars).

:exclamation: Note that the first element in the list is considered the "headers" element.

```python
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
    ["pu'er", "tea", 10]
]
```

## 1.0 Problem 01 (5 points)

Add a new item to the headers called `price (USD)`. Employing a `for` loop, convert the price of
each menu item in `menu` in HKD to USD (US Dollar) and append the converted value to each menu
item rounded to the second decimal place.

#### Requirements

1. The currency exchange rate is `1 HKD = 0.128 USD`.

2. You _must_ use the built-in [`round`](https://www.w3schools.com/python/ref_func_round.asp)
   function to round the price to two (2) decimal places. For example, rounding `3.584` two decimal
   places would result in a rounded value of `3.58`.

The mutated elements in `menu` will resemble the elements below:

```python
[
   ["name", "categories", "price (HKD)", "price (USD)"],
   ["short ribs with xo source", "steamed", 28, 3.58],
   ["pan-fried turnip cake", "Pan-fried/Baked", 22, 2.82],
   ...
]
```

:bulb: Remember to add the new headers element seperately.

## 2.0 Problem 02 (15 points)

In the *yum cha* culture, Cantonese restaurants normally categorize dim sums into grades in the menu
based on their price **in HKD**.

#### Requirements

1. Append a new item in the headers called `grade`.

2. Then categorize the dim sums into following grades employing a `for` loop and conditional
logic:

   * "superb": when the price is greater than 25 HKD
   * "top": when the price is greater than 20 HKD and smaller than or equal to 25 HKD
   * "good": when the price is smaller than 20 HKD
   * "tea": when the dim sum is tea

The mutated elements in `menu` will resemble the elements below:

```python
[
   ["name", "categories", "price (HKD)", "price (USD)", "grade"],
   ["short ribs with xo source", "steamed", 28, 3.58, "superb"],
   ...
   ["pu'er", "tea", 10, 1.28, "tea"]
]
```

:bulb: Remember to add the new headers element seperately.

## 3.0 Problem 03 (20 points)

In this problem we are interested in which dim sum has the highest price and which dim sum has the
lowest. We have created four variables for you: `max_names`, `max_price`, `min_names`, and
`min_price`. Assign the correct values to the four variables employing a `for` loop and
conditional logic.

:bulb: feel free to employ two `for` loops to solve this problem.

#### Requirements

1. Note that there might be multiple dim sums that have the same lowest price, which is why
`max_names` and `min_names` are lists. You must return all dim sum names of the max/min price.

2. You _must_ exclude the category of `"tea"` from the comparison (use `continue` in the
`for` loop to skip `"tea"` menu items).

3. If either a new max price or min price is encountered in either of your loops be sure
   to _clear_ any existing elements in `max_names` or `min_names` (the new max or min priced menu
   item trumps the previous max / min priced menu item(s)). There exists a handy `list` method that
   you can employ to accomplish the task.

## 4.0 Problem 04 (10 points)

In this problem we are interested in the _average_ price of dim sums in the category `"steamed"`.
We have created a variable for you called `steamed_avg_price`. Assign the correct
value to this variable.

#### Requirements

1. Employ a `for` loop, conditional logic, and the accumulator pattern when
working with the menu items.

2. Compute the total price and total count of *steamed* dim sums _first_ before calculating
the average price (average price = total price / total count) in HKD.

## Part 2

In Cantonese culture, `yat jung leung gin (一盅兩件)` is a slang term that translates literally as
**"one cup two pieces"** (a.k.a one cup of tea and two dim sums). In the past when dim sum was not
bite-size, one cup with two pieces constituted a sufficient brunch for one person
(from [Wikipedia](https://en.wikipedia.org/wiki/One_bowl_with_two_pieces)).

## 5.0 Problem 05

Assume Alice is your friend living in the U.S. She is interested in knowing what constitutes
"one cup two pieces". You will implement a function that determines whether three
given dishes is a valid "one cup two pieces". For example, `short ribs with xo source`,
`pan-fried turnip cake`, and `longjing` (tea) is a valid combination.

To solve this problem, we will decompose it into two parts.

### 5.1  Problem 5.1 (15 points)

First, implement a function named `get_category_by_food` that defines two parameters:

1. `menu` (`list`): represents a restaurant menu
2. `food_name` (`str`): the name of a menu item

#### Requirements

1. The function _must_ traverse the passed in menu, filter on the menu item's `food_name`, and
   return the matching menu item's `category`.

2. Utilize the accumulator pattern when implementing this function.

3. Use `break` to exit the `for` loop once you match the food name.

#### Examples

* Calling `get_category_by_food(menu, 'shumai')` will return the category `"steamed"`.

### 5.2  Problem 5.2 (10 points)

Second, we have provided a helper function named `is_one_cup_two_pieces` that defines two
parameters:

1. `menu` (`list`): represents a restaurant menu
2. `foods` (`list`): list of three food names

The function computes whether or not the three provided food names that correspond to menu items
constitute a valid "one cup two pieces". The function will return `True` if _any_ of the three
conditions returns `True`; otherwise it returns `False`.

:exclamation: The function `is_one_cup_two_pieces` delegates the task of retrieving each menu
item's category to the function named `get_category_by_food` implemented earlier. If
`get_category_by_food` is implemented incorrectly the helper function `is_one_cup_two_pieces` will
compute its values incorrectly.

#### Examples

* Calling `is_one_cup_two_pieces(menu, 'shumai', 'pan-fried turnip cake', 'longjing')` returns `True`.

## 6.0 Problem 06

To encourage the tradition of one cup two pieces, the restaurant decides to give a `20%` discount if
the customer orders a correct combination of one cup two pieces. In this problem, you will help
implement a function that can calculate the total price for any given order.

Decompose this problem into two parts.

### 6.1  Problem 6.1 (15 points)

First, implement a function called `has_one_cup_two_pieces` that defines two parameters:

1. `menu` (`list`): represents a restaurant menu
2. `order` (`list`): a list of menu item food names

#### Requirements

1. Design the function to return `True` if the order contains a combination of "one cup two pieces"
   or `False` when the order contains no combination of "one cup two pieces".

2. When implementing this function delegate the task of retrieving each menu item's category to the
   function named `get_category_by_food`.

#### Examples

* Calling `has_one_cup_two_pieces(menu, ["shumai", "longjing"])` will return `False`.
* Calling `has_one_cup_two_pieces(menu, ["shumai", "longjing", "veggies"])` returns `True`.
* Calling `has_one_cup_two_pieces(menu, ["shumai", "barbecued pork bun", "veggies", "Malay sponge cake"])` will return `False`.
* Calling `has_one_cup_two_pieces(menu, ["shumai", "longjing", "veggies", "pu'er", "custard bun"])` will return `True`.

### 6.2 Problem 6.2 (10 points)

Second, implement a function named `get_total_price` that defines two parameters:

1. `menu` (`list`): represents a restaurant menu
2. `order` (`list`): a list of menu item food names

#### Requirements

1. Design the function to compute the total price of the order in HKD and then return the value to
   the caller.

2. Delegate the task of retrieving each menu item's price to the helpert function named
   `get_price_by_food` (provided).

3. If the order contains a correct combination of "one cup two pieces", the function will provide a
   `20%` discount on the total price. Delegate the task of identifying "one cup two pieces"
   combinations to the function named `has_one_cup_two_pieces`.

4. Use the built-in [`round`](https://www.w3schools.com/python/ref_func_round.asp) function to
   round the total price to two decimal places.

#### Examples

* Calling `get_total_price(menu, ["shumai", "longjing"])` will return `46`.
* Calling `get_total_price(menu, ["shumai", "longjing", "veggies"])` will return `50.4`
