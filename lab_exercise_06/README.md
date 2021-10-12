# SI 506: Lab Exercise 06

## This week's Lab Exercise

This week's lab exercise includes five (5) problems focused on creating functions, reading Docstrings, writing to a CSV file, and leveraging the `main()` function.

## Data description

During the COVID-19 pandemic, owning indoor houseplants has become increasingly popular. Although houseplants can be therapeutic and a great way to bring nature inside, they can be difficult to care for. Knowing your houseplant's light, water, and soil preferences is essential to getting it the care it needs. This week's lab includes two lists of nested lists assigned to the variable `houseplants` and `new_houseplants`, each of which includes some popular houseplants and their characteristics.

## 1.0 Problem 01 (4 Points)

1. Create a variable called `houseplants_filepath` and assign the path of `houseplants.csv` file to it. Inside of the `main()` function, call `read_csv()` passing to it the argument `houseplants_filepath`. Assign the return value to a variable called `houseplants`.

   ```python
   houseplants_filepath = None

   houseplants = None
   ```

2. Create a variable called `new_houseplants_filepath` and assign the path of `new_houseplants.csv` file to it. Inside of the `main()` function, call `read_csv()` passing to it the argument `new_houseplants_filepath`. Assign the return value to a variable called `new_houseplants`.

   ```python
   new_houseplants_filepath = None

   new_houseplants = None
   ```

3. Uncomment the accompanying `print()` functions and run your code. You _must_ return the following lists:
   ```python
   [
   ['Money Tree Plant', '18 feet', 'Low', 'Full sun', '54.99'],
   ['Lily', '21 feet', 'Low', 'Part shade', '54.99'],
   ['Dieffenbachia', '12 feet', 'Low', 'Full sun', '39.99'],
   ['Gardenia', '12 feet', 'Medium', 'Part shade', '54.99'],
   ['Snake', '23 feet', 'Low', 'Part shade', '49.99'],
   ['Baby Rubber', '8 feet', 'Low', 'Part shade', '39.99'],
   ['Devils Ivy', '12 feet', 'Medium', 'Part shade', '39.99'],
   ['Fiddle Leaf Fig', '18 feet', 'Medium', 'Full sun', '54.99'],
   ['Majesty Palm', '46 feet', 'Medium', 'Part shade', '119.99'],
   ['Swiss Cheese', '12 feet', 'Low', 'Full sun', '54.99']
   ]
   ```

   ```python
   [
   ['Lucky Bamboo/', '21 feet/', 'Medium/', 'Part shade/', '59.99/'],
   ['Snake/', '23 feet/', 'Low/', 'Part shade/', '49.99/'],
   ['Fall Mum/', '18 feet/', 'Medium/', 'Full sun/', '39.99/'],
   ['Sago Palm/', '15 feet/', 'Medium/', 'Full sun/', '44.99/'],
   ['Snake/', '23 feet/', 'Low/', 'Part shade/', '49.99/']
   ]
   ```


## 2.0 Problem 02 (2 Points)

1. Read the `create_header` function's Docstring and implement the function by replacing the
   `pass` statement with your code block.

2. Return to the `main()` function and test your implementation by calling the function and passing the string 'header_string' as argument.

3. Assign the return value to the variable `header`.

   ```python
   header = None
   ```

4. Uncomment the accompanying `print()` function and run your code. You _must_ return the following list:

   ```python
   ['Name', 'Max height', 'Water', 'Sunlight', 'Price']
   ```

## 3.0 Problem 03 (2 Points)

1. Read the `add_plants()` function's Docstring and implement the function by replacing the `pass` statement with your code block.

2. Return to the `main()` function and test your implementation by calling the function and passing the string 'houseplants' and 'new_houseplants' as arguments.

3. Assign the return value to the variable `all_houseplants`.

   ```python
   all_houseplants = None
   ```

4. Uncomment the accompanying `print()` function and run your code. You _must_ return the following list:

   ```python
   [
   ['Money Tree Plant', '18 feet', 'Low', 'Full sun', '54.99'],
   ['Lily', '21 feet', 'Low', 'Part shade', '54.99'],
   ['Dieffenbachia', '12 feet', 'Low', 'Full sun', '39.99'],
   ['Gardenia', '12 feet', 'Medium', 'Part shade', '54.99'],
   ['Snake', '23 feet', 'Low', 'Part shade', '49.99'],
   ['Baby Rubber', '8 feet', 'Low', 'Part shade', '39.99'],
   ['Devils Ivy', '12 feet', 'Medium', 'Part shade', '39.99'],
   ['Fiddle Leaf Fig', '18 feet', 'Medium', 'Full sun', '54.99'],
   ['Majesty Palm', '46 feet', 'Medium', 'Part shade', '119.99'],
   ['Swiss Cheese', '12 feet', 'Low', 'Full sun', '54.99'],
   ['Lucky Bamboo', '21 feet', 'Medium', 'Part shade', '59.99'],
   ['Fall Mum', '18 feet', 'Medium', 'Full sun', '39.99'],
   ['Sago Palm', '15 feet', 'Medium', 'Full sun', '44.99']
   ]
   ```

## 4.0 Problem 04 (4 Points)
1. Read the `count_avg_height()` function's Docstring and implement the function by replacing the `pass` statement with your code block.

2. Return to the `main()` function and test your implementation by calling the function and passing the list `all_houseplants` as the argument.

3. Assign the return value to the variable `avg_height`.

   ```python
   avg_height = None
   ```

4. Uncomment the accompanying `print()` function and run your code. You _must_ return the collect integer value to pass the autograder test.

## 5.0 Problem 05 (4 Points)

1. Read the `filter_large_plants()` function's Docstring and implement the function by replacing the `pass` statement with your code block.

2. Return to the `main()` function and test your implementation by calling the function and passing the list `all_houseplants` and as `avg_height` arguments.

3. Assign the return value to the variable `large_plants`.

   ```python
   large_plants = None
   ```

4. Uncomment the accompanying `print()` function and run your code. You _must_ return the following list:

   ```python
   [
    ['Lily', '21 feet', 'Low', 'Part shade', '54.99'],
    ['Snake', '23 feet', 'Low', 'Part shade', '49.99'],
    ['Majesty Palm', '46 feet', 'Medium', 'Part shade', '119.99'],
    ['Lucky Bamboo', '21 feet', 'Medium', 'Part shade', '59.99']
   ]
   ```

## 6.0 Problem 06 (4 Points)

1. Read the `write_csv()` function's Docstring and implement the function by replacing the `pass` statement with your code block.

2. Return to the `main()` function and test your implementation by calling the function and passing three arguments to it.

* filepath (str): Create a new file named "all_houseplants.csv" in current directory
* data (list): the variable `all_houseplants` we created
* headers (list): the variable `header` we created

