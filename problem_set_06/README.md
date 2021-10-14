# SI 506: Problem Set 06

## This week's Problem Set

This week's problem set focuses on files, functions, nested loops, tuples, and flow control using the main function.

## Background

This week, we will be working with data concering popular shows on the streaming services Netflix and Disney Plus. In `netflix_data.csv` and `disney_data.csv`, we have the `Title`, `Creator(s)`, and `Genre(s)` of ten shows from each streaming service. In `netflix_ratings.csv` and `disney_ratings.csv`, we have the `Title` of each show along with its rating on the `Internet Movie Database (IMDb)`.

:exclamation: WARNING: When submitting to the autograder, make sure that any undefined variables in the return statement of `main()` are initalized to zero (`0`). The autograder will not run unless these variables have a value.

## Problem 01 (10 points)
1. Define a function called `read_csv()` that defines two parameters:

    `filepath` (`str`): A string that represents the path and name of a csv file

    `encoding` (`str`): A str representing the character encoding of the file

    This function should load a csv file and return its contents in a list of lists.

    :bulb: `encoding` should have a `default value` of `'utf-8'`

2. Inside of the `main function`, use `read_csv()` to load `netflix_data.csv`, `disney_data.csv`, `netflix_ratings.csv`, and `disney_ratings.csv` into variables called `netflix_data`, `disney_data,` `netflix_ratings`, and `disney_ratings` respectively.

## Problem 02 (20 points)
Currently, for each streaming service we have the data stored in two separate lists, let's combine this data.
1. Define a function called `add_ratings()` that defines two parameters:

    `shows` (`list`): A list of shows

    `ratings` (`list`): A list of IMDb ratings for the shows

    This function should create a `deep copy` of the `shows` list and append to it a new column called `IMDb Rating`. This function should then loop through the `copy of shows` and append the rating of each show in the list. The function should then return the `copy of shows`.

    :bulb: There are several ways to approach this problem, one good way would be to use `nested loops` (consider `Problem Set 05`).

2. Inside of the `main function`, use `add_ratings()` to create two new variables called `netflix_data_with_ratings` and `disney_data_with_ratings`. `netflix_data_with_ratings` should combine `netflix_data` and `netflix_ratings` and `disney_data_with_ratings` should combine `disney_data` and `disney_data_with_ratings`.

## Problem 03 (15 points)
1. Define a function called `clean_show_data` that defines one parameter:

    `shows` (`list`): A list of shows

    This function should create a `deep copy` of the `shows` list and then loop through it to clean the data in the following ways:

    1. Convert the numbers into floats
    2. Convert the Creator(s) and Genre(s) strings into lists

    The function should then return the `copy of shows`.

    :bulb: Notice how the `Creator(s)` and `Genre(s)` are divided. What string method can you use to separate them?

2. Inside of the `main function`, use `clean_show_data()` to clean the `netflix_data_with_ratings` and `disney_data_with_ratings` lists and assign the return values of those calls to variables called `clean_netflix_data` and `clean_disney_data` respectively.

## Problem 04 (10 points)
1. Define a function called `get_highest_rated_show()` that defines one parameter:

    `shows` (`list`): A list of shows

    This function should use the `accumulator pattern` to loop through the list of shows and return a tuple that has the `Title` and `Creator(s)` of the show with the highest `IMDb Rating`.

2. Inside of the `main function`, use `get_highest_rated_show()` to define two new variables, one called `best_netflix_show` that should have the `Title` and `Creator(s)` of the highest rated Netflix show and one called `best_disney_show`, which should have the highest rated Disney Plus show.

## Problem 05 (25 points)
1. Define a function called `filter_by_genre()` that defines two parameters:

    `shows` (`list`): A list of shows

    `genre` (`str`): A string representing a genre of shows

    This function should loop through the `shows` list and return a list of every show that matches the given `genre` that was passed in.

    :bulb: Remember to be aware of `case sensitivity` when performing string comparisons. There are once again different ways to approach this problem. One approach that you can consider is the one used in `Lab Exercise 05`.

2. Inside of the `main function` declare a variable called `sci_fi_shows` that will become a list of lists. The first list should be a `header row` with the following columns: `Title`, `Creator(s)`, `Genre(s)`, `IMDb Rating`. Then use the `filter_by_genre()` function to add all of the `Science Fiction` shows from both the `clean_netflix_data` and `clean_disney_data` lists.

    :bulb: You will need to call this function twice and use a certain list method to add the shows to the `sci_fi_shows` list.

## Problem 06 (10 points)
We are going to write the `Science Fiction` shows into a new csv file, but before we do that, we first need to put the `Creator(s)` and `Genre(s)` back into a format that looks nicer in a csv file.
1. Define a function called `stringify()` that defines one parameter:

    `shows` (`list`): A list of shows

    This function should create a `deep copy` of the shows list. This function should then loop through the `copy` and convert the `Creator(s)` and `Genre(s)` of each show back into strings. Each value in the `Creator(s)` and `Genre(s)` lists should be separated by a `'/'`. The function should then return this `copy of shows`.

    :bulb: Which string method can you use to bring a list together into one string?

2. Inside of `main()`, use `stringify()` to convert the data inside of `sci_fi_shows` into a better format for a csv file. Assign the return value of this function call to a variable called `stringified_sci_fi_shows`.

## Problem 07 (10 points)
1. Define a function called `write_csv()` that defines two parameters:

    `filepath` (`str`): A string with the path of the file to be written

    `data` (`list`): A list with content that will be written to a file

    Each list inside of `data` should be written to the file in `filepath`.

    :bulb: When opening this file, make sure to give the `open()` function a `keyword argument` of `newline=''` in order to prevent your file from having an empty line between each row.

2. Finally, inside of `main()`, call `write_csv()` to create a file called `sci_fi_shows.csv` using the data from `stringified_sci_fi_shows`.
