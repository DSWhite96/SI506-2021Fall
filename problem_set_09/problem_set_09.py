""" start setup """

import json
import requests
PEOPLE_URL = 'http://swapi.py4e.com/api/people/'

""" end setup """

# Problem 1.0
class Droid():

    # Problem 1.1
    def __init__(self):
        """
        The constructor of the `Droid` class. This method takes in the given parameters
        and assigns them to the attributes (instance variables) of the class. It then creates
        additional attributes and assigns them with the specified values.
        Parameters:
            name (string): name of the Droid we are looking for
            height (string): height of the Droid we are looking for
            mass (string): mass of the Droid we are looking for
        Additional Attribute:
            languages (None): this is not a parameter, but should be created as an attribute of the class
                              and assigned the value None. We will load a language database into this
                              attribute later.
        Returns:
            None
        """
        pass

    # Problem 1.2
    def __str__(self):
        """
        This method provides a readable string representation of the object.
        Parameters:
            None
        Returns:
            string: If languages != None, returns an f-string with the following syntax:
                    '< name > is a droid with height < height > and mass < mass >. Status: operational.'
            string: If languages == None, returns an f-string with the following syntax:
                '   < name > is a droid with height < height > and mass < mass >. Status: not operational.'
        """
        pass

    # Problem 1.3
    def load_languages(self):
        """
        Assigns the parameter languages to the instance variable languages.
        Parameters:
            languages (Languages object): an object of the Languages class
        Returns:
            None
        """
        pass

    # Problem 1.4
    def jsonable(self):
        """
        This method returns a JSON-friendly representation of the `Droid` object.
        The key should be the name of instance variable and value should be the corresponding value.
        For example, self.title should be converted in this way:
        {"title": self.title}
        If languages != None, make sure to call the `jsonable` method on languages.
        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        pass


# Problem 2.0
class Languages():

    # Problem 2.1
    def __init__(self):
        """
        The constructor of the `Languages` class. This method creates
        attributes and assigns them with the specified values.
        Parameters:
            This method takes no parameters
        Additional Attributes:
            language_database (dict): a dictionary of language information (set to an empty dictionary)
            language_count (string): number of languages in the dictionary (set to 0)
        Returns:
            None
        """
        pass

    # Problem 2.2
    def __str__(self):
        """
        This method provides a readable string representation of the object.
        Parameters:
            None
        Returns:
            string: An f-string with the following syntax:
                    'This language database currently contains < language_count > language entries.'
        """
        pass

    # Problem 2.3
    def add_language(self):
        """
        This method takes a dictionary representing a species. If the species' language is not in the
        `language_database` dictionary, this method should createa new dictionary entry with the language
        as the key and a list containing a tuple in which the species' name is at index 0 and the species'
        homeworld is at index 1. If the species' language is already in the `language_database` dictionary,
        this method should append a tuple in which the species' name is at index 0 and the species'
        homeworld is at index 1 to the language's associated value, a list.
        Paramters:
            species (dict): a dict representing a species
        Returns:
            None
        """
        pass

    # Problem 2.4
    def update_language_count(self):
        """
        This method takes the length of `language_database` and stores it in the lanugage_count variable
        Parameters:
            None
        Returns:
            None
        """
        pass

    # Problem 2.5
    def get_speakers(self):
        """
        This method returns a list of tuples from the `language_database` dictionary representing
        the speakers of a language.
        Parameters:
            language (string): a string representing a language
        Returns:
            list: a list from the `language_database` dictionary representing the speakers of a language
        """
        pass

    # Problem 2.6
    def jsonable(self):
        """
        This method returns a JSON-friendly representation of the `Languages` object.
        The key should be the name of instance variable and value should be the corresponding value.
        For example, self.title should be converted in this way:
        {"title": self.title}
        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        pass



# Problem 3.1
def read_json():
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

# Problem 4.0
def get_swapi_resource():
    """
    This function initiates an HTTP GET request to the SWAPI service in order to return a
    representation of a resource. `params` is not included in the request if no params is passed to this
    function during the function call. Once a response is received, it is converted to a python dict.
    Parameters:
        resource (string): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments. The default value is None.
        timeout (int): timeout value in seconds. The default value is 20.
    Returns:
        dict: dictionary representation of the decoded JSON.
    """
    pass

# Problem 5.1
def fill_language_database():
    """
    This function takes a list of dictionaries representing species and uses the information therin to fill
    a language database. This function should skip the 'Droid' species. For all other species, it should
    replace the url string at the 'homeworld' key with the name of the homeworld planet. It should then pass
    the updated dictionary to the `language_database`'s `add_language` method.
    Parameters:
        species_data (list): a list of dicts, with each dict representing a single species
        language_database (Languages object): an instance of the Languages class
    Returns:
        language_database (Languages object): an instance of the Languages class loaded with language data
    """
    pass

# Problem 6.2
def create_droid():
    """
    This function takes one parameter, a dictionary, represnting a person and returns
    an instance of the Droid class.
    Parameters:
        data (dict): a dictionary representing a person
    Returns:
        Droid object: an instance of the Droid class
    """
    pass

# Problem 7.1
def write_json():
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
    # Problem 3.2

    # Problem 5.2

    #print(f'Testing language_database: {language_database}')

    # Problem 6.1

    # Problem 6.3

    #print(f'Testing c3po: {c3po}')

    # Problem 7.2

    pass

if __name__ == '__main__':
    main()
