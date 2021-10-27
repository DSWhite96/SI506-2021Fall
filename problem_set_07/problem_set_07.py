import csv

def read_csv_to_dicts(filepath, encoding='utf-8-sig', newline='', delimiter=','):
    """
    NOTE: This is a helper function - please do NOT edit or delete it.

    Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data

def write_dicts_to_csv(filepath, data, fieldnames, encoding='utf-8', newline=''):
    """
    NOTE: This is a helper function - please do NOT edit or delete it.

    Writes dictionary data to a target CSV file as row data using the csv.DictWriter().
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): dictionary content to be written to the target file
        fieldnames (seq): sequence specifing order in which key-value pairs are written to each row
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

        writer.writeheader() # first row
        writer.writerows(data)

# PROBLEM 2


def clean_data(data):
    """
    This function takes in data and returns a mutated version that converts string versions of numbers
    to their integer or float form depending on the type of value.

    Parameters:
        data (list): A list of dictionaries.

    Returns:
        (list): A list of dictionaries with the numerical values appropriately converted.
    """

    pass #TODO: Implement

# PROBLEM 3


# PROBLEM 4


# PROBLEM 5


# PROBLEM 6


def compare_points_by_nation(standings, nationality1, nationality2):
    """
    This function calculates the average points for all drivers for two nations and returns
    a tuple with the name and average points for the nation with the higher average points.

    Parameters:
        standings (list): A list of dictionaries that contains the drivers' standings.
        nationality1 (str): A string signifying the first nationality to be checked for.
        nationality2 (str): A string signifying the second nationality to be checked for.

    Returns:
        (tuple): A tuple with the nationality and average points for the nation with
        the higher average points.
    """

    pass #TODO: Implement

#Main function
def main():
    """
    This function serves as the main point of entry point of the program
    """

    # PROBLEM 1
    standings = None
    race_result = None

    # print(f'\n{standings}')
    # print(f'\n{race_result}')

    last_standing_keys = None
    # print(f'\n{last_standing_keys}') # Uncomment to test

    third_standing_values = None
    # print(f'\n{third_standing_values}') # Uncomment to test

    tenth_race_result_kv = None
    # print(f'\n{tenth_race_result_kv}') # Uncomment to test

    # PROBLEM 2
    cleaned_standings = None
    # print(f'\nCleaned standings:\n{cleaned_standings}')

    cleaned_race_result = None
    # print(f'\nCleaned race results:\n{cleaned_race_result}')

    # PROBLEM 3 (Optional Check)


    # PROBLEM 4


    # PROBLEM 5


    # PROBLEM 6


    # PROBLEM 7


#DO NOT EDIT
if __name__ == '__main__':
    main()
