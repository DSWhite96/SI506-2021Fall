# START LAB EXERCISE 02
print('Lab Exercise 02 \n')

companies = 'Ford, 11.54; Honda, 29.82; General Motors Company, 57.22; Toyota, 150.77; Tesla, 709.44'

# PROBLEM 1 (4 points)

company_stocks = companies.replace(',', ":")
print(company_stocks)

# PROBLEM 2 (4 points)

automotive_stocks = company_stocks.split("; ")
print(automotive_stocks)

# PROBLEM 3 (4 points)

companies_num = len(automotive_stocks)
print(companies_num)

# PROBLEM 4 (4 points)

statement = f"In this list, there are {companies_num} automotive companies and their stock prices on May 1st, 2021."
print(statement)

# PROBLEM 5 (4 points)

three_lowest_companies = automotive_stocks[0:3]
print(three_lowest_companies)

# END LAB EXERCISE
