import requests
import json
import os

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
def read_json(filepath):
    """Reads a JSON document, decodes the file content, and returns a
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file

    Returns:
        dict: dict representations of the decoded JSON document
    """

    with open(filepath, 'r') as file_obj:
        return json.load(file_obj)

def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
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

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)

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

    def __init__(self, name, diameter, climate, system, population, orbital_position):
        """Initialize a Planet instance."""
        self.name = name
        self.diameter = diameter
        self.climate = climate
        self.system = system
        self.population = population
        self.orbital_position = orbital_position

    def __str__(self):
        """Return a string representation of the object."""
        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        return {
            'name': self.name,
            'diameter': self.diameter,
            'climate': self.climate,
            'system': self.system,
            'population': self.population,
            'orbital_position': self.orbital_position
            }

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
    def __init__(self, url, name, birth_year, height, mass):
        """Initialize a Person instance."""
        self.url = url
        self.name = name
        self.birth_year = birth_year
        self.height = height
        self.mass = mass
        self.homeworld = None

    def __str__(self):
        """Return a string representation of the object."""
        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        if self.homeworld:
            homeworld = self.homeworld.jsonable()
        else:
            homeworld = None

        return {
            'url': self.url,
            'name': self.name,
            'birth_year': self.birth_year,
            'height': self.height,
            'mass': self.mass,
            'homeworld': homeworld
            }

# END PROBLEM 03


# PROBLEM 04 (10 Points)
def main():
    """Entry point for program."""
    # step 1
    swapi_luke = get_swapi_resource(f"{ENDPOINT}/people", {'search': 'Luke Skywalker'})['results'][0]

    print(f"Luke Skywalker's Data From SWAPI = {swapi_luke}\n")

    # step 2
    luke = Person(
        swapi_luke['url'],
        swapi_luke['name'],
        swapi_luke['birth_year'],
        float(swapi_luke['height']),
        float(swapi_luke['mass'])
        )

    print(f"Luke Skywalker's Profile = {luke}\n")

    # step 3
    # abs_path = os.path.dirname(os.path.abspath(__file__))
    # filepath = os.path.join(abs_path, 'tatooine.json')
    filepath = 'tatooine.json'
    tatooine_data = read_json(filepath)

    print(f"Tatooine Data from tatooine.json File = {tatooine_data}\n")

    # step 4
    swapi_tatooine = get_swapi_resource(f"{ENDPOINT}/planets", {'search': 'Tatooine'})['results'][0]

    print(f"Tatooine Data from SWAPI = {swapi_tatooine}\n")

    # step 5
    swapi_tatooine.update(tatooine_data)

    print(f"Enriched Tatooine Data = {swapi_tatooine}\n")

    # step 6
    tatooine = Planet(
        swapi_tatooine['name'],
        float(swapi_tatooine['diameter']),
        swapi_tatooine['climate'],
        swapi_tatooine['system'],
        int(swapi_tatooine['population']),
        swapi_tatooine['orbital_position']
        )

    print(f"Updated Tatooine Data = {tatooine}\n")

    # step 7
    luke.homeworld = tatooine

    # step 8
    luke_profile = luke.jsonable()

    print(f"luke_profile = {luke_profile}")

    # step 9
    write_json('luke_profile.json', luke_profile)

# END PROBLEM 04

if __name__ == '__main__':
    main()

# END OF LAB EXERCISE