# Problem 2.0
class Planet:
    """Representation of a planet.
    Attributes:
        url (str): identifier/locator
        name (str): planet name
        rotation_period (int): rotation period
        orbital_period (int): orbital period
        diameter (int): diameter of the planet
        climate (list): climate type(s) found on planet
        gravity (dict): gravity level
        terrain (list): terrain type(s) found on planet
        surface_water (float): surface water
        population (int): population size
    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    # Problem 2.1
    def __init__(self, url, name):
        """Initialize a Planet instance."""
        pass

    # Problem 2.2
    def __str__(self):
        """Return a string representation of the object."""
        pass

    # Problem 2.3
    def has_surface_water(self):
        """Return a boolean representation of whether the planet has surface water."""
        pass

    # Problem 2.5
    def is_populated(self):
        """Return a boolean representation of whether the planet has population."""
        pass

    # Problem 2.6
    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use the order specified in the Docstring above.
        Use a dictionary literal rather than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.
        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """

        pass

# Problem 3.0
def convert_data(planet):
    """Convert string values of a dictionary to the appropriate type whenever possible.
    Remember to set the value to None when the string is "unknown".

    Type conversions:
        rotation_period (str->int)
        orbital_period (str->int)
        diameter (str->int)
        climate (str->list) e.g. ["hot", "humid"]
        gravity (str->dict) e.g. {"measure": 0.75, "unit"; "standard"}
        terrain (str->list) e.g. ["fungus", "forests"]
        surface_water (str->float)
        population (str->int)

    Parameters:
        dict: dictionary of a planet
    Returns:
        dict: dictionary of a planet with its values converted
    """

    pass

# Problem 4.0
def create_planet(planet):
    """Creates a < Planet > instance from dictionary data. You must call the convert_data() function
    to clean up the planet dictionary first, then assign the dictionary to the instance.

    Parameters:
        planet (dict): planet as a dictionary
    Returns:
        Planet: new < Planet > instance
    """

    pass
