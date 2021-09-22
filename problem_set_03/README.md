# SI 506: Problem Set 03

## This week's Problem Set

This week's problem set focuses on loops and conditional statements. It also includes practice on previous topics (e.g. list methods, string methods, method chaining, slicing, and indexing).

## Background

The University Career Center will be hosting virtual career fairs on October 1, October 8, and October 13. More details are available through [Handshake](https://umich.joinhandshake.com/). This problem set includes two sequences related to the companies who will attend the career fair. You will be asked to create subsets of the sequences using slicing, `for` loops, and `while` loops. Salary information was gathered from [Glassdoor](https://t.co/bfwwucAv1t?amp=1).

## Part 1

The `day_1` list provided contains the names of some companies attending the October 1 session of the career fair. These are only some of the companies which are looking to hire Masters students.

```python
day_1 = [
   'Kennedy & Company Education Strategies, LLC',
   'Congressional Research Service',
   'M&T Bank',
   'MassMutual Michigan Metro',
   'Alliance for Catholic Eduation (ACE Teaching Fellows)',
   'enFocus',
   'Buckle',
   'Defense Finance and Accounting Services (DFAS)',
   'AllianceBernstein',
   "Domino's",
   'Epic',
   'Fisher Investments',
   'goPuff dba GoBrands Inc.',
   'Govern For America',
   'Guidehouse',
   'Maxim Integrated Now Part of Analog Devices',
   'Equitable Advisors',
   'Exelon Corporation'
   ]

```

Use code to create the outputs requested below.

### 1.0 Problem 01 (7 points)

1. Sort the day_1 `list` in ascending order without creating a new variable.

   :bulb: There are two `list` methods, which can be used for sorting. Use the in-place method.

2. What are the companies that start with the letter 'A'? Assign the slice to the variable `a_companies`.

   :bulb: Use slicing notation (not the slice method) to create the desired output.

3. Using a built-in function, return the number of companies that start with 'A'. Assign this integer to the variable `num_a_companies`.

### 2.0 Problem 02 (14 points)

This way of deriving subsets has its limits. One issue is that sorting alone may not generate the desired order. As you learned last week and can see from the sorted `day_1` list, lowercase and capitalized strings are sorted separately. It would take multiple slices to get all of the companies that start with 'e' and 'E', for example. In this problem, let's use a `for` loop to return a subset instead.

:bulb: Can you think of other situations where sorting and slicing a sequence might not be an ideal approach?

1. Initialize an empty list named `e_companies`. Use a `for` loop and conditional statement to populate the empty list with companies that start with 'e' or 'E'. Use method chaining to perform *case-insensitive* filtering on the company name.

   :bulb: When performing a case-insensitive comparison of two strings, convert the strings to lower case before performing the comparison.

2. Initialize an integer `num_e_lower`. Use a `for` loop and an `if` statement to count the number of elements in the `e_companies`list that start with lower case.

   :bulb: Implement the accumulator pattern and addition assignment. Employ the appropriate `str` method. It must be generic (i.e. 'e' should not be one of its arguments). Indexing may be required to access the company name within each list.

## Part 2

We have provided a multi-line string named `salaries`. This string contains The name of a company, a job position at the company, and an average salary at the company. In the following problems, you will be asked to convert the string to a list and extract salary information.

```python
salaries = """Domino's|Graphic Designer|39000
   Fisher Investments|Analyst|95916
   Department of Health & Human Services|Technical Writing Specialist|76703
   Splunk|Front-End Engineer|139554
   Domino's|Senior Technical Writer|98000
   Department of Health & Human Services|Analyst|71754
   Domino's|Digital Specialist|93000
   Splunk|Product Manager|134633
   Dimensional Insight|Consultant|69359
   Splunk|Customer Success Manager|125720
   Edgeworth Economics|Consultant|80190
   Edgeworth Economics|Computer Systems Engineer|98495
   Domino's|Analyst|77937
   Fisher Investments|Research Associate|79141
   Splunk|Data Analyst|117652
   """
```

### 3.0 Problem 03 (13 points)

1. Use the appropriate string method to convert `salaries` into a list of strings. Assign this list to the variable `sal_strings`.

   :bulb: Be sure to use the method that separates the lines of a **multi-line** string into list elements. The output should resemble the following:

   ```python
   [
      "Domino's|Graphic Designer|39000",
      'Fisher Investments|Analyst|95916',
      'Department of Health & Human Services|Technical Writing Specialist|76703',
      'Splunk|Front-End Engineer|139554',
      "Domino's|Senior Technical Writer|98000",
      'Department of Health & Human Services|Analyst|71754',
      "Domino's|Digital Specialist|93000",
      'Splunk|Product Manager|134633',
      'Dimensional Insight|Consultant|69359',
      'Splunk|Customer Success Manager|125720',
      'Edgeworth Economics|Consultant|80190',
      'Edgeworth Economics|Economic Consultant|80645',
      'Edgeworth Economics|Computer Systems Engineer|98495',
      "Domino's|Analyst|77937",
      'Fisher Investments|Research Associate|79141',
      'Splunk|Data Analyst|117652'
   ]
   ```

2. For this problem, you will be creating a nested list (a.k.a. a list of lists).

Initialize an empty list called `sal_lists` that you will populate with elements from `sal_strings`. To create this nested list, apply a `str` method to each element in `sal_strings` using a `for` loop. This method must separate the company name, job role, and salary and output them as a list comprising three elements. Append these three-element lists to `sal_lists`.

The output should resemble the following.

```python
   [
      ["Domino's", 'Graphic Designer', '39000'],
      ['Fisher Investments', 'Analyst', '95916'],
      ['Department of Health & Human Services', 'Technical Writing Specialist', '76703'],
      ['Splunk', 'Front-End Engineer', '139554'],
      ["Domino's", 'Senior Technical Writer', '98000'],
      ['Department of Health & Human Services', 'Analyst', '71754'],
      ["Domino's", 'Digital Specialist', '93000'],
      ['Splunk', 'Product Manager', '134633'],
      ['Dimensional Insight', 'Consultant', '69359'],
      ['Splunk', 'Customer Success Manager', '125720'],
      ['Edgeworth Economics', 'Consultant', '80190'],
      ['Edgeworth Economics', 'Economic Consultant', '80645'],
      ['Edgeworth Economics', 'Computer Systems Engineer', '98495'],
      ["Domino's", 'Analyst', '77937'],
      ['Fisher Investments', 'Research Associate', '79141'],
      ['Splunk', 'Data Analyst', '117652']
   ]
```

:bulb: How is `sal_lists` structurally different from `sal_strings`?

### 4.0 Problem 04 (15 points)

In this problem, you will implement a `while` loop (a.k.a. an indefinite loop).

:exclamation: Beware of getting stuck in an infinite loop (mistakes do happen). If you need to exit the infinite loop, type `CTRL + C` or `command + C` in the terminal.

1. Initialize an empty list called `dom_sals`. Using a `while` loop and a conditional statement with an `in` operator, populate `dom_sals` with the **Domino's salaries** from `sal_lists`. Employ the accumulator pattern to help loop through sal_lists. The output should resemble the following:

   ```python
   [
      ["Domino's", 'Graphic Designer', '39000'],
      ["Domino's", 'Senior Technical Writer', '98000'],
      ["Domino's", 'Digital Specialist', '93000'],
      ["Domino's", 'Analyst', '77937']
   ]
   ```

   :bulb: Indexing may be required to access the company name within each list. When performing a case-insensitive comparison of two strings, convert the strings to lower case before performing the comparison.

2. Initialize an empty list called `dom_idx`. In the same `while` loop as in Problem 4.1 populate a list called `dom_idx` with the **indices** of the Domino's-related elements in `sal_lists`. The output should resemble the following:

   `[0, 4, 6, 13]`

   :bulb: It may be helpful to use the accumulator pattern from Problem 4.1 to track the indices.

## 5.0 Problem 05 (15 points)

In this problem, you will be using a `for` loop and `if-elif` statements to create new lists with specific roles.

1. Initialize an empty list called `consultant_sals`. Using a `for` loop and a conditional statement with an `in` operator, populate `consultant_sals` with all **Consultant roles** from `sal_lists`. This is a greedy accumulator, meaning that it will take any list as long as it has the word **consultant**. **Economic Consultant** could be included, for example.  The output should resemble the following:

   ```python
   [
      ['Dimensional Insight', 'Consultant', '69359'],
      ['Edgeworth Economics', 'Consultant', '80190'],
      ['Edgeworth Economics', 'Economic Consultant', '80645']
   ]
   ```

   :bulb: Indexing may be required to access the job role within each list. When performing a case-insensitive comparison of two strings, convert the strings to lower case before performing the comparison.

2. Initialize an empty list called `analyst_sals`. Using the same `for` loop from Problem 5.1 and an `elif` statement employing a comparison equal operator, populate `analyst_sals` with **Analyst roles** from `sal_lists`. This is a non-greedy accumulator. This means that it will not take any lists that have words other than **Analyst** in the title. **Data Analyst** would **NOT** be included, for example. The output should resemble the following:

   ```python
   [
      ['Fisher Investments', 'Analyst', '95916'],
      ['Department of Health & Human Services', 'Analyst', '71754'],
      ["Domino's", 'Analyst', '77937']
   ]
   ```

   :bulb:  Think about why you would use an `elif` instead of an additional `if` statement for Problem 5.2.

### 6.0 Problem 06 (15 points)

In this problem, you will use a `for` loop to extract individual nested elements as opposed to whole lists.

1. Initialize an integer called `max_analyst_sal`. Using a `for` loop and a conditional statement with an inequality, find the highest salary in `analyst_sals`. Assign this integer to `max_analyst_sal` in the loop.

   :bulb: Indexing may be required to access the salary within each list. Use the appropriate function to convert the salary to an integer. Assign the salary to a variable before comparing it to max_analyst_sal in the conditional statement.

2. Initialize an empty string called `max_analyst_company`. Using the same `for` loop and conditional statement from Problem 6.1, find the company that provides the highest average salary for Analysts. Assign the name of this company to `max_analyst_company`.

   :bulb: Indexing may be required to access the company name within each list.

### 7.0 Problem 07 (21 points)

In this problem, you will be using a `for` loop that doesn't loop through all elements in the list. You will also be using an `if-else` statement to organize some lists into categories.

1. Using the `range` function, create a `for` loop that only loops through the first 10 items in `sal_lists`.

   :bulb: Indexing may be required to access the salary within each list. Use the appropriate function to convert the salary to an integer. Assign the salary to a variable before using it in the conditional statement.

2. Initialize a list called `sal_great`. Using a `for` loop and a conditional statement with an inequality, find all salaries that are greater than 50000. Assign these lists to `sal_great` in the loop. The desired output of `sal_great` is

   ```python
   [
      ['Fisher Investments', 'Analyst', '95916'],
      ['Department of Health & Human Services', 'Technical Writing Specialist', '76703'],
      ['Splunk', 'Front-End Engineer', '139554'],
      ["Domino's", 'Senior Technical Writer', '98000'],
      ['Department of Health & Human Services', 'Analyst', '71754'],
      ["Domino's", 'Digital Specialist', '93000'],0
      ['Splunk', 'Product Manager', '134633'],
      ['Dimensional Insight', 'Consultant', '69359'],
      ['Splunk', 'Customer Success Manager', '125720']
   ]
   ```

3. Initialize an empty list called `sal_too_low`. Using a `for` loop and an `else` statement, assign the remaining list to `sal_too_low` in the loop. The desired output of `sal_too_low` is

   ```python
   [
      ["Domino's", 'Graphic Designer', '39000']
   ]
   ```
