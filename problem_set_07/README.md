# SI 506: Problem Set 07

## This week's Problem Set

This week's problem set will focus on dictionaries, which are a data structure that involves using `keys` to look up the `values` associated with them. A Python dictionary is quite similar to a traditional dictionary in way information is accessed. In a traditional dictionary, the `key` would be the word you are looking up and the `value` would be the definition of the word.

The general structure of a Python dictionary is:

```python
<dict_name> = {
    <key>: <value>,
    <key>: <value>,
    <key>: <value>
}
```

## Background

:racing_car: &nbsp; :dash::dash::dash:

<!-- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:racing_car: :dash:\
&nbsp;&nbsp;&nbsp;:racing_car: :dash: -->


This week's problem set centers around auto racing, specifically an international competition known as Formula One, or F1 for short. The Formula One competition has been around since 1950 and a season involves teams competing in a series of races known as *Grands Prix*. F1 cars are the fastest regulated racing cars in the world, with top speeds reaching around 215 mph (350 km/h)!

Last Sunday (10/24), the United States held it's annual *Grand Prix* in Austin, TX at the Circuit of the Americas. 10 teams, with two drivers each, competed to win the coveted US Grand Prix and collect points towards the Driver's and Constructor's championships.

## Problem 01 (10 points)
1. Inside of `main()`, use the `read_csv_to_dicts` function to read in the two .csv files provided:

    1. Retieve data from `driver_standings_pre_USGP.csv` and store it in a variable named `standings`.

    2. Retieve data from `usgp_results.csv` and store it in a variable named `race_result`.

`standings` should look like:

```python
    [{'driver': 'Max Verstappen', 'team': 'Red Bull', 'nationality': 'Dutch', 'points': '262.5'},
    {'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'nationality': 'British', 'points': '256.5'},
    {'driver': 'Valtteri Bottas', 'team': 'Mercedes', 'nationality': 'Finnish', 'points': '177'}, ...]
```

`race_result` should look like:
```python
    [{'name': 'Antonio Giovinazzi', 'team': 'Alfa Romeo', 'position': '11', 'fastest_lap': '1:41:145', 'points': '0'},
    {'name': 'Carlos Sainz', 'team': 'Ferrari', 'position': '7', 'fastest_lap': '1:40:377', 'points': '6'},
    {'name': 'Charles Leclerc', 'team': 'Ferrari', 'position': '4', 'fastest_lap': '1:39:303', 'points': '12'}, ...]
```

2. Inside of `main()`, use in-built Python dictionary methods to perform the following:

    1. Retrieve the last element of `standings` and assign its **keys** to `last_standing_keys`.

    2. Retrieve the third element of `standings` and assign its **values** to `third_standing_values`.

    3. Retrieve the tenth element of `race_result` and assign its **keys and values** to `tenth_race_result_kv`.

        :bulb: Which dictionary method returns **both** keys and values of a dictionary?

## Problem 02 (20 points)
Currently, numerical data in both lists is stored as strings. Let's implement a function that converts them to `int` or `float` based on the value type.

1. Define a function called `clean_data()` that defines one parameter:

    `data` (list): A list of dictionaries.

    This function should:
    1. Use a nested loop to iterate over `data` and convert values associated with `points` to `float` and values associated with `position` to `int`.
    
    2. Update values in-place (i.e. update existing string value with numerical value).
    
    2. have the ability to handle both `standings` **and** `race_result` data.

    <!-- :bulb: Consider using a Python dictionary method that would return a sequence that contains `points`/`position` for the standings/race result data. -->

2. Inside `main()`, use `clean_data()` to create two new variables called `cleaned_standings` and `cleaned_race_result`, that contain the "cleaned" versions of `standings` and `race_result`, respectively.

## Problem 03 (10 points)
1. Define a function called `convert_time_to_ms` that defines one parameter:

    `driver_dict` (`list`): A dictionary representation of a driver's race result.

    This function should access the fastest lap time for a driver and convert it from `mm:ss:msms` format to a single millisecond (ms) value.

    1. Retrieve the value for the fastest lap time using the correct key.
    2. Convert the minute and second values to milliseconds and sum up the total.

    The related time conversions are:

    ```
    1 minute = 60000 milliseconds
    1 second = 1000 milliseconds
    ```

    :bulb: Notice how the lap time are formatted. What string method can you use to separate them?

You can test your function on the *first* element of `cleaned_race_result` in `main()`. The value returned value should be **101145** ms. Note that this is an optional step and not required to get full credit for this problem.

## Problem 04 (20 points)

In a Forumla 1 race (aka *Grand Prix*), the driver who drives a lap of the circuit in the least amount of time (aka the fastest lap) is awarded a bonus Championship Point if they finish within the top 10 positions.

1. Define a function called `add_fastest_lap_point` that defines one parameter:

    `race_result` (`list`): A list of dictionaries that contains the results from a race.

    This function should:

    1. Use an `accumulator pattern` to loop through the race results and find the driver with the fastest single lap time.
    
    2. Delegate the task of getting each driver's lap time by calling the `convert_time_to_ms` function and assigning the return value to a variable named `lap_time`.
    
    3. Use a conditional statement to assign/update the fastest lap/driver. The statement should check whether the driver finished with a position in the top 10 **and** check if their `lap_time` was smaller than the current fastest lap time. This should be done within **one** conditional statement.

    4. Iterate through `race_result` and award an extra point to the driver with the fastest lap (if any).

2. Inside `main()`, use `add_fastest_lap_point()` to update the race result to reflect the change made by awarding the bonus point The updated race result should be assigned to a variable named `updated_race_result`.

## Problem 05 (20 points)
1. Define a function called `update_driver_standings()` that defines two parameters:

    `standings` (`list`): A list of dictionaries that contains the current driver's championship standings.

    `race_result` (`list`): A list that contains the results from a race.

    This function should use a nested loop to add points earned by drivers from a race to the overall driver's standings.

2. Inside `main()` declare a variable called `updated_standings`. Call the `updated_driver_standings` function and pass to it the appropriate argument and assign its return value to `updated_standings`.

## Problem 06 (15 points)
Formula 1 has had many great World Championship winning teams and drivers from across the world. Countries like the United Kingdom, Italy, Germany and Brazil are just a few of a long list of countries who have produced World Champions. In this problem we aim see which countries would win a head-to-head challenge!

1. Define a function called `compare_points_by_nation()` that defines three parameters:

    `standings` (`list`): A list of dictionaries that contains the drivers' standings.
    
    `nationality1` (`str`): A string signifying the first nationality to be checked for.

    `nationality2` (`str`): A string signifying the second nationality to be checked for.

    This function should:
    
    1. Use a `for` loop with conditional statements to find the average points for each of the two nationalities that are passed in as arguments. Each country's average points score should be contained in its own variable, i.e. `nation1_avg` for `nationality1` and `nation2_avg` for `nationality2`.

    2. Use conditional statements to determine the nationality with the greater point average. The winning nationality and its respective point average (rounded to one decimal place) should be returned as a tuple in the form:

    ```python
    (< nationality >, < nationx_avg >)
    ```

2. Inside `main()`, call `compare_points_by_nation()` to find whether German drivers are performing better than British drivers. Assign the return value of this function call to a variable called `ger_vs_gbr`.

3. Inside `main()`, call `compare_points_by_nation()` to find whether French drivers are performing better than Spanish drivers. Assign the return value of this function call to a variable called `fra_vs_spa`.

## Problem 07 (5 points)
1. Inside `main()`, call `write_dicts_to_csv()` by doing the following:
    1. Assigning to a variable named `write_filepath`, the filepath for a file named `driver_standings_post_USGP.csv`.

    2. Assigning to a variable named `write_fieldnames`, a `list` of `strings` that matches the header row in `driver_standings_pre_USGP.csv`.

    :bulb: You may choose to hard-code this list or use a dictionary method to extract the same information from a dictionary in your final standings data.

    3. Call `write_dicts_to_csv()` using *keyword arguments* in **default** order. Use the variable created in Problem 5.2 as the argument for data.
