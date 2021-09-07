# SI 506: Problem Set 01

## This week's Problem Set

This week's problem set is going to focus on comments, values, types, variables, built-in functions and performing basic arithmetic operations using Python.

## Background

The city of Ann Arbor is home to several notable movie theaters. In addition to the more traditional movie theater, The Quality 16, Ann Arbor is also home to the historic landmarks the `Michigan Theater` and the `State Theater`.

## Problem 01 (15 points)
1. You have been provided with 4 lines of code, each attempting to declare a variable. Only two of these lines are valid variable declarations. Uncomment the statements that are valid varaible declarations.

    :bulb: "Uncomment" means to remove the leading hash symbol (`#`) from a line of code.

2. You should now have two variables, one called `michigan_theater` and one called `state_theater`. Create a list called `ann_arbor_theaters` that contains these two variables.

3. Using the built-in `type()` function, declare three variables called `michigan_theater_type`, `state_theater_type`, and `ann_arbor_theaters_type`.

    :bulb: These variables should store the types of `michigan_theater`, `state_theater`, and `ann_arbor_theaters` respectively.

## Problem 02 (20 points)
You have been provided with two `strings`, `movie_str_1` which represents the movies being shown this week at the `Michigan Theater` and `movie_str_2` which represents the movies being shown at the `State Theater`.
1. Using the `str` method `str.split()`, create a list called `michigan_theater_movies` that contains all of the titles of the movies in `movie_str_1`.
2. Using the `str` method `str.split()`, create a list called `state_theater_movies` that contains all of the titles of the movies in `movie_str_2`.

    :bulb: When splitting, note that the movie titles are separated by a comma followed by a space.

## Problem 03 (10 points)
Use the built-in `len()` function to determine the length of `michigan_theater_movies` and `state_theater_movies`. Assign these values to `num_movies_michigan` and `num_movies_state` respectively.

:bulb: If implemented correctly, your code should output the following to the terminal:

```terminal
The Michigan Theater is showing 8 movies this week.
The State Theater is showing 7 movies this week.
```

## Problem 04 (25 points)
The State Theater underwent a major rennovation in 2017. As a result, State Theater has four screens that contain `140`, `100`, `80`, and `50` seats each. These are reflected in the `integer` variables `theater_1_seats`, `theater_2_seats`, `theater_3_seats`, and `theater_4_seats`.
1. Using the addition operator (`+`) calculate the total number of seats across all four theaters at the State Theater. Assign the return value of this this arithmetic operation to the variable `total_seats_state`.

2. Using `floor division`, calculate the average number of seats for a screen at the State Theater. Assign the return value of this arithmetic operation to a variable called `avg_seats_state`.

    :bulb: Unlike in previous problems, this variable declaration has not been started for you. You must declare a variable called `avg_seats_state` and assign the return value of this calculation to that variable.

## Problem 05 (30 points)
The Michigan Theater contains two viewing screens, the main auditiorium, which seats 1610 people and the screening room, which seats 200 people.
1. Declare a variable called `main_auditorium_seats` and assign to it the `integer` value of `1610`.
2. Declare a variable called `screening_room_seats` and assign to it the `integer` value of `200`.
3. Using the `addition operator`, calculate the total number of seats between the two rooms and assign the return value of this calculation to a variable called `total_seats_michigan`.
4. Using `floor division`, calculate the average number of seats for a screen at the Michigan Theater. Assign the return value of this calculation to a variable called `avg_seats_michigan`.

:bulb: Much like in problem `4.2`, none of these variable declarations have been started for you. You must declare each of thse varaibles and assign the approriate values to them. Remember to format the variable assignments as discussed in class.