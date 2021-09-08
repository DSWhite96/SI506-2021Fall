
# SI 506: Lab Exercise 01

## This week's Lab Exercise

This week's lab exercise includes seven (7) problems that focus on comments, variable
assignment, using built-in functions, and basic arithmetic operations.

## Background

Every summer, the International Center at the University of Michigan holds some social events for incoming students to join in. Those social events are meant to give students opportunities to make friends and learn more about life in Ann Arbor.

## 1.0 Problem 01 (3 Points)

Comment out (i.e., add a hash sign (#) as the first character on the line) the variable name and
assigned value that violates Python's variable naming rules and conventions.

:bulb: You may need to comment out more than one (1) of the variables.

## 2.0 Problem 02 (2 Points)

Create a list. Name the list `events` and append those variables that are not
commented out in Problem 01 to the list.

:bulb: You must employ **exactly the same** list name provided in the instructions in order to pass
the auto grader.

## 3.0 Problem 03 (3 Points)

Use the built-in function `len()` to return the number of elements in the list `events`. Assign
the return value to a new variable named `num_events`.

:bulb: You __must__ use the built-in function `len()` to get the length of `events` in order to pass
the auto grader.

## 4.0 Problem 04 (3 Points)

Use the built-in function `type()` to return the data type of  `num_events`. Assign
the return value to a new variable named `data_type`.

:bulb: You __must__ use the built-in function `type()` to get the data type of `num_events` in order to pass
the auto grader.

## 5.0 Problem 05 (3 Points)

The variables, `sonic_attended` (the number of students who attended the Sonic Lunch Event), `central_tour_attended` (the number of students who attended the central campus tour), `north_tour_attended` (the number of students who attended the north campus tour), `kerry_town_attended` (the number of students who attended the Kerrytown tour) all have the student populations assigned to them as an integer. Calculate the total number of students who participated in these events by adding all four variables and assigning the value to a new variable named `total_students`.

## 6.0 Problem 06 (3 Points)

Calculate the average size of the events by using the `total_students` variable computed in Problem 05 and divide it by the number of events. Assign the value to a new variable named `avg_event_size`

:bulb: Consider using **floor division** and the pre-defined variable `num_events`.

## 7.0 Problem 07 (3 Points)

Previously you created a list by appending the valid variables in Problem 02.
Create another list by using the string method `str.split()` to change `free_gifts`, a list of gifts that the international center gave to students in a string format, to a list type. Assign the return value to `gifts`.

:bulb: You __must__ use the string method `str.split()` in order to pass
the auto grader.
