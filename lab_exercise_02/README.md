# SI 506: Lab Exercise 02

## This week's Lab Exercise

This week's lab exercise includes five (5) problems, which focus on strings and list operations.

## Background

2021 is an incredible year from the perspective of the stock market. Stocks in different industries have been affected and have gone through many ups and downs. Traditional industries, especially the traditional motor vehicle stocks, have changed a lot. For this lab, you will worked with a list of stock prices from five automobile companies. After completing this lab you will be able to show different stock prices of different automobile companies on May 1st, 2021.

## 1.0 Problem 01 (4 points)

The variable `companies` is a string with different motor companies followed by their stock prices individually. Replace the punctuation "," with ":" and assign the new string object to a variable named `company_stocks`.

:bulb: each company should be followed by a colon, then the stock price of this company

## 2.0 Problem 02 (4 points)

Create a list by splitting the string, `company_stocks`. Assign this list to a new variable named `automotive_stocks`.

:bulb: Watch for spaces when using the `str.split()` method, the resultant list elements must have one space after splitting on the semicolon "; ".

## 3.0 Problem 03 (4 points)

Use the built-in list function, `len(<list>)`, to get how many elements in this list. Create a new variable named `companies_num` and assign the value to it.

## 4.0 Problem 04 (4 points)

Build an formatted string literal (f-string) using the variable `companies_num`. Create a variable named `statement` and assign the string to it.

The f-string has the following output:

``` "In this list, there are 5 automotive companies and their stock prices on May 1st, 2021." ```

## 5.0 Problem 05 (4 points)
Use list slicing to assign the first three companies and their stock prices in this list. Created a variable named `three_lowest_companies` and assign the value to it.
