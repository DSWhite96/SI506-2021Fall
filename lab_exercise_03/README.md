# SI 506: Lab Exercise 03

## This week's Lab Exercise

This week's lab exercise includes five (5) problems that focus on loops and conditional statements.

## Background
The University Career Fair is coming up next month. This year's career fair will be held virtually,
and you can now find information about your potential employers through Handshake (https://umich.joinhandshake.com/).
For this lab, you are provided with a short list that includes some basic information about
the companies attending the career fair. The list contains several strings, which include names of companies,
headquarters' locations, the total number of employees, and the industries they are operating in. You are going
to use `for` loops, `conditional statements` to complete each problem.

```python
companies = [
    "Domino's, Ann Arbor, 14400, Food",
    "Fisher Investments, Camas, 3500, financial",
    "M&T Bank, Buffalo, 16840, Financial",
    "Dimensional Insight, Burlington, 102, Tech",
    "Bloomingdale's, New York, 6500, Retail",
    "Meijer, Grand Rapids, 70000, Retail",
    "CIL Management Consultants, Chicago, 189, Consulting"
]
```

## 1.0 Problem 01 (3 points)

Loop over the `companies` list and access the headquarter location of each company. Append each location to
the empty list named `locations` using list indexing.

## 2.0 Problem 02 (4 points)

Implement an `if` statement inside a `for` loop that identifies each company operating in the financial industry.
Loop over the `companies` list; if the company is operating in the financial industry, append the company's name to
the new list named `financial_co`.

:bulb: Python is a case-sensitive programming language. Be careful about the uppercase letters in the list.
You might need to use a built-in str method to convert the uppercase letters to lowercase when performing string matching.

## 3.0 Problem 03 (4 points)

Implement an `if` statement inside a `for` loop and count the number of companies operating in the retail industry.
Loop over the `companies` list; if the company is operating in the retail industry, increment the variable `count` by one (1).

:bulb: In this question, you might not need to convert the uppercase letters to lowercase. But it is a good practice
to make all letters the same case when performing a _case-insensitive_ string comparison.

## 4.0 Problem 04 (4 points)

Implement an `if-elif-else` statement inside a `for` loop and categorize the companies into three groups based on their sizes.
Loop over the `companies` list and if the number of employees in the company is less than 500 (exclusive), then append the
company's name to a list named `small_companies`. If the number of employees is larger than or equal to 5000 (inclusive),
then append the company's name to a list named `large_companies`. Otherwise, append the name of the company to a list
named `medium_companies`.

:bulb: Recall that you can utilize the built-in function print() to check on the values being appended to the small, medium, and large community lists. When satisfied with your conditional statements you can comment out print() or remove the expression from your code.

## 5.0 Problem 05 (5 points)

Implement an `if` statement inside a `for` loop to find the name of the largest company.
Loop over the `companies` list and check the number of employees that the company has. Assign the name of the largest
company to the new variable named `largest_company`.
