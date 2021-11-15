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

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


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

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()


# Problem 03
def delete_items(dictionary, key_list):
    """
    This function performs a deep copy of a dictionary, checks if the
    specified keys are included in the copy, and deletes key-value pairs
    accordingly.
    Parameters:
        dictionary (dict): a dictionary
        key_list (list): a list of the keys to be deleted
    Returns:
        dict_copy (dict): dictionary with key-value pairs removed
    """
    dict_copy = copy.deepcopy(dictionary)
    for k in key_list:
        if k in dict_copy.keys():
            del(dict_copy[k])
    return dict_copy


# Problem 04
def get_homeworld(person, key_list=None):
    """
    This function gets a SWAPI representation of a person's
    homeworld by accessing the link included in their dictionary.
    Parameters:
        person (dict): A dictionary representation of a person
        key_list (list): Optional list of keys to keep in returned dictionary.
                        Default value is None.
    Returns:
        dict: A dictionary representation of a person's homeworld
    """
    home = get_swapi_resource(person['homeworld'])
    if key_list:
        details = {}
        for key in key_list:
            details[key] = home[key]
        return details
    else:
        return home


def get_species(person, key_list=None):
    """
    This function gets a SWAPI representation of a person's
    species by accessing the link included in their dictionary.
    Parameters:
        person (dict): A dictionary representation of a person
        key_list (list): A list of keys to keep in returned dictionary
    Returns:
        dict: A dictionary of a <species>
    """
    species_list = person['species']
    details_dict = {}

    if len(species_list) > 0:
        species_dict = get_swapi_resource(species_list[0])
        if key_list:
            for key in key_list:
                details_dict[key] = species_dict[key]
            # details_list.append(details_dict)
        else:
            # details_list.append(species_dict)
            details_dict = species_dict
    return details_dict


# Problem 05
def clean_person_dictionary(person, delete_list, home_list=None, species_list=None):
    """
    This function deletes unwanted key-value pairs from a person's dictionary
    and updates the homeworld and species values with dictionary representations.
    Parameters:
        person (dict): A dictionary representation of a person
        delete_list (list): A list of keys to be deleted from person
        home_list (list): Optional list of keys to keep in the homeworld dictionary.
                         Default value is None.
        species_list (list): Optional list of keys to keep in the species dictionary.
                            Default value is None.
    Returns:
        person_cleaned (dict): An updated representation of a person
        """
    person_cleaned = delete_items(person, delete_list)
    home = get_homeworld(person_cleaned, home_list)
    species = get_species(person_cleaned, species_list)
    person_cleaned['homeworld'] = home
    person_cleaned['species'] = species
    return person_cleaned


# Problem 06
def board_ship(ship, passengers):
    """
    This function creates a deep copy of a dictionary <starship>
    and generates a list <passengers> sorted by the order they boarded
    the starship. It then updates the copy of the dictionary <starship>
    with this information.
    Parameters:
        ship (dict): A dictionary representation of a starship
        passengers (list): A list of dicionaries with passenger information
    Returns:
        ship_copy (dict): A deep copy of the ship dictionary
    """
    ship_copy = copy.deepcopy(ship)
    sorted_passengers = []
    for i in range(1, len(passengers) + 1):
        for passenger in passengers:
            if passenger['boarding_order'] == i:
                sorted_passengers.append(passenger)

    ship_copy['passengers'] = sorted_passengers
    return ship_copy

# Problem 07
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


def main():
    """Program entry point."""

    # Problem 01
    filepath = './passengers.json'
    passengers = read_json(filepath)['passengers']

    print(f'\nProblem 01:\n{passengers}')

    # Problem 02
    base_url = 'https://swapi.py4e.com/api/'
    falcon_params = {'search': 'falcon'}
    falcon = get_swapi_resource(base_url + 'starships/', falcon_params)['results'][0]

    print(f'\nProblem 02:\n{falcon}')

    # Problem 03
    falcon_keys_delete = list(falcon.keys())[-5:]
    falcon_updated = delete_items(falcon, falcon_keys_delete)

    print(f'\nProblem 03:\n{falcon_updated}')
    print(f'\n{falcon_keys_delete}')

    # Problem 04

    ppl_url = base_url + 'people/'
    bail = get_swapi_resource(ppl_url, {'search': 'bail'})['results'][0]

    print(f'\nBail Organa dictionary:\n{bail}')

    bail_home = get_homeworld(bail)
    home_keys_keep = list(bail_home.keys())[:9]
    bail_species = get_species(bail)

    print(f'\nProblem 04.3.1:\n{bail_home}')
    print(f'\nProblem 04.3.2:\n{home_keys_keep}')
    print(f'\nProblem 04.3.3:\n{bail_species}')

    # Problem 05
    ppl_keys_delete = ['films']
    ppl_keys_delete.extend(list(bail.keys())[11:])

    print(ppl_keys_delete)

    for info in passengers:
        name = info['name']
        passenger = get_swapi_resource(ppl_url, {'search': name})['results'][0]
        passenger_cleaned = clean_person_dictionary(
            passenger,
            ppl_keys_delete,
            home_keys_keep,
            ['name'])
        info.update(passenger_cleaned)

    print(f'\nProblem 05:\n{passengers}')

    # Problem 06
    all_aboard = board_ship(falcon_updated, passengers)

    print(f'\nProblem 06:\n{all_aboard}')

    # Problem 07
    leaving_tatooine = './hyperspace_jump.json'
    write_json(data=all_aboard, filepath=leaving_tatooine)


if __name__ == '__main__':
    main()
