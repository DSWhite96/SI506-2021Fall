# SI 506: Problem Set 09

## This week's problem set

This week's problem set introduces classes and continues work with the json and requests modules as
well as the Star Wars API (SWAPI).

## Background

C-3PO is a protocol droid built to communicate in foreign environments. He knows the ettiquete,
customs, and languages of millions of planets! Sadly, C-3PO doesn't have very good defensive
capabilities and is freqeuntly incapacitated. On this mission, C-3PO's database of languages and
cultural information was destroyed. It's our job to rebuild him and make him operational again.

## Problem 1.0 (45 points)

First, we are going to create a `Droid` class that we will use to build a C-3PO object. This class
will have several attributes and methods. Let's implement them one at a time.

### Problem 1.1 (10 points)

Implement the `__init__` method (the constructor) according to the docstring.

### Problem 1.2 (10 points)

Implement the `__str__` method according to the docstring. This method sets what displays in the
terminal when the object is printed. It is recommended that you copy the sample f-strings and make
alterations in the appropriate places to avoid typos and unnecessary trouble with Gradescope.

### Problem 1.3 (15 points)

Implement the `load_languages` method according to the docstring. This method will be used to add a
language database to the C-3PO object later.

### Problem 1.4 (10 points)

Implement the `jsonable` method according to the docstring. This function will be used to make an
instance of the `Droid` class json-friendly.

:bulb: If `languages` != None, be sure to call the `jsonable` method on the `languages` instance
variable in order to convert it to a dictionary. This will make more sense once you get to Problem
2.5.

## Problem 2.0 (60 points)

Next, we are going to create a `Languages` class. This class will hold a language database, which
we will later load into C-3PO

### Problem 2.1 (10 points)

Implement the `__init__` method (the constructor) according to the docstring.

### Problem 2.2 (10 points)

Implement the `__str__` method according to the docstring. This method sets what displays in the
terminal when the object is printed. It is recommended that you copy the sample f-string and make
alterations in the appropriate places to avoid typos and unnecessary trouble with Gradescope.

### Problem 2.3 (10 points)

Implement the `add_language` method according to the docstring.

### Problem 2.4 (10 points)

Implement the `update_language_count` method according to the docstring.

### Problem 2.5 (10 points)

Implement the `get_speakers` method according to the docstring.

### Problem 2.6 (10 points)

Implement the `jsonable` method according to the docstring. This function will be used to make an
instance of the `Languages` class json-friendly.

## Problem 3.0 (15 points)

Next, we will implement a function to read json files and use it to load some data.

### Problem 3.1 (10 points)

Implement the `read_json` function according to the docstring.

### Problem 3.2 (5 points)

In `main`, use this function to read the 'swapi_species.json' into a variable called `species_data`.

## Problem 4.0 (10 points)

Implement the `get_swapi_resource` function according to the docstring. We will use this function
to collect homeworld information and to gather information on C-3PO so we can rebuild him.

## Problem 5.0 (25 points)

Next, we will implement a function to fill the `language_database` instance variable of the `Languages` class.

### Problem 5.1 (15 points)

Implement the `fill_language_database` function according to the docstring.

### Problem 5.2 (10 points)

Call this function in `main`, passing `species_data` and an instance of the `Languages` class.
Store the return value in a variable called `language_database`. Now that `language_database` is
full of language information, call the `update_language_count` method to update the number of
languages in the database. Finally, let's test the database code by using the `get_speakers` method
to find information on the species and planets that speak 'Galactic Basic'. Store the return value
of this method in a variable called `galactic_basic_speakers`.

## Problem 6.0 (25 points)

In this problem, we will finally rebuild C-3PO!

### Problem 6.1 (5 points)

In `main`, call `get_swapi_resource` using the `PEOPLE_URL` constant variable to conduct a search
for 'C-3PO'. Extract the dictionary containing information about C-3PO from the resulting data
object and store it in a variable called `c3po_data`. In order to pass Gradescope, you might
consider calling `get_swapi_resource` and extracting the C-3PO information dictionary on one line.

### Problem 6.2 (15 points)

Next, implement the `create_droid` function according to the docstring.

### Problem 6.3 (10 points)

Next, in `main`, use this function to create an instance of the `Droid` class called `c3po`. Use
`Droid`'s `load_languages` method to load the `language_database` object we created in Problem 4.2
into `c3po`.

## Problem 7.0 (15 points)

Finally, we are going to create a backup of C-3PO in case he becomes not operational again!

### Problem 7.1 (5 points)

Implement the `write_json` function according to the docstring.

### Problem 7.2 (10 points)

In `main`, use the `write_json` function to write `c3po` to a json file called 'c3po.json'. For
this problem, you should use *positional arguments*. You are required to put the filename,
'c3po.json', directly in the function. Do not store 'c3po.json' in a variable.
