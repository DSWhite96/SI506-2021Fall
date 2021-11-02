# SI 506: Lab Exercise 08

## This Week's Lab

The following lab exercise will introduce you to the [Star Wars API](https://swapi.py4e.com/api/)
(SWAPI) and the [requests](https://docs.python-requests.org/en/latest/) module. You will retrieve
from SWAPI a representation of the Star Wars character Owen Lars.

## Background

> Owen Lars is a human male moisture farmer from the desert planet Tatooine. He is the
> son of Aika and Cliegg Lars, and he became the stepbrother of Jedi Knight Anakin Skywalker when
> Cliegg married Anakin's mother, Shmi Skywalker. In 22 BBY, Shmi was killed by Tusken Raiders, and
> Cliegg passed away soon after. Lars married his girlfriend, Beru Whitesun, and they toiled to
> maintain the homestead.

Source: [Wookieepedia](https://starwars.fandom.com/wiki/Owen_Lars)

## PROBLEM 01 (5 Points)

Implement `get_swapi_resource()` in order to request resources from the SWAPI endpoint and decode
the response into a dictionary. Review the Docstring for more information about the function's
behavior.

After implmenting the function, return to `main()` and call the function passing to it as arguments
the SWAPI endpoint URL for retrieving people and the dictionary `{'search': owen lars}` as the
`params` value.

The return value is a dictionary. Access the SWAPI representation of Owen Lars in the dictionary's
`results` list and assign the element to the variable named `lars_data`.

## PROBLEM 02 (2 Points)

In this problem you will create a dictionary called `lars`. Provision it with four key-value pairs
with the value of each set to `None`.

Keys and values:
* `name` (str): None.
* `hair_color` (str): None.
* `eye_color` (str): None.
* `species_name` (str): None.

## PROBLEM 03 (5 Points)

In this problem you will implement `write_json()`. This function defines two required parameters,
`filepath` and `data`, and three optional parameters, `encoding`, `ensure_ascii`, and `indent`.
Review the Docstring for more information about the function's behavior.

## PROBLEM 04 (8 Points)

Implement the `main()` function.

1. Call `get_swapi_resource()` and pass it the arguments specified in Problem 01 above in order to
   retrieve a representation of Owen Lars. Save the results to `lars_data`.

2. A URL is assigned to the `species` key in `lars_data`. Retrieve a representation of Owen Lars's
   species by retreiving it from SWAPI using the `species` URL. Assign the _name_ of Owen
   Lars's species to the variable named `lars_species` and then update `lars_data` by assigning the
   species name to the appropriate key.

3. Use a `for` loop to iterate over the keys in `lars_data`. For every key that matches the keys in
   the `lars` dictionary, update the value with the value contained in `lars_data`.

4. Call `write_json`, encode the `lars` dictionary as JSON, and write the object to a new file
   named `owen_lars.json`.
