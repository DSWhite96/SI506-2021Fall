import requests
import json

# LAB EXERCISE 09

# SETUP CODE
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

# END SETUP


# PROBLEM 01 (2 Points)
def read_json():
    """Reads a JSON document, decodes the file content, and returns a
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file

    Returns:
        dict: dict representations of the decoded JSON document
    """

    pass

def write_json():
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """

    pass

# END PROBLEM 01


# PROBLEM 02 (4 Points)
class Planet:
    """
    Representation of a planet.

    Instance Variables:
        name (str): name of the planet.
        diameter (float): diameter of the planet measured in kilometers.
        climate (str): climate type(s) found on the planet.
        system(str): name of the planetary system.
        population (int): population size.
        orbital_position(str): position from the sun.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__():
        """Initialize a Planet instance."""
        pass

    def __str__():
        """Return a string representation of the object."""
        pass

    def jsonable():
        """Return a JSON-friendly representation of the object.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        pass

# END PROBLEM 02


# PROBLEM 03 (4 Points)
class Person:
    """
    Representation of a person.

    Instance Variables:
        url (str): identifer/locator
        name (str): person's name
        birth_year (str): person's birth_year
        height (float): height of the person measured in centimeters.
        mass (float): person's weight in kilograms
        homeworld (Planet): person's home planet (optional)

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """
    def __init__():
        """Initialize a Person instance."""
        pass

    def __str__():
        """Return a string representation of the object."""
        pass

    def jsonable():
        """Return a JSON-friendly representation of the object.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        pass

# END PROBLEM 03


# PROBLEM 04 (10 Points)
def main():
    """Entry point for program."""
    # step 1
    swapi_luke = None

    print(f"Luke Skywalker's Data From SWAPI = {swapi_luke}\n")

    # step 2
    luke = None

    print(f"Luke Skywalker's Profile = {luke}\n")

    # step 3


    # step 4


    # step 5


    # step 6


    # step 7


    # step 8


    # step 9


# END PROBLEM 04

if __name__ == '__main__':
    main()

# END OF LAB EXERCISE