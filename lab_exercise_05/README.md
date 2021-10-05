# SI 506: Lab Exercise 05

## Background

This week's lab exercise focuses on reading from and writing to a file using data sourced from the Design Clinic Program held by the UMSI Engagement Learning Office. Design Clinic is a program that seeks innovative solutions to information challenges. Interdisciplinary teams of four to six students, mentored by professionals, collaborate and innovate on fast-paced, self-driven, semester-long projects for real-world clients. If you are interested in participating in this program, you can find more information at https://www.si.umich.edu/programs/engaged-learning/design-and-innovation. Data for the lab exercise is contained in `project_data.txt`, which includes a list of projects organized by `< project type >`, `< project name >` and `< project goal >`.

## Create filepath using the `os` module
```python
abs_path = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(abs_path, 'project_data.txt')
```

:exclamation: Before submitting the assignment to Gradescope comment out the two variables that
rely on `os.path` for their values.

## 1.0 Problem 01 (6 Points)

1. Implement the `read_file()` function.  The function accepts a filepath string and returns each
line in the text file as a list element.

   * utilize the built-in `open()` function and the `with` keyword to open the file.
   * the `readlines()` method is a great tool in reading a text file.
   * utilize the `str.strip()` method to get rid of the new line character.

2. Call the function by passing the argument `filepath`. Assign the return value to the variable `projects`.

   * your result must match the result below:

```python
['Project Type,Project Name,Project Goal', 'Data Project,Patient Satisfaction Tableau Dashboard,Build a Tableau Dashboard to get information on patient satisfaction at multiple levels', 'Archives Project,Detroit Archives Creation,Establish an archive to chronicle 20 years for the nonprofit organization', 'Libraries Project,Design of University Library Website,Redesign of a university library website with a focus on accessibility', 'UI/UX Project,Online Education Platform Development for K-12 students,Develop a UX/UI experience for a minimum viable product that can be user tested in student environments', 'UI/UX Project,TimeBanks Website Updates,Upgrade and redesign the website for the nonprofit organization', 'UI/UX Project,Website Rebrand and Redesign for Entrepreneurship Fund,Update the website to align with the next phase of growth for the organization']
```

## 2.0 Problem 02 (8 Points)

1. Implement the `get_filtered_projects` function. The function accepts two parameters: a list of projects and a list of categories used to filter on the project's category. To implement this function, you need to loop through the `projects` list and utilize `str.split()` method to create a list of strings for each element in the `projects` list. Then apply list unpacking to unpack the `< project type >`, `< project name >`, `< project goal>`. Then loop through the `categories` list to check if the project type belongs to one of the categories. If the condition is met, append a tuple of the project name and its goal to the empty list `filtered_projects`.

   * in this problem, you will need to write a nested `for` loop and an `if` statement inside the loop.
   * utilize the `str.split()` method to split the elements in the list
   * utilize the `str.lower()` method to perform the case-insensitive string comparision.

2. Call the function by passing the argument `projects`
returned from Problem 01 and the `categories` list `['data', 'UI/UX']`. Assign the return value to the variable `data_ux_projects`.

   * the function returns a list of tuples, with each nested tuple comprising project name and project goal. Your result must match the result below:

```python
[('Patient Satisfaction Tableau Dashboard', 'Build a Tableau Dashboard to get information on patient satisfaction at multiple levels'), ('Online Education Platform Development for K-12 students', 'Develop a UX/UI experience for a minimum viable product that can be user tested in student environments'), ('TimeBanks Website Updates', 'Upgrade and redesign the website for the nonprofit organization'), ('Website Rebrand and Redesign for Entrepreneurship Fund', 'Update the website to align with the next phase of growth for the organization')]
```

## 3.0 Problem 03 (6 Points)

1. Implement the `write_file` function. The function accepts two arguments: a filepath string and a
sequence (e.g., `list`). The function _must_ write each list element to its own line in the file created.

2. Call the function and pass to it the filepath string `'data_ux_projects.txt'` and the list of tuples `data_ux_projects` returned from Problem 02.
