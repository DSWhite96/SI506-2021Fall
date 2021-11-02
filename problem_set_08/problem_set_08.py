import json, requests, copy


# Problem 01
def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    pass # TODO Implement


# Problem 02
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


# Problem 03


# Problem 04


# Problem 05


# Problem 06


# Problem 07


def main():
    """Program entry point."""

    # Problem 01
    passengers = None

    # print(f'\nProblem 01:\n{passengers}')

    # Problem 02
    base_url = None
    falcon_params = None
    falcon = None

    # print(f'\nProblem 02:\n{falcon}')

    # Problem 03


    # Problem 04


    # Problem 05


    # Problem 06


    # Problem 07



if __name__ == '__main__':
    main()
