# SI 506: Lab Exercise 04

## This week's Lab Exercise

This week's lab exercise includes five (5) problems focused on creating functions.

## Data description

Last Tuesday was the Mid-Autumn Festival, a traditional festival in China. On that day, no matter where you are, you should come home and enjoy dinner and mooncake with your families. Mooncake, as a traditional dessert, has already become an important symbol of this festival. Also, there are so many other different kinds of desserts in China. Chinese people are good at making use of fruits and vegetables to make desserts, as a substitute for processed sugar. What’s more, desserts in China can be either sweet or savory. Today, you will be introduced to some traditional desserts in China. The desserts are assigned to the variable name `chinese_desserts`, which is a list of nested lists with each dessert's name and its corresponding calories.

## 1.0 Problem 01 (3 Points)

Create a function named `get_name()` that defines a single parameter named "dessert" (a `list`) and returns the name of the dessert.

After implementing the function, call `get_name()` and pass to it as an argument the first "dessert" in `chinese_desserts`. Assign the return value to a variable named `name`.

## 2.0 Problem 02 (3 Points)

Create a function named `get_calories()` that defines a single parameter named "dessert" (a `list`) and returns the number of calories in the dessert.

After implementing the function, call `get_calories()` and pass to it as an argument the second "dessert" in `chinese_desserts`. Assign the return value to a variable named `calories`.


## 3.0 Problem 03 (5 Points)

Create a function named `remove_dessert()` that defines two parameters:

* desserts (list): a `list` of _nested_ dessert lists
* dessert (list): a dessert to be removed

Before removing the dessert, this function must confirm that the dessert to be removed is an element in the desserts list. The function does not return a specified value.

Create a variable named `sun_cake` and assign the last dessert in the `chinese_desserts` list to it.

Call the `remove_dessert()` function in order to remove the `sun_cake` from the list `chinese_desserts`.


## 4.0 Problem 04 (6 points)

Create a function named `add_dessert()` that defines three parameters:

* desserts (list): a `list` of _nested_ dessert lists
* dessert (list): a dessert to add
* idx (int): the index position in the list of desserts where the dessert will be inserted. Assign a default value of `0`.

The function does not return a specified value.

Create a list with two elements ("Sweetheart Cake", 170) and assign this list to a new variable named `sweetheart_cake`.

Call the `add_dessert()` function and add the dessert `sweetheart_cake` to `chinese_desserts` in the *second* position.


## 5.0 Problem 05 (3 points)

Create a list with two elements ("Egg Tarts", 376) and assign this list to a new variable named `egg_tarts`.

Call the `add_dessert()` function and add the dessert `egg_tarts` to `chinese_desserts` in the *third* position using keyword arguments in _reverse order_.

:exclamation: You _must_ employ keyword arguments passed to the function in _reverse order_ in order to pass the auto grader. You must also style the keyword arguemnt assignment correctly (e.g., `keyword_arg=value`, not `keyword_arg = value`).
