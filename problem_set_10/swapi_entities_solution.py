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

        self.url = url
        self.name = name
        self.rotation_period = None
        self.orbital_period = None
        self.diameter = None
        self.climate = None
        self.gravity = None
        self.terrain = None
        self.surface_water = None
        self.population = None

    # Problem 2.2
    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    # Problem 2.3
    def has_surface_water(self):
        """Return a boolean representation of whether the planet has surface water."""

        if self.surface_water:
            return self.surface_water > 0 # returns either True or False
        else:
            return False

    # Problem 2.5
    def is_populated(self):
        """TODO"""

        if self.population:
            return self.population > 0 # returns either True or False
        else:
            return False

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

        return {
                'url': self.url,
                'name': self.name,
                'rotation_period': self.rotation_period,
                'orbital_period': self.orbital_period,
                'diameter': self.diameter,
                'climate': self.climate,
                'gravity': self.gravity,
                'terrain': self.terrain,
                'surface_water': self.surface_water,
                'population': self.population
            }

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

    for key, val in planet.items():
        if isinstance(val, str):
            if not val or val.lower() in ('n/a', 'none', 'unknown'):
                planet[key] = None
            else:
                if key in ('diameter', 'orbital_period', 'population', 'rotation_period'):
                    planet[key] = int(val)
                elif key in ('climate', 'terrain'):
                    planet[key] = val.strip().split(', ')
                elif key == 'surface_water':
                    planet[key] = float(val)
                elif key == 'gravity':
                    gravity = val.strip().split()
                    planet['gravity'] = {"measure": float(gravity[0]), "unit": "standard"}
                else:
                    continue

    return planet

    # if planet.get('rotation_period') == "unknown":
    #     planet['rotation_period'] = None
    # else:
    #     planet['rotation_period'] = int(planet['rotation_period'])

    # if planet.get('orbital_period') == "unknown":
    #     planet['orbital_period'] = None
    # else:
    #     planet['orbital_period'] = int(planet['orbital_period'])

    # if planet.get('diameter') == "unknown":
    #     planet['diameter'] = None
    # else:
    #     planet['diameter'] = int(planet['diameter'])

    # if planet.get('climate') == "unknown":
    #     planet['climate'] = None
    # else:
    #     planet['climate'] = planet['climate'].strip().split(', ')

    # if planet.get('gravity') == "unknown":
    #     planet['gravity'] = None
    # else:
    #     splitted = planet['gravity'].strip().split()
    #     if len(splitted) == 2:
    #         planet['gravity'] = {"measure": float(splitted[0]), "unit": splitted[1]}
    #     else:
    #         planet['gravity'] = {"measure": float(splitted[0]), "unit": "standard"}

    # if planet.get('terrain') == "unknown":
    #     planet['terrain'] = None
    # else:
    #     planet['terrain'] = planet['terrain'].strip().split(', ')

    # if planet.get('surface_water') == "unknown":
    #     planet['surface_water'] = None
    # else:
    #     planet['surface_water'] = float(planet['surface_water'])

    # if planet.get('population') == "unknown":
    #     planet['population'] = None
    # else:
    #     planet['population'] = int(planet['population'])

    # return planet


# Problem 4.0
def create_planet(planet):
    """Creates a < Planet > instance from dictionary data. You must call the convert_data() function to 
    clean up the planet dictionary first, then assign the dictionary to the instance.

    Parameters:
        planet (dict): planet as a dictionary
    Returns:
        Planet: new < Planet > instance
    """

    cleaned_planet = convert_data(planet)
    planet = Planet(cleaned_planet['url'], cleaned_planet['name'])

    planet.rotation_period = cleaned_planet['rotation_period']
    planet.orbital_period = cleaned_planet['orbital_period']
    planet.diameter = cleaned_planet['diameter']
    planet.climate = cleaned_planet['climate']
    planet.gravity = cleaned_planet['gravity']
    planet.terrain = cleaned_planet['terrain']
    planet.surface_water = cleaned_planet['surface_water']
    planet.population = cleaned_planet['population']

    return planet
