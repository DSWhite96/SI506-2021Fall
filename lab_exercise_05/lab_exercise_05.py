# START LAB EXERCISE 05
print('Lab Exercise 05 \n')

import os

# PROBLEM 01

def read_file(filepath):
    """Reads text file and returns each line as a list element.

    Parameters:
        filepath (str): path to file

    Returns
        list: list of all lines in the file
    """
    pass

filepath = 'project_data.txt' # Gradescope

# Create filepath using the os module (COMMENT OUT BEFORE SUBMITTING TO GRADESCOPE)
# abs_path = os.path.dirname(os.path.abspath(__file__))
# filepath = os.path.join(abs_path, 'project_data.txt')

projects = None
print(f"\n1.0 {projects}")

# PROBLEM 02
def get_filtered_projects(projects,categories):
    """
    This function returns a filtered list of projects based on one or more passed in categories.

    Parameters:
        projects (list): a list of strings that represent project information.
        categories (list): list of categories used as filters

    Returns:
        list: A filtered list of tuples. Each tuple contains both project name and project goal
    """
    pass

categories = ['data', 'UI/UX']
data_ux_projects = None

print(f"\n2.0 {data_ux_projects}")

# PROBLEM 03
