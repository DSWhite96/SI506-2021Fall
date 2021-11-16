# SI 506: Lab Exercise 10

## This Week's Lab

This week we will focus on importing modules, instantiating classes, and implementing functions.
The following lab exercise will allow you to work more with SWAPI to get you comfortable using
modules and cleaning data. 

:exclamation: You _must_ submit both `lecture_10.py` and `swapi_utils.py` to Gradescope in order
to earn points (do not change the filenames).

## Background

> A starship, often referred to as simply a ship, is a manned vehicle used for traveling in
> realspace or hyperspace. Dating back thousands of years, the earliest starships transported
> spacers to new worlds through cryogenic freezing processes. Upon the invention of the hyperdrive,
> those that were equipped could travel faster than light by entering
> hyperspace, drastically reducing the journey times between two solar systems

Source: [Wookieepedia](https://starwars.fandom.com/wiki/Starship)

## PROBLEM 01 (9 Points)

In the `swapi_utils.py`, you need to,

1. Import `json` and `request` modules.

2. Create a constant variable `ENDPOINT` and assign the SWAPI endpoint URL used in recent lectures.

3. Implement `get_swapi_resource()` in order to request resources from the SWAPI endpoint and
   decode the response into a dictionary. Review the Docstring for more information about the
   function's behavior.

4. Implement `write_json()`. This function defines two required parameters, `filepath` and `data`,
   and three optional parameters, `encoding`, `ensure_ascii`, and `indent`. Review the Docstring
   for more information about the function's behavior.

In the `lab_exercise_10.py`, you need to,

1. Import `swapi_utils` as `utl`.

2. In the main function, call the function `get_swapi_resource()` in `utl` and retrieve a list of dictionary representations for the first ten starships. See the
   SWAPI [documenutation](https://swapi.py4e.com/api/) or check previous lectures if you need help
   constructing the arguments to pass to get_swapi_resource().

3. Assign the return value to a local variable named `starships_data`.

## PROBLEM 02 (9 Points)
Implement the `create_starship()` function.

1. Replace `pass` with a code block that instantiates an instance of `Starship` using the passed in
   `data` dictionary for values.

2. The `Starship` class has been provided. Initialize the `Starship` instance employing bracket
   notation when passing the required `data` dictionary values to the `__init__()` method. This will
   ensure that a runtime error is triggered if you accidently misspell a key or reference a key that
   does not exist in `data`. We recommend assigning each instance to a local variable named
   `starship`.

   ```python
   starship = Starship(data[< key >], ...)
   ```

3. After the `Starship` instance is created, assign values to the optional instance variables. Before
   attempting to assign a value to an optional instance variable check the _truth value_ of the
   appropriate `data` key-value pair. If the truth value resolves to `True` assign the value; if
   `False` make no assignment.

   :bulb: You can check the truth value of a key-value pair by writing an `if` statement that tests
   the return value of `dict.get(< key >)`. If the key does not exist in the dictionary or the value
   returned is "falsy" (e.g., `None`, `False`, etc.) then `dict.get()` will return `None` and
   the `if statement` will evaluate to `False`.

   If `data.get(< key >)` evaluates to `True` assign the value to the instance variable. In some
   cases (although not for `Species`) you will need to convert the `str` value to a more appropriate
   value, e.g., `int`, `dict`, `float` as specified in the Docstring under the sub-heading
   "Type Conversions".

   ```python
   if data.get(< key >): # truth value (returns True/False)
       # if True assign value to the appropriate instance variable,
       # converting the value's type if required
   ```

   | Attribute | Type | Convert to | Special Cases Requirements |
   | :-------- | :--- | :--------- | :----------- |
   | max_atmosphering_speed | `str` | `int` | If the value is equal to 'n/a', change it to `None`. If the value ends with 'km', remove 'km' from the end and convert the return value to type `int`.|
   | consumables | `str` | `dict` | If the value ends with 's', remove 's' from the end. Split the string. For the first key-value pair in the dict, key is `'interval'` and value is second element of the split string. For the second key-value pair, key is `'value'`. The value is the first element of the split string, but you need to change it to `int` type.|
   | hyperdrive_rating | `str` | `float` |

   <br />

4. Return the instance to the caller.

## PROBLEM 03 (5 Points)

1. In `main()` assign an empty `list` to a local variable named `starships`.

2. Loop over `starships_data`. For every starship dictionary in `starships_data`, create a
   `Starship` instance using data sourced from the key-value pairs and then assign the instance
   to the `starships` list.

## PROBLEM 04 (2 Points)

Next, create a list called `writable`. Loop over `starships` and append a JSON-friendly
representation of each starship instance to the `writable` list. Then call the function
`write_json()` from `utl` and pass to it the following arguments:

* `filepath` = 'starships.json'
* `data` = `writable`

:bulb: After generating your file right click on `starships.json` and select the "Select for
Compare" option and then right click on `fxt_starships.json` and select "Compare with Selected".
Lines highlighted in red indicate character mismatches. If any mismatches are encountered revise
your code.
