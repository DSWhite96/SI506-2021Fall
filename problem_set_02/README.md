# SI 506: Problem Set 02
## This week's Problem Set

This week's problem set focuses on sequence indexing and slicing, list methods, string methods, and formatting values as strings using formatted string literals (f-strings).

## Background
2021 saw the rise of "Meme Stocks". These stocks saw a meteoric rise in their stock price, not due to their financial performance or strong fundamentals, but rather due to their increasing popularity on social media platforms like Reddit. All prices have been gathered through Google Finance.

## 1.0 Problem 01 (10 points)

During the first five (5) weeks of 2021, GameStop's [NYSE: GME] Friday closing prices (in USD) were **15.84, 35.50, 65.01, 325.00, 63.77**. We provide a list of prices named `gme_prices`.

1. What is the maximum value in `gme_prices`? Assign the maximum value to a variable
   named `price_max`.

   :bulb: Use the appropriate built-in function to return the max value in the list.

2. What's the maximum value's index in `gme_prices`? Assign the maximum value's index to a variable
   named `price_max_index`.

   :bulb: Use the appropriate list method to return the index value.

3. For the week of 02/12, GameStop's Friday closing price (in USD) was **52.40**. Add this value to the end of the list using the appropriate list method.

4. An error exists in the data. The first element of `gme_prices` is actually **17.69** instead of
   **15.84**. Please update the list with the correct value using list indexing.

## 2.0 Problem 02 (10 points)

During the last five (5) weeks (from 08/13 - 09/10), AMC's [NYSE: AMC] Friday closing prices (in USD) were **33.47, 34.41, 40.84, 44.02, 50.16**.

1. Create a list called `amc_prices`. Add the Friday closing prices to `amc_prices` in chronological
   order.

2. Use list indexing to return the latest closing stock price in `amc_prices` and assign it to a variable named `amc_prices_latest`.

3. Extract the prices from the last **three (3)** weeks. Use list slicing to assign the values from the last three weeks to a new list named `amc_prices_last_three`.

## 3.0 Problem 03 (10 points)

We have provided a string named `pltr_prices` with the Friday closing prices of Palantir Technologies Inc. [NYSE: PLTR] for last 6 weeks, separated by a dash (`-`). Note, that at the start and the end of `pltr_prices` there are two spaces.

Use string methods to create a list of strings
that matches the list `['21.82', '24.90', '24.01', '25.71', '26.64', '26.28']`. Assign the list of strings to
a variable named `pltr_prices_list`.

   :bulb: Use the appropriate `str` methods to achieve this task.

## 4.0 Problem 04 (20 points)

In this problem, we have provided you with a list called `dates`.

1. Use the appropriate `list` method to reverse this list, so that the dates are in order.

2. Use the `str.join()` method on this reversed list to create a new string called `dates_str` where each date is separated by a pipe symbol (`|`).

In other words, the value assigned to `dates_str` must match the string:

`'August 6th|August 13th|August 20th|August 27th|September 3rd|September 10th'`

## 5.0 Problem 05 (20 points)

1. Use a formatted string literal (f-string) to generate a string named `pltr_highest` that summarizes
   the weekly end date, share price for Palantir, and share price for AMC for the week that saw the highest closing price for Palantir over the last five weeks.

   The value assigned to `pltr_highest` _must_ implement the following text format:

    ```commandline
    In the week ending on < date >, Palantir closed with a price of $< price_1 > and AMC closed with a price of $< price_2 >.
    ```

    :exclamation: Use of `< some_var >` indicates that a variable expression is to be inserted into the
    string.

   :bulb: `date` is an element of `dates`, `price_1` is an element of `pltr_prices_list`, while `price_2`
   is an element of `amc_prices`.

2. Similarly, use a formatted string literal (f-string) to generate the string `amc_highest` that
   summarize the weekly end date, share price for Palantir, and share price for AMC for the week that saw the highest closing price for AMC over the last five weeks. Use
   the same text format as described above in problem 5.1.

## 6.0 Problem 06 (20 points)

Use **slicing** to reverse the list `dates` and assign it to a list named `dates_reversed`.

   :exclamation: Remember that `dates` was reversed in an earlier problem, so the expected output of should match the original `dates` list that we provided.

## 7.0 Problem 07 (10 points)

Use **slicing** to return every **other** element of `dates_reversed`, starting with the first element. Assign this return value to a list named `every_other_date`.