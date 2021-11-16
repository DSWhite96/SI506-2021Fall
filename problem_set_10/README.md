# SI 506: Problem Set 10

## This week's problem set

This week's problem set introduces modules and continues to work with Python class, json, etc.
In this week, we particularly focus on the process of data cleaning and manipulation.
You will work on two Python files: `problem_set_10.py` and `swapi_entities.py`, where the `problem_set_10.py` file is the main workspace that imports classes and functions from `swapi_entities.py`.
The `swapi_planets.json` is the source data for this problem set.

:exclamation: **You _must_ submit both `problem_set_10.py` and `swapi_entities.py` to Gradescope in order to earn points (do not change the filenames).**

## Problem 1.0

Reading and writing json files.

### Problem 1.1 (5 points)

- Implement the function `read_json()` in the file `problem_set_10.py`.

- Read the JSON file `swapi_planets.json` in `main()` in the file `problem_set_10.py`, and assign the return value to `planet_data`

### Problem 1.2 (5 points)

- Implement the function `write_json()` in the file `problem_set_10.py`.

## Problem 2.0 (50 points)

Now turn to the file `swapi_entities.py`, implement a `Planet` class with the following methods:

- `__init__()`. Replace `pass` and add the required and optional instance
  variable assignments. Assign `None` to the optional instance variables. (10 points)
- `__str__()`. Replace `pass` and return the `Planet` instance's name value. (5 points)
- `has_surface_water()`. Replace `pass` and return a boolean value if the `Planet` instance's surface_water is greater than 0. (10 points)
- `is_populated()`. Replace `pass` and return a boolean value if the `Planet` instance's population is greater than 0. (10 points)
- `jsonable()`. Replace `pass` and return a JSON-friendly dictionary comprising all the instance
  variables and their values expressed as key-value pairs
  __in the order specified in the Docstring__. This is best accomplished by returning a dictionary
  literal. (15 points)

## Problem 3.0 (30 points)

In the file `swapi_entities.py`, write a `convert_data()` function that converts planet dictionary's string values to int, float, list, etc. 

:bulb: When the value is "unknown", you must set it to `None` instead of converting it.

:bulb: For the value of `gravity`, you must provide a default unit as "standard" if there is no unit provided. (Some planets have only `"gravity": "1.1"` instead of `"gravity": "1.1 standard"`)

:bulb: See the Docstring for more details. Here is an example of expected input and output:

```json
// input
{
    "name": "Hoth",
    "rotation_period": "23",
    "orbital_period": "549",
    "diameter": "7200",
    "climate": "frozen",
    "gravity": "1.1 standard",
    "terrain": "tundra, ice caves, mountain ranges",
    "surface_water": "100",
    "population": "unknown",
    "residents": [],
    "films": [
    "https://swapi.py4e.com/api/films/2/"
    ],
    "created": "2014-12-10T11:39:13.934000Z",
    "edited": "2014-12-20T20:58:18.423000Z",
    "url": "https://swapi.py4e.com/api/planets/4/"
}

// output
{
    "name": "Hoth",
    "rotation_period": 23,
    "orbital_period": 549,
    "diameter": 7200,
    "climate": ["frozen"],
    "gravity": {"measure": 1.1, "unit": "standard"},
    "terrain": ["tundra", "ice caves", "mountain ranges"],
    "surface_water": 100,
    "population": None,
    "residents": [],
    "films": [
    "https://swapi.py4e.com/api/films/2/"
    ],
    "created": "2014-12-10T11:39:13.934000Z",
    "edited": "2014-12-20T20:58:18.423000Z",
    "url": "https://swapi.py4e.com/api/planets/4/"
}
```

## Problem 4.0 (20 points)
Write a `create_planet` function. This function should return an instance of a `Planet`.
During the implementation, you must call `convert_data` to convert the planet dictionary values before assigning them to the appropriate instance variables. See the Docstring for more details. 

## Problem 5.0

### Problem 5.1 (10 points)

Now that we have implemented a Python class and two functions in the file `swapi_entities.py`, we can import this file in `problem_set_10.py`.

- Import the file `swapi_entities.py` as `ent` in the beginning of the file `problem_set_10.py`.

### Problem 5.2 (20 points)
In `main()`, loop over the `planet_data` list, call `create_planet` from `ent` for each planet dictionary, and create a "cleaned" `Planet` instance. 
Then insert a new key-value pair into an accumulator dictionary called `planets`. 
The variable `planets` should be in the following format:
```json
{
    < planet.name >: < Planet instance >
    ... 
}
```

## Problem 6.0

Now that we have cleaned the data, we need to categorize the data and write to JSON files. Now you should loop over the values of the dictionary `planets` and do the following:

### Problem 6.1 (10 points)
If the planet has surface water (call the `has_surface_water()` method), then insert a JSON format of the planet instance to the variable `planets_with_surface_water`.

Write the list `planets_with_surface_water` into a file named `stu_planets_with_surface_water.json`.

:bulb: You must exclude those planets whose `surface_water` is `None`.

### Problem 6.2 (10 points)
If the planet is inhabited (call the `is_populated()` method), then insert a JSON format of the planet instance to the variable `planets_inhabited`; otherwise insert it to the variable `planets_uninhabited`.

- Write the list `planets_inhabited` into a file named `stu_planets_inhabited.json`.

- Write the list `planets_uninhabited` into a file named `stu_planets_uninhabited.json`.

:bulb: You must exclude those planets whose `population` is `None`.

### Problem 6.3 (10 points)
If the planet's terrain is only `desert`, then insert a JSON format of the planet instance to the variable `planets_desert_only`.

- Write the list `planets_desert_only` into a file named `stu_planets_desert_only.json`.

:bulb: You must exclude those planets whose `terrain` is `None`.

:bulb: You must make sure that `terrain` (which is a list) has only one element and that element is `desert`.

### Problem 6.4 (30 points)
Use the accumulation pattern to get a list of the biggest planets (the largest in `diameter`) and the smallest planets (the smallest in `diameter`).
Fill these two lists in the dictionary `planets_biggest_smallest`.

- Write the list `planets_biggest_smallest` into a file named `stu_planets_biggest_smallest.json`.

:bulb: You must exclude those planets whose `diameter` is `None`. 

:bulb: You must include all planets that have the same biggest/smallest diameter in the list. 
