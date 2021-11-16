import json
import swapi_entities as ent

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

    pass

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

    pass

def main():
    # Problem 1.0
    planet_data = None

    # Problem 2.0 - Problem 4.0
    # Complete in problem_set_10_utils.py

    # Problem 5.2
    global planets
    planets = {}
    
    # Problem 6.0
    planets_with_surface_water = []
    planets_inhabited = []
    planets_uninhabited = []
    planets_desert_only = []
    planets_biggest_smallest = {"biggest": [], "smallest": []}
        
if __name__ == '__main__':
    main()
