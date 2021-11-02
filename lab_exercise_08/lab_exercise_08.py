import json
import requests

# LAB EXERCISE 08

# SETUP CODE
ENDPOINT = 'https://swapi.py4e.com/api'

# END SETUP

# PROBLEM 01 (5 Points)

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

    pass # TODO Implement


# END PROBLEM 01

# PROBLEM 02 (2 Points)

# END PROBLEM 02

# PROBLEM 03 (5 Points)

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

    pass # TODO Implement

# END PROBLEM 03

# PROBLEM 04 (8 Points)

def main():
    """ This function calls <get_swapi_resource> function to retrieve SWAPI character data. Update values in < lars >.
    Then it calls <write_json> function to store data to a json file.

    Parameters:
        None

    Return:
        None
    """

    # Call < get_swapi_resource() > with the correct parameters and save results to < lars_data >

    # print(f"Owen Lars data = {lars_data}")


    # Retrieve Owen Lars's species and assign to < lars_species >

    # print(f"Owen Lars data w/Species = {lars_data}")


    # Update values in < lars >.

    # print(f"Owen Lars Dictionary = {lars}")


    # Write out the information of the dictionary < lars >


# END PROBLEM 04


if __name__ == '__main__':
    main()
