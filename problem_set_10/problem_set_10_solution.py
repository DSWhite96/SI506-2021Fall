import json
import swapi_entities_solution as ent

# import swapi_entities_solution as ent # local testing only

# Problem 1.0
def read_json(filepath, encoding='utf-8'):
    """
    Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.
    Parameters:
        filepath (string): path to file
        encoding (string): optional name of encoding used to decode the file. The default is 'utf-8'.
    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)

# Problem 1.0
def write_json(filepath, data):
    """
    This function dumps the JSON object in the dictionary `data` into a file on
    `filepath`.
    Parameters:
        filepath (string): The location and filename of the file to store the JSON
        data (dict): The dictionary that contains the JSON representation of the objects.
    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


def main():
    # Problem 1.0
    planet_data = read_json("./swapi_planets.json")

    # Problem 1.0 - Problem 4.0
    # Complete in problem_set_10_utils.py

    # Problem 5.0
    global planets
    planets = {}
    for planet in planet_data:
        cleaned_planet_ins = ent.create_planet(planet)
        planets[cleaned_planet_ins.name] = cleaned_planet_ins

    # Problem 6.0
    planets_with_surface_water = []
    planets_inhabited = []
    planets_uninhabited = []
    planets_desert_only = []
    planets_biggest_smallest = {"biggest": [], "smallest": []}

    tmp_biggest_diameter = list(planets.values())[0].diameter
    tmp_smallest_diameter = tmp_biggest_diameter

    for planet in planets.values():
        if planet.has_surface_water():
            planets_with_surface_water.append(planet.jsonable())

        if planet.is_populated():
            planets_inhabited.append(planet.jsonable())
        else:
            if planet.population == 0:
                planets_uninhabited.append(planet.jsonable())

        if planet.terrain and len(planet.terrain) == 1 and planet.terrain[0] == "desert":
            planets_desert_only.append(planet.jsonable())

        if planet.diameter or planet.diameter == 0:
            if planet.diameter >= tmp_biggest_diameter:
                if planet.diameter > tmp_biggest_diameter:
                    planets_biggest_smallest['biggest'] = []
                tmp_biggest_diameter = planet.diameter
                planets_biggest_smallest['biggest'].append(planet.jsonable())
            if planet.diameter <= tmp_smallest_diameter:
                if planet.diameter < tmp_smallest_diameter:
                    planets_biggest_smallest['smallest'] = []
                tmp_smallest_diameter = planet.diameter
                planets_biggest_smallest['smallest'].append(planet.jsonable())

    write_json("stu_planets_with_surface_water.json", planets_with_surface_water)
    write_json("stu_planets_biggest_smallest.json", planets_biggest_smallest)
    write_json("stu_planets_inhabited.json", planets_inhabited)
    write_json("stu_planets_uninhabited.json", planets_uninhabited)
    write_json("stu_planets_desert_only.json", planets_desert_only)


if __name__ == '__main__':
    main()
