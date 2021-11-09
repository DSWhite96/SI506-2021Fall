# LAB EXERCISE 07
print('Lab Exercise 07 \n')

# SETUP
restaurants = [
    {'Name': 'Frita Batidos', 'Location': '117 W Washington St', 'Rating': 4.5, 'Reviews': 1871, 'Category': 'Burgers'},
    {'Name': "Zingerman's Delicatessen", 'Location': '422 Detroit St', 'Rating': 4.0, 'Reviews': 2224, 'Category': 'Delis'},
    {'Name': "Scorekeepers", 'Location': '310 Maynard St', 'Rating': 2.5, 'Reviews': 59, 'Category': 'Burgers'},
    {'Name': 'Rich Jc Korean Restaurant', 'Location': '1313 S University Ave', 'Rating': 4.0, 'Reviews': 183, 'Category': 'Korean'},
    {'Name': 'Tomukun Noodle Bar', 'Location': '505 E Liberty St Ste 200', 'Rating': 4.0, 'Reviews': 773, 'Category': 'Noodles'},
    {'Name': "Sava's", 'Location': '216 S State St', 'Rating': 4.0, 'Reviews': 1195, 'Category': 'American'},
    {'Name': "Krazy Jim's Blimpy Burger", 'Location': '304 S Ashley St', 'Rating': 3.5, 'Reviews': 231, 'Category': 'Burgers'},
    {'Name': "Joe's Pizza", 'Location': '1107 S University Ave', 'Rating': 4.5, 'Reviews': 107, 'Category': 'Pizza'},
    {'Name': 'Hola Seoul', 'Location': '715 N University Ave', 'Rating': 4.0, 'Reviews': 98, 'Category': 'Korean'},
    {'Name': 'The Chop House', 'Location': '322 S Main St', 'Rating': 4.0, 'Reviews': 448, 'Category': 'Steakhouses'},
    {'Name': 'TK Wu', 'Location': '510 E Liberty St', 'Rating': 3.5, 'Reviews': 236, 'Category': 'Chinese'},
    {'Name': 'HopCat', 'Location': '311 Maynard St', 'Rating': 3.5, 'Reviews': 397, 'Category': 'Burgers'},
    {'Name': 'Lan City Noodle Bar', 'Location': '1235 S University Ave', 'Rating': 4.0, 'Reviews': 5, 'Category': 'Chinese'},
    {'Name': 'First Bite', 'Location': '108 S Main St', 'Rating': 5.0, 'Reviews': 104, 'Category': 'Burgers'}
]

# END SETUP

# Problem 01 (3 points)
def get_restaurants(restaurants, category=None):
    """
    This function takes a list of dictionaries as an argument and returns a list of strings that includes restaurants' names

    Parameters:
        restaurants (list): A list of dictionaries, each representing a restaurant
        category (list): A list of strings containing different categories of restaurants

    Returns:
        restaurants_names (list): A list containing the restaurants' names
    """
    restaurants_names = []

    for restaurant in restaurants:
        if category:
            if restaurant['Category'] in category:
                restaurants_names.append(restaurant['Name'])
        else:
            restaurants_names.append(restaurant['Name'])

    return restaurants_names

# Problem 02 (4 points)
def get_most_reviewed_restaurant(restaurants):
    """
    This function takes a list of dictionaries as an argument and returns a dictionary with the restaurant's name as value to the key 'Name' and the number of reviews as value to the key 'Reviews'

    Parameters:
        restaurants (list): A list of dictionaries, each representing a restaurant

    Returns:
        most_reviewed_restaurant (dict): A dictionary containing the restaurant's name and the number of reviews
    """
    most_reviewed_restaurant = {}
    num_reviews = 0

    for restaurant in restaurants:
        if restaurant['Reviews'] > num_reviews:
            most_reviewed_restaurant['Name'] = restaurant['Name']
            most_reviewed_restaurant['Reviews'] = restaurant['Reviews']
            num_reviews = restaurant['Reviews']

    return most_reviewed_restaurant


# Problem 03 (5 points)
def get_high_rating_restaurants(restaurants, category):
    """
    This function takes a list of dictionaries and a list of strings as arguments and returns a dictionary with the restaurant's name as key and rating as value.

    Parameters:
        restaurants (list): A list of dictionaries, each representing a restaurant
        category (list): A list of strings containing different categories of restaurants

    Returns:
        high_rating_restaurants (dict): A dictionary containing restaurants' names(key) and ratings(value)
    """
    high_rating_restaurants = {}

    for restaurant in restaurants:
        if restaurant['Category'] in category and restaurant['Rating'] >= 3.5:
            high_rating_restaurants[restaurant['Name']] = restaurant['Rating']

    return high_rating_restaurants

# Problem 04 (4 points)
def get_avg_rating(high_rating_restaurant):
    """
    This function takes a dictionary as an argument and returns the average value of the values inside the dictionary

    Parameters:
        high_rating_restaurant (dict): A dictionary containing restaurants' names(key) and ratings(value)

    Returns:
        avg_rating (float): average rating of the restaurants
    """
    avg_rating = sum(high_rating_restaurant.values())/len(high_rating_restaurant)

    return avg_rating

# Problem 05 (4 points)
def write_txt(filepath, data):
    """
    This function takes a txt filepath and a list of dictionaries as arguments and outputs them to the specified text file

    Parameters:
        filepath (str): A filepath of a txt file to be written to
        data (list): A list of dictionaries, each representing a restaurant

    Returns:
        None
    """
    with open(filepath, 'w', encoding='utf-8') as file_obj:
        for line in data:
            line = list(line.items())[:3]
            file_obj.write(f"{str(line)}\n")

# Call functions below
def main():
    """
    This function serves as the point of entry and controls the flow of this Python script

    Parameters:
        None

    Returns:
        None
    """

    # Problem 01
    print("Problem 01:\n")
    korean_restaurants = get_restaurants(restaurants, 'Korean')
    print(korean_restaurants)

    # Problem 02
    print("Problem 02:\n")
    most_reviewed_restaurant = get_most_reviewed_restaurant(restaurants)
    print(most_reviewed_restaurant)

    # Problem 03
    print("Problem 03:\n")
    categories = ['Burgers', 'Chinese']
    high_rating_restaurants = get_high_rating_restaurants(restaurants, categories)
    print(high_rating_restaurants)

    # Problem 04
    print("Problem 04:\n")
    avg_rating = get_avg_rating(high_rating_restaurants)
    print(avg_rating)

    # Problem 05
    write_txt('restaurant_info.txt', restaurants)

if __name__ == "__main__":
    main()