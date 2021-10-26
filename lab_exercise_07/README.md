# SI 506: Lab Exercise 07

## This week's Lab Exercise

This week's lab exercise includes five (5) problems that focus on the dictionary, functions, and conditional statements.

## Background

For this lab, you are provided with a list of dictionaries that includes information about restaurants located in downtown Ann Arbor.
The dictionaries within the list contain the restaurant's name, location, rating, number of reviews, and category.
You will use `for` loops, `conditional statements`, and
functions to complete the problems.

```python
restaurants = [
    {'Name': 'Frita Batidos', 'Location': '117 W Washington St', 'Rating': 4.5, 'Reviews': 1871, 'Category': 'Burgers'},
    {'Name': "Zingerman's Delicatessen", 'Location': '422 Detroit St', 'Rating': 4.0, 'Reviews': 2224, 'Category': 'Delis'},
    {'Name': "Scorekeepers", 'Location': '310 Maynard St', 'Rating': 2.5, 'Reviews': 59, 'Category': 'Burgers'},
    {'Name': 'Rich Jc Korean Restaurant', 'Location': '1313 S University Ave', 'Rating': 4.0, 'Reviews': 183, 'Category': 'Korean'},
    {'Name': 'Tomukun Noodle Bar', 'Location': '505 E Liberty St Ste 200', 'Rating': 4.0, 'Reviews': 773, 'Category': 'Noodles'},
    {'Name': "Sava's", 'Location': '216 S State St', 'Rating': 4.0, 'Reviews': 1195, 'Category': 'American'},
    {'Name': "Krazy Jim's Blimpy Burger", 'Location': '304 S Ashley St', 'Rating': 3.5, 'Reviews': 231, 'Category': 'Burgers'},
    {'Name': "Joe's Pizza", 'Location': '1107 S University Ave', 'Rating': 4.5, 'Reviews': 107, 'Category': 'Pizza'},
    {'Name': 'Hola Seoul', 'Location': '715 N University Ave', 'Rating': 4.0, 'Reviews': 98, 'Category': 'Korean'},
    {'Name': 'The Chop House', 'Location': '322 S Main St', 'Rating': 4.0, 'Reviews': 448, 'Category': 'Steakhouses'},
    {'Name': 'TK Wu', 'Location': '510 E Liberty St', 'Rating': 3.5, 'Reviews': 236, 'Category': 'Chinese'},
    {'Name': 'HopCat', 'Location': '311 Maynard St', 'Rating': 3.5, 'Reviews': 397, 'Category': 'Burgers'},
    {'Name': 'Lan City Noodle Bar', 'Location': '1235 S University Ave', 'Rating': 4.0, 'Reviews': 5, 'Category': 'Chinese'},
    {'Name': 'First Bite', 'Location': '108 S Main St', 'Rating': 5.0, 'Reviews': 104, 'Category': 'Burgers'}
]
```

## 1.0 Problem 01 (3 points)

1. Implement a function called `get_restaurants(category=None)` that can accept two parameters: `restaurants`, a list of dictionaries containing all restaurants' information; `category`, an optional parameter to specify a list of strings containing different categories of restaurants. This function should Loop over the `restaurants` list and return a list of strings containing the restaurants' names if the restaurants are in the specified category.

:bulb: If category is None return all restaurants' names. Otherwise return a subset of restaurants based on the category.

2. Inside of the `main()` function, call `get_restaurants()` passing to it the list argument `restaurants` and specify the category as `['Korean']`. Then assign the return value to a variable called `korean_restaurants`.

:bulb: After calling this function on `restaurants` and `['Korean']`, the output must be the following:

```python
['Rich Jc Korean Restaurant', 'Hola Seoul']
```

## 2.0 Problem 02 (4 points)

1. Implement a function called `get_most_reviewed_restaurant()` that accepts one parameter: `restaurants`, a list of dictionaries that containing information about restaurants. This function should loop over `restaurants` and check the value that belongs to the key `"Reviews"` to find the restaurant with the highest number of reviews. Create an empty dictionary inside the function. Assign the restaurant's name as a value to the key `"Name"` and assign the number of reviews as a value to the key `"Reviews"`. Return the dictionary.

2. Inside of the `main()` function, call `get_most_reviewed_restaurant()` passing to it the list argument `restaurants` and assign the return value to a variable called `most_reviewed_restaurant`.

:bulb: After calling this function on `restaurants`, the output must be the following:

```python
{'Name': "Zingerman's Delicatessen", 'Reviews': 2224}
```

## 3.0 Problem 03 (5 points)

1. Implement a function called `get_high_rating_restaurants()` that accepts two parameters: `restaurants`, a list of dictionaries; `category`, a list of strings that specifies the restaurant's category. Similar to Problem 02, loop over `restaurants` and check the values that belong to the key `"Rating"` and `"Category"` to find the restaurant with the rating of at least 3.5 in the specified categories. Create an empty dictionary inside of the function. Assign the restaurant's name as the key and its rating as the value to the dictionary. Return the dictionary.

2. Inside of the `main()` function, call `get_high_rating_restaurants()` passing to it the list argument `restaurants` and a list named `categories` that contains `"Burgers"` and `"Chinese"`. Assign the return value to a variable called `high_rating_restaurants`.

:bulb: After calling this function on `restaurants` and `categories`, the output should be the following:

```python
{'Frita Batidos': 4.5, "Krazy Jim's Blimpy Burger": 3.5, 'TK Wu': 3.5, 'HopCat': 3.5, 'Lan City Noodle Bar': 4.0, 'First Bite': 5.0}
```

## 4.0 Problem 04 (4 points)

1. Implement a function called `get_avg_rating()` that accepts one parameter: `high_rating_restaurants`, a dictionary that contains restaurants' names and ratings. Utilize the dictionary `values()` method to access the values in the dictionary and then calculate the average rating of restaurants in the dictionary. Return the average rating as a number.

2. Inside of the `main()` function, call `get_avg_rating()` passing to it the dictionary argument `high_rating_restaurants` returned from Problem 03. Assign the return value to a variable called `avg_rating`.

:bulb: After calling this function on `high_rating_restaurants`, the output _must_ be 4.0


## 5.0 Problem 05 (4 points)

1. Implement a function called `write_txt()` that accepts a file path and a list of dictionaries as arguments. Utilize the dictionary `items()` method and the built-in `list()` function to extract each dictionary's first three key-value pairs. Output the lists of tuples into a text file. The function _must_ write each list element to its own line in the file created.

2. Inside of the main() function, call the `write_txt()` function to create a file called `restaurants_info.txt` using the `restaurants` list.

:bulb: After calling this function, the text file generated _must_ look like the following:

```text
[('Name', 'Frita Batidos'), ('Location', '117 W Washington St'), ('Rating', 4.5)]
[('Name', "Zingerman's Delicatessen"), ('Location', '422 Detroit St'), ('Rating', 4.0)]
[('Name', 'Scorekeepers'), ('Location', '310 Maynard St'), ('Rating', 2.5)]
[('Name', 'Rich Jc Korean Restaurant'), ('Location', '1313 S University Ave'), ('Rating', 4.0)]
[('Name', 'Tomukun Noodle Bar'), ('Location', '505 E Liberty St Ste 200'), ('Rating', 4.0)]
[('Name', "Sava's"), ('Location', '216 S State St'), ('Rating', 4.0)]
[('Name', "Krazy Jim's Blimpy Burger"), ('Location', '304 S Ashley St'), ('Rating', 3.5)]
[('Name', "Joe's Pizza"), ('Location', '1107 S University Ave'), ('Rating', 4.5)]
[('Name', 'Hola Seoul'), ('Location', '715 N University Ave'), ('Rating', 4.0)]
[('Name', 'The Chop House'), ('Location', '322 S Main St'), ('Rating', 4.0)]
[('Name', 'TK Wu'), ('Location', '510 E Liberty St'), ('Rating', 3.5)]
[('Name', 'HopCat'), ('Location', '311 Maynard St'), ('Rating', 3.5)]
[('Name', 'Lan City Noodle Bar'), ('Location', '1235 S University Ave'), ('Rating', 4.0)]
[('Name', 'First Bite'), ('Location', '108 S Main St'), ('Rating', 5.0)]
```
