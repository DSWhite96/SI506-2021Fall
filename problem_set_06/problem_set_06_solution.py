import csv
import copy

#Problem 01
def read_csv(filepath, encoding='utf-8'):
    """
    This function reads in a csv and returns its contents as a list

    Parameters:
        filepath (str): A str representing the filepath for the file to be read
        encoding (str): A str representing the character encoding of the file

    Returns:
        (list): A list with the content of the file
    """
    with open(filepath, 'r', encoding=encoding) as file:
        reader = csv.reader(file)
        data = []
        for line in reader:
            data.append(line)
        return data

#Problem 02
def add_ratings(shows, ratings):
    """
    This function makes a copy of a show list and adds the shows IMDb rating to it

    Parameters:
        shows (list): A list of shows
        ratings (list): A list of IMDb ratings for the shows

    Returns:
        (list): A list of shows with the ratings added
    """
    show_copy = copy.deepcopy(shows)
    show_copy[0].append("IMDb Rating")
    for show in show_copy[1:]:
        for rating in ratings:
            if rating[0].lower() == show[0].lower():
                show.append(rating[1])
    return show_copy

#Problem 03
def clean_show_data(shows):
    """
    This function cleans the data of a list of shows

    Parameters:
        shows (list): A list of shows

    Returns:
        (list): The list of shows with clean data
    """
    show_copy = copy.deepcopy(shows)
    for show in show_copy[1:]:
        show[1] = show[1].split('/')
        show[2] = show[2].split('/')
        show[3] = float(show[3])
    return show_copy

#Problem 04
def get_highest_rated_show(shows):
    """
    This function loops through a list of shows and returns the name and creators of
    the highest rated show

    Parameters:
        shows (list): A list of shows

    Returns:
        (list): A list representing the show with the highest rating
    """
    highest_rating = 0
    highest_rated_show = None
    for show in shows[1:]:
        if show[-1] > highest_rating:
            highest_rating = show[-1]
            highest_rated_show = (show[0], show[1])
    return highest_rated_show

#Problem 05
def filter_by_genre(shows, genre):
    """
    This function filters a list of shows by genre.

    Parameters:
        shows (list): A list of shows
        genre (str): A string representing a genre of shows

    Returns:
        (list): A list of shows that match the given genre
    """
    filtered_shows = []
    for show in shows:
        for show_genre in show[2]:
            if genre.lower() == show_genre.lower():
                filtered_shows.append(show)
    return filtered_shows

#Problem 06
def stringify(shows):
    """
    This function converts the creator and genre lists in a show to a format that will
    be easier to read in a CSV file

    Parameters:
        shows (list): A list of shows

    Returns:
        (list): A list of shows where the creators and genres have been reformatted
    """
    show_copy = copy.deepcopy(shows)
    for show in show_copy[1:]:
        show[1] = '/'.join(show[1])
        show[2] = '/'.join(show[2])
    return show_copy

#Problem 07
def write_csv(filepath, data):
    """
    This function writes a given data list to a file.

    Parameters:
        filepath (str): A string with the path of the file to be written
        data (list): A list with content that will be written to a file
    """
    with open(filepath, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

#Main function
def main():
    """
    This function serves as the main point of entry point of the program
    """
    #Problem 01
    netflix_data = read_csv('netflix_data.csv')
    disney_data = read_csv('disney_data.csv')
    netflix_ratings = read_csv('netflix_ratings.csv')
    disney_ratings = read_csv('disney_ratings.csv')

    print(disney_data)
    print(disney_ratings)

    #Problem 02
    netflix_data_with_ratings = add_ratings(netflix_data, netflix_ratings)
    disney_data_with_ratings = add_ratings(disney_data, disney_ratings)

    print(disney_data_with_ratings)

    #Problem 03
    clean_netflix_data = clean_show_data(netflix_data_with_ratings)
    clean_disney_data = clean_show_data(disney_data_with_ratings)
    print(clean_disney_data)

    #Problem 04
    best_netflix_show = get_highest_rated_show(clean_netflix_data)
    best_disney_show = get_highest_rated_show(clean_disney_data)
    print(best_disney_show)

    #Problem 05
    sci_fi_shows = [['Title', 'Creator(s)', 'Genre(s)', 'IMDb Rating']]
    sci_fi_shows.extend(filter_by_genre(clean_netflix_data, 'Science Fiction'))
    sci_fi_shows.extend(filter_by_genre(clean_disney_data, 'Science Fiction'))
    print(sci_fi_shows)
    print(filter_by_genre(clean_netflix_data, 'drama'))

    #Problem 06
    stringified_sci_fi_shows = stringify(sci_fi_shows)
    print(sci_fi_shows)
    print(stringified_sci_fi_shows)

    #Problem 07
    write_csv('sci_fi_shows.csv', stringified_sci_fi_shows)

    # WARN: if variables in the tuple below are not yet defined, initialize them to zero (0)
    return (netflix_data, disney_data, netflix_ratings, disney_ratings, netflix_data_with_ratings,
    disney_data_with_ratings, clean_netflix_data, clean_disney_data, best_netflix_show, best_disney_show
    )

#Do not delete
if __name__ == '__main__':
    main()
