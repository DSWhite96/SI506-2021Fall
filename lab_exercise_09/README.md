# SI 506: Lab Exercise 09

## This Week's Lab

This week we will focus on creating and instantiating classes, and implementing functions. The
following lab exercise will allow you to work more with SWAPI to get you comfortable using the
`requests` module.

## Background

> [Tatooine](https://starwars.fandom.com/wiki/Tatooine) is a sparsely inhabited circumbinary desert
> planet located in the galaxy's Outer Rim Territories. It was the homeworld of Anakin and Luke
> Skywalker, who would go on to shape galactic history.
> [Luke Skywalker](https://starwars.fandom.com/wiki/Luke_Skywalker), a Force-sensitive human male,
> was a legendary Jedi Master who fought in the Galactic Civil War during the reign of the Galactic
> Empire.

## Setup Code

```python
ENDPOINT = 'https://swapi.py4e.com/api'

def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more SWAPI entities to be found in ['results'] list; otherwise, response
    object body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()
```

## PROBLEM 01 (2 Points)

1. Implement a function called `read_json()` that reads a JSON document per the provided filepath
   and returns the decoded data to the caller.

2. Implement a function called `write_json()` that accepts a dictionary or a list of dictionaries,
   encodes the passed-in data as JSON, and writes the encoded data to the target file.

:bulb: We have discussed these two functions in class. Refer to the lecture 18 solution file for
example code.

## PROBLEM 02 (4 Points)

Implement the `Planet` class with the following methods:

1. `__init__()`. Replace `pass` and add the instance variables `name`, `diameter`, `climate`,
   `system`, `population`, `orbital_position`. See the docstring for more implementation details.

2. `__str__()`. Replace `pass` and return the `Planet` instance's name value.

3. `jsonable()`. Replace `pass` and return a JSON-friendly dictionary comprising all the instance
   variables and their values expressed as key-value pairs
   __in the order specified in the Docstring__. This is best accomplished by returning a dictionary
   literal.

  ```python
  return {
      '< instance variable name >': < instance variable value >,
      # add additional key-value pairs
      # . . .
      }
  ```

## PROBLEM 03 (4 Points)

Implement the `Person` class with the following methods:

1. `__init__()`. Add the instance variables `url`, `name`, `birth_year`, `height`, `mass`, as
   parameters. Assign `None` to the optional instance variable `homeworld`. See the docstring for
   more implementation details.

2. `__str__()`. Return the `Person` instance's name value.

3. `jsonable()`. Return a JSON-friendly dictionary comprising all the instance variables and their
   values expressed as key-value pairs __in the order specified in the Docstring__. This is best
   accomplished by returning a dictionary literal.

    :bulb: `Person` is a composite class that includes a `Planet` component. The `jsonable()`
    method _must_ convert both the `Person` instance to a dictionary and the `homeworld` value
    `Planet` instance to a dictionary (or `None` if the `self.homeworld` value is `None`).

## PROBLEM 04 (10 Points)

In this problem you will implement `main()`:

1. Call `get_swapi_resource()` and pass it the appropriate URL and querystring search value in
   order to retrieve the SWAPI representation of Luke Skywalker.

   bulb: the querystring you need to pass to retrieve Luke is a single key-value pair:

   `{'search: 'luke skywalker'}`

   Retrieve the dictionary representation of Luke from the "response" dictionary returned by
   `get_swapi_resource`. Assign the return value to the variable `swapi_luke`.

    :bulb: The following is an excerpt of what a typical SWAPI JSON response looks like when
    searching for people.

    ```json
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "name": "Luke Skywalker",
                "height": "172",
                "mass": "77",
                "hair_color": "blond",
                "skin_color": "fair",
                "eye_color": "blue",
                "birth_year": "19BBY",
                "gender": "male",
                ...
                "created": "2014-12-09T13:50:51.644000Z",
                "edited": "2014-12-20T21:17:56.891000Z",
                "url": "https://swapi.py4e.com/api/people/1/"
            }
        ]
    }
    ```

2. Create a `Person` instance with the dictionary `swapi_luke`. Assign the new class instance the
   name `luke`. When instantiating the the `Person` instance convert the following values when
   passing them to the `__init__` method:

   * height (float)
   * mass (float)

3. Call `read_json()` and pass the filepath `tatooine.json` as the argument. Assign the return
   value to the variable `tatooine_data`.

4. Call `get_swapi_resource()` again. This time retrieve information about a __planet__ called
   `Tatooine`. The querystring you need to pass to the function is a single key-value pair:
   `{'search: 'tatooine'}`. Use the "results" key and corresponding index to access the resource(s)
   matched by the search query return. Assign the return value to the variable `swapi_tatooine`.

    :bulb: similar to step 1, the value of the "results" key is a list and you need to access the
    first element in the list.

5. Update the `swapi_tatooine` dictionary with the `tatooine_data` sourced from `tatooine.json`.

6. Create a `Planet` instance with the updated dictionary `swapi_tatooine`. Assign the new class instance the name `tatooine`.
When instantiating the
   the `Planet` instance convert the following values when passing them to the `__init__`
   method:

   * diameter (float)
   * population (int)

7. Assign `tatooine` to `luke.homeworld`.

8. Call `luke.jsonable()` and assign the return value to `luke_profile`.

9. Call the function `write_json()` and pass to it the following arguments:

    * `filepath`: 'luke_profile.json'
    * `data`: `luke_profile`.

    <br />

    :exclamation: The resulting `luke_profile.json` _must_ match the following
    JSON document:

    ```json
    {
      "url": "https://swapi.py4e.com/api/people/1/",
      "name": "Luke Skywalker",
      "birthyear": "19BBY",
      "height": 172.0,
      "mass": 77.0,
      "homeworld": {
        "name": "Tatooine",
        "diameter": 10465.0,
        "climate": "hot and arid",
        "system": "Tatoo system",
        "population": 200000,
        "orbital_position": "first from the sun"
      }
    }
    ```
