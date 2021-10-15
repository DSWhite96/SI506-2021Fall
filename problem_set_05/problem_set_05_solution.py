# SI 506 Problem Set 05

import csv
import copy


print("Problem 01\n\n")


# Problem 01: Implement read_csv and load the election data.
def read_csv(filepath):
    """
    This function takes a filepath for a csv as an argument and returns a list of lists, each
    representing a party's election results.

    Parameters:
        filepath (str): A filepath of a csv file to be read from

    Returns:
        (list): A list of lists, each representing a party's election results
    """
    with open(filepath, 'r', encoding='utf-8-sig') as file:
        new_list = []
        reader = csv.reader(file)
        for line in reader:
            new_list.append(line)
        return new_list

raw_election_data_2021 = read_csv('election_data_2021.csv')
raw_election_data_2017 = read_csv('election_data_2017.csv')
print(raw_election_data_2021)
print(raw_election_data_2017)

print("\n\nProblem 02\n\n")


# Problem 02: Implement clean and clean the election data.
def clean(data):
    """
    This function takes a list of lists as an argument, makes a deep copy of the list, and, within the deep copy,
    strips strings of trailing whitespece converted and converts numbers to integers.

    Parameters:
        data (list): A list of lists, each representing a party's election results

    Returns:
        clean_data (list): a list of lists with clean data, each representing a party's election results
    """
    new_data = copy.deepcopy(data)
    for line in new_data[1:]:
        line[0] = line[0].strip()
        line[1] = int(line[1])
        line[2] = line[2].lower().strip()
    return new_data

clean_election_data_2021 = clean(raw_election_data_2021)
clean_election_data_2017 = clean(raw_election_data_2017)
print(clean_election_data_2021)
print(clean_election_data_2017)


print("\n\nProblem 03\n\n")


# Problem 03: Implement get_party_seat_differences and get the party seat differences for the 2021 election.
def get_seat_differences(current_election, previous_election):
    """
    This function takes two lists of lists as arguments, with each list representing a party's election results
    and returns a list of tuples, with each tuple representing a party's name and the seats they lost or gained
    between the current and previous elections.

    Parameters:
        current_election (list): A list of lists, each representing a party's more recent election results
        previous_election (list): A list of lists, each representing a party's previous election results

    Returns:
        A list of tuples with party name at index 0 and seat difference at index 1
    """
    party_seat_differences = []
    for current_party_result in current_election[1:]:
        for previous_party_result in previous_election[1:]:
            if previous_party_result[0].lower() == current_party_result[0].lower():
                seat_diff = current_party_result[1] - previous_party_result[1]
                party_seat_differences.append((current_party_result[0], seat_diff))
    return party_seat_differences

party_seat_differences = get_seat_differences(clean_election_data_2021, clean_election_data_2017)
print(party_seat_differences)


print("\n\nProblem 04\n\n")


# Problem 04: Implement get_leaders and get the leaders for the 2021 election data.
party_leaders_2021 = [
                        ('AfD', 'Joerg Meuthen and Tino Chrupalla'),
                        ('FDP', 'Christian Lindner'),
                        ('CDU/CSU', 'Armin Laschet'),
                        ('SPD', 'Olaf Scholz'),
                        ('Greens', 'Annalena Baerbock and Robert Habeck'),
                        ('Left', 'Janine Wissler and Susanne Hennig-Wellsow')
                    ]

def get_leaders(election_data, party_leaders):
    """
    This function takes one list of lists as an argument, with each list representing a party's election results, and one
    list of tuples, with each tuple containing (party name, part leader). It makes a deep copy of the list of lists and adds
    the party leader(s) to a new column of the election data.

    Parameters:
        election_data (list): A list of lists, each representing a party's election results
        party_leaders (list): A list of tuples, each representing a party and its current leader(s)

    Returns:
        A list of lists containing election data, including a column for party leader(s).

    """
    election_data_copy = copy.deepcopy(election_data)
    election_data_copy[0].append('Party Leader(s)')
    for party in election_data_copy[1:]:
        for party_tuple in party_leaders:
            party_name, party_leader = party_tuple
            if party_name.lower() == party[0].lower():
                party.append(party_leader)
    return election_data_copy

election_data_2021_with_leaders = get_leaders(clean_election_data_2021, party_leaders_2021)
print(election_data_2021_with_leaders)


print("\n\nProblem 05\n\n")


# Problem 05: Implement get_seats_percent and get affiliation percents for the 2021 election data.
def get_seats_percent(election_data):
    """
    This function takes a lists of lists as and argument, with each list representing a party's election results,
    and returns a tuple with the percentage of Bundestag seats won by various political affiliations.

    Parameters:
        election_data (list): A list of lists, each representing a party's election results

    Returns:
        A tuple with percentage of Bundestag seats won by various political affiliations
    """

    left_seats = 0
    right_seats = 0
    extreme_seats = 0
    center_seats = 0
    total_bundestag_seats = 0

    for party in election_data[1:]:
        total_bundestag_seats += int(party[1])
        if 'far' in party[2]:
            extreme_seats += party[1]
        else:
            center_seats += party[1]
        if 'left' in party[2]:
            left_seats += party[1]
        else:
            right_seats += party[1]

    left_percent = round((left_seats / total_bundestag_seats * 100), 2)
    right_percent = round((right_seats / total_bundestag_seats * 100), 2)
    extreme_percent = round((extreme_seats / total_bundestag_seats * 100), 2)
    center_percent = round((center_seats / total_bundestag_seats * 100), 2)

    return left_percent, right_percent, extreme_percent, center_percent

affiliation_percents = get_seats_percent(election_data_2021_with_leaders)
print(affiliation_percents)


print("\n\nProblem 06\n\n")


# Problem 06: Implement write_csv and write election_data_2021_with_leaders to a file called revised_election_data_2021.csv.
def write_csv(filepath, data):
    """
    This function takes a csv filepath and a list of lists as arguments and outputs them
    to the specified csv file.

    Parameters:
        filepath (str): A filepath of a csv file to be written to
        data (list): A list of lists, each representing a party's election results

    Returns:
        None
    """
    with open(filepath, "w", encoding='utf-8', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

write_csv('revised_election_data_2021.csv', election_data_2021_with_leaders)
test = read_csv('revised_election_data_2021.csv')
print(test)
