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

def clean_data(data):
    """
    This function takes in data and returns a mutated version that converts string versions of numbers
    to their integer or float form depending on the type of value.

    Parameters:
        data (list): A list of dictionaries.

    Returns:
        (list): A list of dictionaries with the numerical values appropriately converted.
    """

    for row in data:
        for key in row.keys():
            if key == 'points':
                row[key] = float(row[key])
            elif key == 'position':
                row[key] = int(row[key])

    return data

def convert_time_to_ms(driver_dict):
    """
    This function loops through the race results and converts a string with the time in the format mm:ss:msms
    to a single value in milliseconds (ms).

    Parameters:
        driver_dict (dict): A dictionary representation of a driver's race result.

    Returns:
        (int): The driver's fastest lap time in milliseconds.
    """

    lap_time_str = driver_dict['fastest_lap'].split(':')
    lap_time_ms = (int(lap_time_str[0])*60000) + (int(lap_time_str[1])*1000) + (int(lap_time_str[2]))

    return lap_time_ms

def add_fastest_lap_point(race_result):
    """
    This function adds a point to the driver who drove the fastest single lap in a race,
    if they placed above 10th place.

    Parameters:
        race_result (list): A list that contains the results from a race.

    Returns:
        (list): An updated list that contains the results from a race with the added point (if any).
    """

    fastest_lap = float('inf')
    fastest_driver = ''

    for driver in race_result:
        position = driver['position']
        lap_time = convert_time_to_ms(driver)
        if position <= 10 and lap_time < fastest_lap:
            fastest_lap = lap_time
            fastest_driver = driver['name']

    for driver in race_result:
        if driver['name'] == fastest_driver:
            points = driver['points']
            # driver.update({'points':points+1})
            driver['points'] = points + 1

    return race_result

def update_driver_standings(standings, race_result):
    """
    This function updates the driver's standings to reflect the points earned from a race.

    Parameters:
        standings (list): A list of dictionaries that contains the current driver's championship standings.
        race_result (list): A list of dictionaries that contains the results from a race.

    Returns:
        (list): The updated driver's standings list containing points earned from the given race.
    """

    for driver in race_result:
        for row in standings:
            if row['driver'] == driver['name']:
                row['points'] = driver['points'] + row['points']

    return standings

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
    nation1_points = 0
    nation1_driver_count = 0

    nation2_points = 0
    nation2_driver_count = 0

    for driver in standings:
        if driver['nationality'].lower() == nationality1.lower():
            nation1_points += driver['points']
            nation1_driver_count += 1
        elif driver['nationality'].lower() == nationality2.lower():
            nation2_points += driver['points']
            nation2_driver_count += 1

    nation1_avg = nation1_points / nation1_driver_count
    nation2_avg = nation2_points / nation2_driver_count

    if nation1_avg > nation2_avg:
        return (nationality1, round(nation1_avg, 1))
    elif nation2_avg > nation1_avg:
        return (nationality2, round(nation2_avg, 1))

#Main function
def main():
    """
    This function serves as the main point of entry point of the program
    """

    # PROBLEM 1
    standings = read_csv_to_dicts('./driver_standings_pre_USGP.csv')
    race_result = read_csv_to_dicts('./usgp_results.csv')

    # print(f'\n{standings}')
    # print(f'\n{race_result}')

    last_standing_keys = standings[-1].keys()
    #print(f'\n{last_standing_keys}')

    third_standing_values = standings[2].values()
    # print(f'\n{third_standing_values}')

    tenth_race_result_kv = race_result[-11].items()
    # print(f'\n{tenth_race_result_kv}')

    # PROBLEM 2
    cleaned_standings = clean_data(standings)
    # print(f'\nCleaned standings:\n{cleaned_standings}')

    cleaned_race_result = clean_data(race_result)
    # print(f'\nCleaned race results:\n{cleaned_race_result}')

    # PROBLEM 3 (Optional Check)

    antonio_lap_time_ms = convert_time_to_ms(cleaned_race_result[0])
    # print(f'\nAntonio Giovinazzi fastest lap time (in ms): {antonio_lap_time_ms} ms')

    # PROBLEM 4
    updated_race_result = add_fastest_lap_point(cleaned_race_result)
    # print(f'\nUpdated race results:\n{updated_race_result}')

    # PROBLEM 5
    updated_standings = update_driver_standings(cleaned_standings, updated_race_result)
    # print(f'\nUpdated standings:\n{updated_standings}')

    # PROBLEM 6
    ger_vs_gbr = compare_points_by_nation(updated_standings, "German", "British")
    # print(f'\n{ger_vs_gbr}')

    fra_vs_spa = compare_points_by_nation(updated_standings, "French", "Spanish")
    # print(f'\n{fra_vs_spa}')

    # PROBLEM 7
    write_filepath = 'driver_standings_post_USGP.csv'
    write_fieldnames = list(updated_standings[0].keys())

    # write_dicts_to_csv(filepath=write_filepath, data=updated_standings, fieldnames=write_fieldnames)

#DO NOT EDIT
if __name__ == '__main__':
    main()
