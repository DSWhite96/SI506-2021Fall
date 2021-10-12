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
    pass #TODO: Replace and Implement

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
    pass #TODO: Replace and Implement

#Problem 03
def clean_show_data(shows):
    """
    This function cleans the data of a list of shows

    Parameters:
        shows (list): A list of shows

    Returns:
        (list): The list of shows with clean data
    """
    pass #TODO: Replace and Implement

#Problem 04

#Problem 05

#Problem 06

#Problem 07

#Main function
def main():
    """
    This function serves as the main point of entry point of the program
    """
    #Problem 01
    netflix_data = None #TODO: Replace
    disney_data = None #TODO: Replace
    netflix_ratings = None #TODO: Replace
    disney_ratings = None #TODO: Replace

    #Problem 02
    netflix_data_with_ratings = None #TODO: Replace
    disney_data_with_ratings = None #TODO: Replace

    #Problem 03
    clean_netflix_data = None #TODO: Replace
    clean_disney_data = None #TODO: Replace

    #Problem 04
    best_netflix_show = None #TODO: Replace
    best_disney_show = None #TODO: Replace

    #Problem 05

    #Problem 06

    #Problem 07

    # WARN: if variables in the tuple below are not yet defined, initialize them to zero (0)
    return (netflix_data, disney_data, netflix_ratings, disney_ratings, netflix_data_with_ratings,
    disney_data_with_ratings, clean_netflix_data, clean_disney_data, best_netflix_show, best_disney_show
    )

#Do not delete
if __name__ == '__main__':
    main()
