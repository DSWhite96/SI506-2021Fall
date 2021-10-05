# SI 506: Problem Set 05

## This week's Problem Set

This week's problem set focuses on files, functions, nested loops, and tuples.

## Background

On September 26, 2021, Germany held a national election. Germany's most recent previous national election occured in 2017. The 2021 election was important for many reasons. Angela Merkel, who has been the chancellor of Germany since 2005, elected not to run, leaving big shoes to fill. This election also served as a referendum on extreme and populist parties in Germany, which did very well in Germany's 2017 election. Germany is the largest country in the European Union and has huge sway on the continent. This election will impact politics worldwide. How did things shake up this year? Let's load some data and find out!

### Problem 01 (15 points)

Write a function called `read_csv` that defines one parameter:

* `filepath` (`str`): represents the path and name of a csv file

### Requirements
This function should load a csv file and return its contents in a list of lists, where each list is one row from the csv file.

Use `read_csv` to load `election_data_2021.csv` and `election_data_2017.csv` into variables called `raw_election_data_2021` and `raw_election_data_2017`, respectively. For your reference, `raw_election_data_2021` should look like this:
```python
    raw_election_data_2021 = [
            ['Party', 'Seats', 'Affiliation'],
            ['AfD ', '94', 'far right'],
            ['SPD', '153', 'center Left'],
            ['  Left', '69', 'FAR left'],
            ['Greens', '67', 'left  '],
            ['CDU/CSU  ', '246', 'center right'],
            ['  FDP', '80', '  right']
    ]
```

### Problem 02 (15 points)

Define a function called `clean` with one parameter:

* `data` (list): A list of lists, each representing a party's election results

### Requirements

This function will be used to create a **deep copy** of the data that was loaded in Problem 1 and return a clean version of the raw data. This function should accomplish three things:
1. convert numbers to integers,
2. remove trailing whitespace from **all** strings, and
3. make the values under party affiliation lowercase.

:bulb: Data cleaning is a crucial step when working with any real-world data. It makes working with data easier and helps us avoid mistakes!

Use `clean` to clean `raw_election_data_2021` and `raw_election_data_2017`. Store the cleaned version of these datasets in variables called `clean_election_data_2021` and `clean_election_data_2017`, respectively. For your reference, `clean_election_data_2021` should look like this:
```python
    clean_election_data_2021 = [
            ['Party', 'Seats', 'Affiliation'],
            ['SPD', 206, 'center left'],
            ['CDU/CSU', 196, 'center right'],
            ['FDP', 92, 'right'],
            ['Left', 39, 'far left'],
            ['Greens', 118, 'left'],
            ['AfD', 83, 'far right']
    ]
```

:bulb: Be sure to use the cleaned data and not the raw data for future problems!

### Problem 03 (15 points)

Write a function called `get_seat_differences` that defines two parameters:

* `current_election` (`list`): List of lists that represents election data
* `previous_election` (`list`): List of lists that represents election data

### Requirements

Using **nested loops**, calculate the difference between the number of seats that a party won in the current election and the number of seats that a party won in the previous election. Store that difference in a list of tuples, where each tuple has the party name at index 0 and the difference in seats between the two elections at index 1 (example: `("Party Name", -15)`)

Use `get_seat_differences` to get the seat differences between the 2021 and 2017 elections for every party. Store the resulting list of tuples in a variable called `party_seat_differences`.

### Problem 04 (20 points)

Write a function called `get_leaders` that defines two parameters:

* `election_data` (`list`): List of lists representing election data
* `party_leaders` (`list`): List of tuples, where each tuple contains (`party_name`, `party_leader(s)`)

### Requirements

Create a **deep copy** of `election_data`. Create a new column in the copy of `election_data` called `Party Leader(s)` and fill each party row with the appropriate party leader(s). Remember to return the edited deep copy of `election_data`. When looping over `party_leaders`, you must name your loop variable `party_tuple`. For this problem, you are required to employ **nested loops** and to **unpack the tuple** in order to access the values therein.

Use this function to add the data in `party_leaders_2021` to `clean_election_data_2021`. Store the resulting list of lists in a variable called `election_data_2021_with_leaders`.

:bulb: In Germany, chancellors are not elected directly. Rather, a chancellor has to both form a majority coalition with other parties *and* be the leader of the party with the most votes. If the leader of the party with the most votes cannot form a coalition, the leader of the party with the next highest vote total gets to try to form a majority coaltion.

### Problem 05 (20 points)

Write a function called `get_seats_percent` that defines one parameter:

* `election_data` (`list`): List of lists representing election data

### Requirements

This function takes a list of lists and then calculates the percentage of seats that different affiliations won. The percentages should be as follows:
* percent of seats that parties on the left won (contain "left" in affiliation)
* percent of seats that parties on the right won (contain "right" in affiliation)
* percent of seats that parties in the center won (does not contain "far" in affiliation)
* percent of seats that extreme parties won (contain "far" in affiliation)

Calculate the percentage of seats won using this formula:
* (seats / total_seats) * 100

Then, using the `round` function, round the resulting four percentage values to two decimal points.

:bulb: Hint: You may consider accumulating the number of seats for each affiliation category in one loop and performing the percent calculations outside of the loop.

Return the resulting percentage values in a tuple with the percentage values stored in this order: left, right, extreme, center.

Using `get_seats_percent`, calculate the percentage of seats that center and extreme parties and right and left parties won in 2021. Store the returned value in a variable called `affiliation_percents`.

:bulb: For this problem, you may used either `clean_election_data_2021` or `election_data_2021_with_leaders` to calculate the percentage values. Just be sure to index values according to the dataset you plan to use!


### Problem 06 (15 points)

Write a function called `write_csv` that defines two parameters:

* `filepath` (`string`): represents the path and name of a csv file
* `data` (`list`): List of lists representing election data

Write `data` to a csv file in `filepath`, where each list is a row in the csv file.

Finally, call `write_csv` to write `election_data_2021_with_leaders` to a new file called `revised_election_data_2021.csv`.