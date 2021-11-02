# SI 506: Problem Set 08

## This week's Problem Set

This week's problem set introduces the [Star Wars API (SWAPI)](https://swapi.py4e.com/about), the
json and requests module, and JSON objects. JSON objects can be represented as dictionaries, which
we will continue to explore in this problem set.

## Background

After escaping a massacre by Imperial forces, two droids, R2-D2 and C-3PO, land on the planet
Tatooine with a special message from Princess Leia to Obi-Wan Kenobi. On their way to find the Jedi
Master, the droids are bought by a moisture farmer and his nephew Luke Skywalker. While Luke helps
the pair find Obi-Wan, Imperial stormtroopers kill Luke's family in search of the droids. Without a
home, Luke decides to continue on to Alderaan with the rest of the crew, driven by Leia's plea.
After enlisting the help of smuggler Han Solo and his First Mate Chewbacca in a bid to escape
Tatooine, the crew is sold out by a mercenary. The stormtroopers pursue and attack them just as
they board the famed starship the Millennium Falcon. Help our friends board the ship safely and
make the jump to hyperspace!

## Problem 01 (10 points)

Let's figure out the order that the crew needs to board the ship.

1. Define a function called `read_json()` that defines two parameters:

    `filepath` (str): The location and filename of a JSON file.

    `encoding` (str): Optional encoding format. The default value is 'utf-8'.

    This function should:
    1. Use the `open` function to open the file.

    2. Use `json.load()` to parse the file into a `json` object.

    3. Return the `json` object.

    <!-- :bulb: Refer to the `docstring` for further details. -->

2. Inside `main()`, use the `read_json()` function to read in the `.json` file provided:

    1. Retrieve data from `./passengers.json`. This output should contain a dictionary with one key and a list of dictionaries as its value.

    2. Access the value for the `passengers` key from the output mentioned above. Assign this list of dictionaries to the variable `passengers`.

    `passengers` should look like this:

    ```python
    [
        {
            "name": "Han Solo",
            "category": "captain",
            "boarding_order": 6
        },
        {
            "name": "Chewbacca",
            "category": "co-pilot",
            "boarding_order": 1
        },
        ...
    ]
    ```

## Problem 02 (10 points)

Let's get information about our legendary starship.

1. Define a function called `get_swapi_resource()` that defines three parameters:

    1. Required

       * `url` (str): A url that provides information about entities in the Star Wars universe.

    2. Optional

       * `params` (dict): optional dictionary of querystring arguments (default value is `None`)

       * `timeout` (int): optional timeout value denoted in seconds (default value is `10`)

    This function _must_:

    1. Check whether the `params` dictionary has been specified.

    2. Use the `.get()` method from the `requests` library to access data with the `url` and
       `params` given, if any.

    3. Return the output as a `json` object.

    <!-- :bulb: Refer to the `Docstring` for further details. -->

2. Inside `main()`, use the `get_swapi_resource()` function to search for information about the
   Millenium Falcon:

    1. Create a variable called `base_url`. Assign the string `'https://swapi.py4e.com/api/'` to
       this variable. We will build on this root url to get data from SWAPI.

    2. Create a variable called `falcon_params`. Assign the dictionary `{'search': 'falcon'}` to
       this variable.

    3. Call the `get_swapi_resource()` function. Using the variables above, get information about
       the *Millennium Falcon*.

       <!-- :bulb: You will need to concatenate the `base_url` with the starships path before passing it to the `get_swapi_resource()` function. -->

    4. Create variable called `falcon`. Access the first element of the `results` key. Assign this
       dictionary to `falcon`.

       `falcon` should look like this:

       ```python
       {
           'name': 'Millennium Falcon',
           'model': 'YT-1300 light freighter','manufacturer': 'Corellian Engineering Corporation',
           'cost_in_credits': '100000',
           ...
       }
       ```

## Problem 03 (10 points)

The `falcon` variable contains some extraneous information. Let's create a function to remove it.

1. Define a function called `delete_items` that defines two parameters:

    `dictionary` (dict): A dictionary.

    `key_list` (list): A list of the keys to be deleted.

    This function _must_:

    1. Create a `deepcopy` of `dictionary` called `dict_copy`.

    2. Use a `for` loop and the built-in `del()` function to remove the specified keys from `dict_copy`.

    3. Use `in` operator to check whether each key is in the dictionary before deleting.

       <!-- :bulb: Using the `.get()` method in your conditional statement may not remove all the items for a specific key. -->

    4. Return `dict_copy`.

2. Inside `main()`, call the `delete_items()` function to remove the last five key-value pairs from `falcon`:

    1. Using the built-in `list` function, the `.keys()` method, and slicing in the same line,
       access the last five keys from the `falcon` dictionary. Assign this value to the
       `falcon_keys_delete` variable.

    2. Call the `delete_items()` function using the appropriate arguments to delete the last five
       items from the `falcon` dictionary. Assign this dictionary to the variable `falcon_updated`.

       `falcon_updated` should look like:

       ```python
       {
           'name': 'Millennium Falcon',
           'model': 'YT-1300 light freighter',
           'manufacturer': 'Corellian Engineering Corporation',
           'cost_in_credits': '100000',
           'length': '34.37',
           'max_atmosphering_speed': '1050',
           'crew': '4',
           'passengers': '6',
           'cargo_capacity': '100000',
           'consumables': '2 months',
           'hyperdrive_rating': '0.5',
           'MGLT': '75',
           'starship_class': 'Light freighter'
       }
       ```

## Problem 04 (20 Points)

It seems that some information about people are given in terms of URLs. Let's extract these details from SWAPI.

1. Define a function called `get_homeworld` that defines two parameters:

    `person` (dict): A dictionary.

    `key_list` (list): Optional list of keys to keep. Default value is `None`.

    This function should:
    1. Access the homeworld url from `person` and pass it to the `get_swapi_resource` function to get data about a person's homeworld.

    2. Check whether the `key_list` has been specified.

    3. Use a `for` loop with the accumulator pattern to create a dictionary with the specified items.

    4. Return the original homeworld dictionary or subset of the homeworld dictionary according to the value of `key_list`.

2. Implement a function called `get_species` that defines two parameters:

    `person` (dict): dicitionary representation of a person

    `key_list` (list): Optional list of keys to keep. Default value is `None`.

    This function _must_:

    1. Access the `value` for the species `key` in the person dictionary.

    2. Access the first species url if any has been specified.

    3. Check for the `key_list`.

    4. Use a `for` loop with the accumulator pattern to create a dictionary with the specified items.

    5. Return an empty or populated dictionary accordingly.

3. In the `main()` function, create the following variables:

    1. Call the `get_homeworld` function to get information about Bail Organa's homeworld. Assign
       this value to the variable `bail_home`.

       `bail_home` should look like:

       ```python
       {
           'name': 'Alderaan',
           'rotation_period': '24',
           'orbital_period': '364',
           'diameter': '12500',
           'climate': 'temperate',
           ...
       }
       ```

    2. Use the built-in `list` function, `.keys` method, and slicing to get the first 9 keys in
       `bail_home`.
       Assign this value to the variable `home_keys_keep`.

       `home_keys_keep` should look like:

       ```python
       [
           'name',
           'rotation_period',
           'orbital_period',
           'diameter',
           'climate',
           'gravity',
           'terrain',
           'surface_water',
           'population']
       ```

    3. Use the `get_species` function to retrieve information about Bail Organa's species. Assign
       the value to the variable `bail_species`.

       `bail_species` should look like:

       ```python
       [
           {
               'name': 'Human',
               'classification': 'mammal',
               'designation': 'sentient',
               'average_height': '180',
               ...
           }
       ]
       ```

## Problem 05 (20 Points)

Let's use the functions from the previous steps to bring our passengers to life.

1. Define a function called `clean_person_dictionary` that defines four parameters:

    `person` (dict): A dictionary representation of a person.

    `delete_list` (list): A list of keys to be deleted from person.

    `home_list` (list): Optional list of keys to keep in the homeworld dictionary. Default value is
                        None.
    `species_list` (list): Optional list of keys to keep in the species dictionary.
                            Default value is None.

    This function _must_ call the previously-made functions to:

    1. Delete the specified values.

    2. Get information about a person's homeworld and replace the `value` in the person dictionary
       with this information.

       <!-- :bulb: You should edit the output of the `delete_items` function, not the original person dictionary. -->

    3. Get information about a person's species and replace the `value` in the person's dictionary
       with this information.

       <!-- :bulb: You should edit the output of the `delete_items` function, not the original person dictionary. -->

    4. Return the person dictionary that has been edited by the `clean_person_dictionary` function.

       <!-- :bulb: You should not need a `for` loop to create this function. -->

2. Inside `main()`, update the `passengers` dictionary as follows:

    1. Using a `for` loop, access the name of each passenger.

    2. Call the `get_swapi_resource` function to get more information about each passenger.

    3. Use the `clean_person_dictionary` function to retain only the important information about a
       passenger.

       Delete the dictionary items with the following keys:

       ```python
       [
            'films',
            'vehicles',
            'starships',
            'created',
            'edited',
            'url'
        ]
        ```

       :exclamation: For the `homeworld` dictionary, retain the items for the keys specified in `home_keys_keep`.

       :exclamation: For the `species` list, retain _only_ the species name.

    4. Using the `.update()` method, update the passengers dictionary with the new information.

    `passengers` should look like:

    ```python
    [
        {
            'name': 'Han Solo',
            'category': 'captain',
            'boarding_order': 6,
            'height': '180',
            'mass': '80',
            ...
            'homeworld':
                {
                    'name': 'Corellia',
                    'rotation_period': '25',
                    ...
                }
            ...
        },
        {
            'name': 'Chewbacca',
            'category': 'co-pilot',
            'boarding_order': 1,
            'height': '228',
            ...
        }
        ...
    ]
    ```

## Problem 06 (20 points)

Let's help the passengers board the ship per a specified order.

1. Define a function called `board_ship()` that defines two parameters:

    `ship` (dict): A dictionary representation of a starship.

    `passengers` (list): A list of dictionaries with passenger information.

    This function _must_:

    1. Create a `deepcopy` of the `ship` dictionary.

    2. Using an accumulator pattern and the `boarding_order` key, populate a list with passengers according to the order that they boarded the starship. Use a nested `for` loop and the `range` object in your solution.

    3. Replace the passengers on the ship copy with this ordered list.

    4. Return the ship copy.

2. Inside `main()`, perform a new variable assignment as follows:

    1. Call the `board_ship()` function with `falcon_updated` and `passengers` as arguments. Assign
       the return value to the variable `all_aboard`.

## Problem 07 (10 points)

Let's help the Millennium Falcon get off Tatooine.

1. Implement the function named `write_json()` that defines six parameters:

   1. Required
       * filepath (str): the path to the file
       * data (dict)/(list): the data to be encoded as JSON and written to the file
   2. Optional
       * encoding (str): name of encoding used to encode the file (Default value is `utf-8`)
       * ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise non-ASCII
         characters are escaped (Default value is `False`).
       * indent (int): number of "pretty printed" indention spaces applied to encoded JSON (Default
         value is `2`)

    This function _must_:

    1. Use the built-in `open` function to open the file.

    2. Use `json.dump()` to "dump" or serialize a dictionary or list of dictionaries as JSON and
       write it to a target `JSON` file.

2. Inside `main()`, call `write_json()` and create a JSON file named `hyperspace_jump.json`. Do the
   following:

    1. Assign the filepath to a variable named `leaving_tatooine`.

    2. Using *keyword arguments* in **reverse order**, call the `write_json()` function to write the `all_aboard` dictionary to the file specified in `leaving_tatooine`.

    :exclamation: Specify only the required arguments when calling the function; passing default
    values for optional arguments when calling the function is redundant and unnecessary.
