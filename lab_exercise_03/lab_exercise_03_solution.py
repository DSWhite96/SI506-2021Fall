# Lab Exercise 03
print('Lab Exercise 03 \n')

# Setup
companies = [
    "Domino's, Ann Arbor, 14400, Food",
    "Fisher Investments, Camas, 3500, financial",
    "M&T Bank, Buffalo, 16840, Financial",
    "Dimensional Insight, Burlington, 102, Tech",
    "Bloomingdale's, New York, 6500, Retail",
    "Meijer, Grand Rapids, 70000, Retail",
    "CIL Management Consultants, Chicago, 189, Consulting"]

# Problem 01 (3 points)

locations = []
for company in companies:
    locations.append(company.split(', ')[1])

print(f"\n1. locations = {locations}")

# Problem 02 (4 points)

financial_co = []
for company in companies:
    company = company.split(', ')
    if company[-1].lower() == "financial":
        financial_co.append(company[0])

print(f"\n2. financial_co = {financial_co}")

# Problem 03 (4 points)

count = 0
for company in companies:
    company = company.split(', ')
    if company[-1].lower() == 'retail':
        count += 1

print(f"\n3. There are in total of {count} companies in the retail industry")

# Problem 04 (4 points)

small_companies = []
medium_companies = []
large_companies = []
for company in companies:
    company = company.split(', ')
    num_employees = int(company[2])
    if num_employees < 500:
        small_companies.append(company[0])
    elif 500 <= num_employees < 5000:
        medium_companies.append(company[0])
    else:
        large_companies.append(company[0])

# Problem 05 (5 points)

largest = 0
for company in companies:
    company = company.split(', ')
    num_employees = int(company[2])
    if num_employees > largest:
        largest = num_employees
        largest_company = company[0]

print(f"\n5. The largest company in the list is {largest_company}")